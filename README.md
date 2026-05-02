# 🚀 HR Policy RAG System (Dual Mode)

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system with two modes:

- 🟢 Lightweight mode (production-ready)
- 🔵 LangChain + FAISS mode (demo / portfolio)

---

## 🧠 Architecture
User Query
↓
Embedding (Gemini)
↓
Retriever (Simple OR LangChain+FAISS)
↓
Context
↓
LLM (Gemini)
↓
Answer


---

## ⚙️ Modes

### 🟢 SIMPLE MODE (Default)
- No LangChain
- No FAISS
- Low RAM
- Runs on Render free tier

### 🔵 LANGCHAIN MODE
- Uses LangChain
- Uses FAISS
- Demonstrates RAG pipeline design

---

## 🔧 Setup

### 1. Clone repo

```bash
git clone <repo-url>
cd FastAPI-Render-Demo

