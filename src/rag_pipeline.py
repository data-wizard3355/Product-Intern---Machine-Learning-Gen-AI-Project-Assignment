"""
Retrieval + generation stage of the RAG pipeline.

Pipeline stage: Query -> Hybrid Retrieve (FAISS + BM25) -> Rerank (FlashRank)
                -> Prompt Assembly -> GEMINI LLM -> Answer + Source Chunks

This module exposes `answer_question(query)` which returns both the
generated answer AND the exact source chunks used, since the assignment
asks you to paste chunks alongside your answers.
"""

import os
from dataclasses import dataclass, field
from typing import List

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever, ContextualCompressionRetriever
from langchain_community.document_compressors import FlashrankRerank
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GEMINI_MODEL = 'gemini-3.1-flash-lite'
VECTORSTORE_DIR = "vectorstore"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

PROMPT_TEMPLATE = """You are a precise research assistant answering questions about \
the attached paper using ONLY the context chunks provided below. If the context \
does not contain the answer, say so explicitly instead of guessing.

Context:
{context}

Question: {question}

Answer clearly and cite which part of the context supports your answer."""


@dataclass
class RAGResult:
    answer: str
    source_chunks: List[str] = field(default_factory=list)
    source_pages: List[int] = field(default_factory=list)
    source_chunk_ids: List[int] = field(default_factory=list)


def _load_documents_for_bm25(vectorstore: FAISS):
    """BM25 needs the raw documents, not just the FAISS index, so we pull
    them back out of the FAISS docstore rather than re-reading the PDF."""
    docs = list(vectorstore.docstore._dict.values())
    return docs


def build_retriever(vectorstore_dir: str = VECTORSTORE_DIR, top_k: int = 6):
    """Builds the hybrid retriever: dense (FAISS) + sparse (BM25),
    combined via EnsembleRetriever, then reranked with FlashRank.

    Why hybrid: FAISS/dense embeddings are good at semantic/paraphrased
    matches ("evaluation cost" ~ "how expensive is it to run"), while
    BM25 is good at exact keyword/acronym matches ("DevAI", "MetaGPT")
    which dense embeddings sometimes under-weight. Combining both covers
    more of the question types likely to show up in the question bank.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.load_local(
        vectorstore_dir, embeddings, allow_dangerous_deserialization=True
    )

    faiss_retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})

    docs = _load_documents_for_bm25(vectorstore)
    bm25_retriever = BM25Retriever.from_documents(docs)
    bm25_retriever.k = top_k

    ensemble_retriever = EnsembleRetriever(
        retrievers=[faiss_retriever, bm25_retriever],
        weights=[0.5, 0.5],
    )

    # Rerank the merged candidate pool down to the most relevant few —
    # this trims noise before it reaches the LLM's context window.
    compressor = FlashrankRerank(top_n=top_k)
    reranked_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=ensemble_retriever
    )

    return reranked_retriever


def build_chain(retriever):
    llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    temperature=0
)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    def format_docs(docs):
        return "\n\n".join(
            f"[Chunk {d.metadata.get('chunk_id')} | page {d.metadata.get('page')}]\n{d.page_content}"
            for d in docs
        )

    chain = (
        {"context": retriever | format_docs, "question": lambda x: x}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


def answer_question(query: str, retriever=None) -> RAGResult:
    """Answers a single question and returns the answer plus the exact
    chunks retrieved, so both can go into the submission form."""
    if retriever is None:
        retriever = build_retriever()

    docs = retriever.invoke(query)
    llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL,temperature=0)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    context = "\n\n".join(
        f"[Chunk {d.metadata.get('chunk_id')} | page {d.metadata.get('page')}]\n{d.page_content}"
        for d in docs
    )

    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": query})

    return RAGResult(
        answer=answer,
        source_chunks=[d.page_content for d in docs],
        source_pages=[d.metadata.get("page") for d in docs],
        source_chunk_ids=[d.metadata.get("chunk_id") for d in docs],
    )


if __name__ == "__main__":
    retriever = build_retriever()
    while True:
        q = input("\nAsk a question about the paper (or 'exit'): ")
        if q.lower() in ("exit", "quit"):
            break
        result = answer_question(q, retriever)
        print("\n--- ANSWER ---")
        print(result.answer)
        print("\n--- SOURCE CHUNKS ---")
        for i, chunk in enumerate(result.source_chunks):
            print(f"\n[Chunk {result.source_chunk_ids[i]}] (page {result.source_pages[i]}) {chunk[:300]}...")