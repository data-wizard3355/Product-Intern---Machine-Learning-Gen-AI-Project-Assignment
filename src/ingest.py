"""
Ingestion stage of the RAG pipeline.

Pipeline stage: PDF -> Load -> Clean -> Chunk -> Embed -> Store (FAISS)

Run:
    python src/ingest.py --pdf data/paper.pdf --out vectorstore/
"""

import argparse
import os
import re

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_pdf(pdf_path: str):
    """Loads the PDF page-by-page, preserving page number metadata.
    Page numbers matter later: they let the chatbot cite exactly where
    an answer came from, which is what the submission form is asking for.

    PyMuPDF (fitz) generally extracts text in more reading-order-correct
    fashion than pypdf, which matters a lot on figure-heavy pages (word
    clouds, charts with axis labels) where pypdf tends to interleave
    label fragments with body text and garble the result.
    """
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load()
    return pages


def _alpha_ratio(text: str) -> float:
    """Fraction of characters that are alphabetic. Garbled figure-region
    text (scrambled labels, stray symbols, broken word-cloud extraction)
    tends to have a much lower ratio than normal prose."""
    if not text:
        return 0.0
    alpha = sum(c.isalpha() for c in text)
    return alpha / len(text)


def _looks_like_noise(text: str) -> bool:
    """Heuristic filter for chunks that are more likely to be extraction
    noise than usable content, e.g. from figure/chart regions where
    PyMuPDF pulls out scattered labels rather than sentences.

    Not used to DROP chunks (that risks losing real content) — only to
    tag them, so noisy chunks don't silently outrank clean prose during
    retrieval without you knowing why.
    """
    stripped = text.strip()
    if len(stripped) < 40:
        return True
    if _alpha_ratio(stripped) < 0.55:
        return True
    # Runs of single-char "words" (typical of scrambled label extraction)
    tokens = stripped.split()
    if tokens:
        short_token_ratio = sum(len(t) <= 2 for t in tokens) / len(tokens)
        if short_token_ratio > 0.45:
            return True
    return False


def clean_pages(pages):
    """Light normalization pass before chunking: collapses excessive
    whitespace/newlines that PDF extraction tends to leave behind, which
    otherwise inflates chunk_size accounting and can push real sentences
    across a chunk boundary."""
    for page in pages:
        text = page.page_content
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        page.page_content = text.strip()
    return pages


def chunk_documents(pages, chunk_size: int = 1000, chunk_overlap: int = 400):
    """Splits pages into overlapping chunks.

    chunk_overlap is set to 400 with a dense research paper,
    150 chars of overlap isn't always enough to keep a full sentence
    (e.g. a figure caption) from being split right at a page/chunk
    boundary. 250 costs a bit more storage/embedding time but noticeably
    reduces "the answer exists in the paper but got cut in half" misses.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(pages)

    # Tag each chunk with a stable id, and flag likely-noisy chunks so
    # you can inspect them later (e.g. `grep -l noisy` on a dump) without
    # blindly dropping content that might still be partially useful.
    noisy_count = 0
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i
        is_noisy = _looks_like_noise(chunk.page_content)
        chunk.metadata["is_noisy"] = is_noisy
        if is_noisy:
            noisy_count += 1

    print(f"      -> flagged {noisy_count}/{len(chunks)} chunks as likely extraction noise")
    return chunks


def build_faiss_index(chunks, out_dir: str, embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """Embeds chunks and persists a FAISS index to disk."""
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    os.makedirs(out_dir, exist_ok=True)
    vectorstore.save_local(out_dir)
    return vectorstore


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", default="data/paper.pdf")
    parser.add_argument("--out", default="vectorstore")
    parser.add_argument("--chunk-size", type=int, default=1000)
    parser.add_argument("--chunk-overlap", type=int, default=400)
    args = parser.parse_args()

    print(f"[1/4] Loading PDF: {args.pdf}")
    pages = load_pdf(args.pdf)
    print(f"      -> {len(pages)} pages loaded (using PyMuPDF)")

    print(f"[2/4] Cleaning page text")
    pages = clean_pages(pages)

    print(f"[3/4] Chunking (size={args.chunk_size}, overlap={args.chunk_overlap})")
    chunks = chunk_documents(pages, args.chunk_size, args.chunk_overlap)
    print(f"      -> {len(chunks)} chunks created")

    print(f"[4/4] Embedding chunks and building FAISS index -> {args.out}")
    build_faiss_index(chunks, args.out)
    print("Done. Index saved to", args.out)


if __name__ == "__main__":
    main()