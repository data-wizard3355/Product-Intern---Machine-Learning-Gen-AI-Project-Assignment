"""
Batch-runs a list of questions through the RAG pipeline and writes both
a JSON file (for your own records) and a Markdown file formatted for
copy-pasting into the submission form (answer + retrieved chunks).

Edit QUESTIONS below once you have the actual question bank, then run:
    python src/answer_questions.py
"""

import json
import os

from rag_pipeline import build_retriever, answer_question

QUESTIONS = [
    "What is the DevAI dataset, and how many tasks, requirements, and preferences does it contain?",
    "What percentage of evaluation time and cost does Agent-as-a-Judge save compared to using three human experts?",
    "According to Section 4.4 (Cost Analysis), how much did Agent-as-a-Judge cost and how long did it take, compared to Human-as-a-Judge?",
    "Which three open-source agentic frameworks were benchmarked on DevAI?",
    "What is the average cost and average time for OpenHands?",
    "Which system is the most cost-efficient and which is the most expensive?",
    "What was GPT-Pilot's \"Requirements Met (Independent)\" percentage under Human-as-a-Judge?",
    "What was MetaGPT's Task Solve Rate?",
    "In the black-box setting, what Alignment Rate did Agent-as-a-Judge vs. LLM-as-a-Judge achieve when evaluating OpenHands?",
    "What alignment rate does Agent-as-a-Judge achieve using only the \"ask\" component, and after adding \"graph,\" \"read,\" and \"locate\"?",
    "Which search algorithm (BM25, Sentence-BERT, Fuzzy Search, or no search module) gave the best alignment rate?",
    "Which two model architectures are mentioned most frequently in the DevAI user queries?",
    "What is requirement R1 in the \"Devin AI Software Engineer Plants Secret Messages in Images\" task?",
    "Which of the three human evaluators (231a, 38bb, cn9o) made the most errors when judging GPT-Pilot, and what was the error rate?",
    "In the diagram comparing LLM-as-a-Judge, Agent-as-a-Judge, and Human-as-a-Judge, what key drawback is highlighted for Human-as-a-Judge?",
]

OUT_DIR = "outputs"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    retriever = build_retriever()

    results = []
    md_lines = []

    for i, question in enumerate(QUESTIONS, start=1):
        print(f"[{i}/{len(QUESTIONS)}] {question}")
        result = answer_question(question, retriever)

        results.append(
            {
                "question": question,
                "answer": result.answer,
                "source_chunks": result.source_chunks,
                "source_pages": result.source_pages,
                "source_chunk_ids": result.source_chunk_ids,
            }
        )

        md_lines.append(f"### Q{i}: {question}\n")
        md_lines.append(f"**Answer:** {result.answer}\n")
        md_lines.append("**Retrieved chunks:**\n")
        for j, chunk in enumerate(result.source_chunks):
            md_lines.append(f"> Chunk {result.source_chunk_ids[j]} (page {result.source_pages[j]}): {chunk}\n")
        md_lines.append("\n---\n")

    with open(os.path.join(OUT_DIR, "answers.json"), "w",encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open(os.path.join(OUT_DIR, "answers.md"), "w",encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\nDone. See {OUT_DIR}/answers.json and {OUT_DIR}/answers.md")


if __name__ == "__main__":
    main()