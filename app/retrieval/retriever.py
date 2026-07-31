from sentence_transformers import SentenceTransformer

from app.config import (
    EMBEDDING_MODEL,
    TOP_K
)

from app.vectordb.qdrant_db import QdrantManager


class Retriever:

    def __init__(self):

        print(f"\nLoading Embedding Model: {EMBEDDING_MODEL}")

        self.embedding_model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        self.embedding_dimension = (
            self.embedding_model.get_sentence_embedding_dimension()
        )

        print(f"Embedding Dimension : {self.embedding_dimension}")

        print("Embedding Model Loaded Successfully.\n")

        self.qdrant = QdrantManager()

    def retrieve(self, question: str):

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