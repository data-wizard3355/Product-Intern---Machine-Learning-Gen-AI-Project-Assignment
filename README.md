# DevAI Paper RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that ingests the *Agent-as-a-Judge: Evaluating Agents with Agents* research paper and answers questions using relevant retrieved passages from the paper.

The project was built for the **Product Intern – Machine Learning & Gen-AI project assignment**.

## Architecture

```text
PDF
 ↓
PDF Loading
 ↓
Text Cleaning
 ↓
Recursive Chunking
 ↓
HuggingFace Embeddings
 ↓
FAISS Vector Store
 ↓
┌───────────────┐
│  User Query   │
└───────┬───────┘
        ↓
┌──────────────────┐
│ Hybrid Retrieval │
│                  │
│ FAISS + BM25     │
└────────┬─────────┘
         ↓
FlashRank Reranking
         ↓
   Prompt Assembly
         ↓
    Google Gemini
  gemini-3.1-flash-lite
         ↓
  Answer + Sources
```

A visual diagram of the pipeline is included in:

```text
docs/pipeline_diagram.png
```

## Project Structure

```text
agent-as-a-judge/
├── data/
│   └── paper.pdf
├── docs/
│   └── pipeline_diagram.png
├── outputs/
│   ├── answers.json
│   └── answers.md
├── src/
│   ├── answer_questions.py
│   ├── ingest.py
│   └── rag_pipeline.py
├── vectorstore/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## How It Works

### 1. PDF Loading

The paper is loaded page-by-page using **PyMuPDF** when available.

`PyPDFLoader` is used as a fallback.

Page metadata is preserved so that retrieved chunks can be traced back to their original page.

### 2. Text Cleaning

Extracted PDF text is normalized before chunking.

The cleaning step reduces excessive whitespace and line breaks that can otherwise affect chunk boundaries.

### 3. Chunking

The document is split using `RecursiveCharacterTextSplitter`.

Current configuration:

* **Chunk size:** 1000 characters
* **Chunk overlap:** 400 characters
* **Separators:** paragraph, line, sentence, word, and character boundaries

Each chunk is also assigned a `chunk_id`.

The ingestion pipeline additionally flags chunks that appear likely to contain extraction noise. These chunks are not removed from the index.

### 4. Embeddings and Vector Store

Each chunk is converted into an embedding using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The embeddings are stored locally using **FAISS**.

### 5. Hybrid Retrieval

For each user question, the system combines two retrieval approaches:

**FAISS dense retrieval**

Uses semantic similarity between the question and document chunks.

**BM25 sparse retrieval**

Uses keyword-based matching, which is particularly useful for exact terms, names, acronyms, and numerical information.

The two retrieval methods are combined using an ensemble with equal weights.

```text
FAISS    → 0.5
BM25     → 0.5
```

### 6. FlashRank Reranking

The retrieved results are passed through **FlashRank** to rerank the candidate chunks.

The final retrieval stage uses the most relevant chunks as context for the language model.

### 7. Answer Generation

The retrieved context and user question are passed to:

```text
Google Gemini
gemini-3.1-flash-lite
```

The generated answer is returned together with the retrieved source chunks, page numbers, and chunk IDs.

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_key_here
```

Do not commit the `.env` file or your API key to GitHub.

### 5. Add the research paper

Place the PDF at:

```text
data/paper.pdf
```

## Usage

### Build the Vector Index

Run the ingestion pipeline once for the paper:

```bash
python src/ingest.py --pdf data/paper.pdf --out vectorstore/
```

The ingestion pipeline:

1. Loads the PDF
2. Cleans the extracted text
3. Splits it into overlapping chunks
4. Generates embeddings
5. Builds the FAISS index
6. Saves the index locally

You can also customize the chunk size and overlap:

```bash
python src/ingest.py --pdf data/paper.pdf --out vectorstore/ --chunk-size 1000 --chunk-overlap 400
```

### Ask a Single Question

```bash
python src/rag_pipeline.py
```

This runs the RAG pipeline interactively so individual questions can be asked about the paper.

### Run the Question Bank

```bash
python src/answer_questions.py
```

The script runs the complete **15-question question bank** through the RAG pipeline.

It generates:

```text
outputs/answers.json
outputs/answers.md
```

`answers.json` stores the results in a structured format.

`answers.md` contains the questions, generated answers, and retrieved source chunks, including their page numbers and chunk IDs.

## Source Tracking

Each retrieved chunk contains metadata including:

```text
chunk_id
page
source
is_noisy
```

The question-answering output uses this information to identify the source chunks used for each answer.

This makes it possible to inspect which parts of the paper were retrieved for a particular question.

## Future Enhancements

Testing against the 15-question benchmark surfaced a few areas for future improvement.

### Reduce chunk-boundary truncation further

Some information can still be split across chunk boundaries. Increasing the chunk overlap from 250 to 400 characters already helped preserve information that was previously split across chunks; further tuning could reduce this further.

### Resolve retrieval ranking collisions

Some passages in the paper contain similar terminology and compare the same systems across different metrics. These passages can compete for the available retrieval slots.

A planned improvement is adding more detailed section or table metadata to help distinguish similar passages.

### Improve robustness to prompt-phrasing variation

Even when the relevant information is retrieved, the LLM can answer conservatively when the wording of the question differs significantly from the wording used in the paper.

This is a generation-side improvement rather than a retrieval fix, and could be addressed with query rewriting or few-shot prompting.

### Add multimodal PDF extraction

Figure-heavy pages, charts, word clouds, and multi-column layouts can produce less clean extracted text than normal paragraphs. Some content — such as bar charts — currently isn't captured at all by text-only extraction.

A future version could pass page images to a vision-capable model for figures and charts, in addition to the current PyMuPDF/PyPDFLoader text extraction.

### Stabilize retrieval across ingestion runs

Re-running the ingestion pipeline can occasionally change retrieval rankings, which may result in different chunks being selected for the same question. Pinning embedding/index build parameters more tightly could improve reproducibility.

## Tech Stack

* **Language:** Python
* **RAG Framework:** LangChain
* **PDF Loading:** PyMuPDF / PyPDF
* **Text Splitting:** RecursiveCharacterTextSplitter
* **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`
* **Vector Store:** FAISS
* **Sparse Retrieval:** BM25
* **Reranking:** FlashRank
* **LLM:** Google Gemini `gemini-3.1-flash-lite`
* **Environment Variables:** python-dotenv

## License

MIT
