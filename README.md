# 🚀 End-to-End AI RAG System with Evaluation Dashboard

A full-stack Retrieval-Augmented Generation (RAG) application that converts PDFs into embeddings, performs vector search using MongoDB Atlas, generates contextual answers using an LLM, and evaluates output quality with RAGAS metrics.

Includes:

✅ PDF ingestion pipeline  
✅ MongoDB Atlas vector search  
✅ LLM answer generation  <img width="1024" height="1536" alt="attach" src="https://github.com/user-attachments/assets/867e1310-c880-4aba-bc91-47bf10f460f4" />

✅ Retrieved evidence display  
✅ Automated RAG evaluation (Faithfulness, Relevance, Recall, Precision)  
✅ Metrics visualization dashboard  
✅ FastAPI backend  
✅ React frontend UI  

---

# 🧠 How It Works

### 1️⃣ Document Processing
- Load PDF files
- Split into text chunks
- Convert chunks into embeddings
- Store embeddings in MongoDB Atlas

### 2️⃣ Retrieval
- User asks a question
- Question converted to embedding
- MongoDB vector search retrieves closest chunks

### 3️⃣ Generation
- Retrieved context sent to LLM
- Model generates grounded answer

### 4️⃣ Evaluation
- RAGAS computes:
  - Faithfulness
  - Answer Relevance
  - Context Precision
  - Context Recall

### 5️⃣ Visualization
- Metrics plotted in dashboard
- Helps detect hallucinations & retrieval issues

---

# 🖥️ UI Preview

The UI shows:

- Question input box
- AI generated answer
- Retrieved PDF chunks
- RAG performance metrics graph

---

# 🏗️ Tech Stack

## Backend
- Python
- FastAPI
- OpenAI API
- MongoDB Atlas Vector Search
- RAGAS evaluation

## Frontend
- React
- Axios
- Recharts (metrics visualization)

---

# 📁 Project Structure

rag-project/
│
├── ingest.py # PDF → embeddings → MongoDB
├── rag_engine.py # Retrieval + generation logic
├── api.py # FastAPI backend
├── ragas_eval.py # evaluation pipeline
├── plot_metrics.py # metrics graph
├── pdfs/
│ └── sample.pdf
│
└── rag-ui/ # React frontend


---

# ⚙️ Setup Instructions

## 1️⃣ Clone repo


---

## 2️⃣ Install Python dependencies


---

## 4️⃣ Ingest PDF


---

## 5️⃣ Start backend


---

## 5️⃣ Start backend

#Architecture 
                    ┌─────────────────────┐
                    │      React UI       │
                    │                     │
                    │  Ask Question       │
                    │  Show Answer        │
                    │  Show Context       │
                    │  Show Metrics       │
                    └──────────┬──────────┘
                               │ API request
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │                     │
                    │  /ask endpoint      │
                    │  Handles query      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    RAG ENGINE       │
                    │                     │
                    │ 1 Convert query→vec │
                    │ 2 Retrieve context  │
                    │ 3 Send to LLM       │
                    │ 4 Return answer     │
                    └───────┬────────────┘
                            │
        ┌───────────────────┴──────────────────┐
        ▼                                      ▼

┌───────────────────────┐           ┌──────────────────────┐
│ MongoDB Atlas         │           │ OpenAI LLM           │
│ Vector Database       │           │                      │
│                       │           │ Generates grounded   │
│ Stores PDF embeddings │           │ answer using context │
│ Performs similarity   │           └──────────────────────┘
│ search                │
└───────────────────────┘


                    ▼
         ┌──────────────────────┐
         │ RAGAS Evaluation     │
         │                      │
         │ Faithfulness         │
         │ Answer Relevance     │
         │ Context Precision    │
         │ Context Recall       │
         └──────────┬───────────┘
                    ▼
          Metrics Visualization


#start command 
**npm run **

