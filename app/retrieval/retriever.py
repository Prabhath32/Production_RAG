from sentence_transformers import SentenceTransformer

from app.config import TOP_K
from app.vectordb.qdrant_db import QdrantManager


class Retriever:

    def __init__(self):

        print("Loading Embedding Model...")

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        print("Embedding Model Loaded")

        self.qdrant = QdrantManager()

    def retrieve(
        self,
        question: str
    ):

        print("\nGenerating Query Embedding...")

        query_vector = self.embedding_model.encode(
            question,
            normalize_embeddings=True
        ).tolist()

        print("Searching Qdrant...")

        results = self.qdrant.search(

            query_vector=query_vector,

            top_k=TOP_K

        )

        return results