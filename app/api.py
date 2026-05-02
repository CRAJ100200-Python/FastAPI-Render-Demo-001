import os
from fastapi import FastAPI
from pydantic import BaseModel

from app.data import documents

app = FastAPI()

RAG_MODE = os.getenv("RAG_MODE", "simple")

if RAG_MODE == "langchain":
    from app.agent_langchain import build_retriever
    from app.rag_chain import build_rag_chain

    retriever = build_retriever(documents)
    rag_chain = build_rag_chain(retriever)

    def answer_fn(q):
        return rag_chain.invoke(q)

else:
    from app.agent_simple import get_vector_store
    from app.embeddings_cache import embed
    from app.rag_chain import build_rag_chain, format_docs

    store = get_vector_store()
    rag_chain = build_rag_chain()

    def answer_fn(q):
        query_embedding = embed(q)
        docs = store.search(query_embedding)
        context = format_docs(docs)

        return rag_chain.invoke({
            "context": context,
            "question": q
        })

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "HR RAG API is running"}

@app.post("/ask")
def ask(q: Query):
    return {"answer": answer_fn(q.question)}