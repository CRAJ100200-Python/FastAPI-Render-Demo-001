import os
import numpy as np
from app.data import documents
from app.embeddings_cache import DOC_EMBEDDINGS

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

class SimpleVectorStore:
    def search(self, query_embedding, top_k=3):
        scores = [
            cosine_similarity(query_embedding, emb)
            for emb in DOC_EMBEDDINGS
        ]
        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [documents[i] for i in top_indices]

def get_vector_store():
    return SimpleVectorStore()