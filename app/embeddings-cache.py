import os
import google.generativeai as genai
from app.data import documents

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def embed(text):
    return genai.embed_content(
        model="models/embedding-001",
        content=text
    )["embedding"]

DOC_EMBEDDINGS = [embed(doc) for doc in documents]
