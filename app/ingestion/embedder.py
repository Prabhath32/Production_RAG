from sentence_transformers import SentenceTransformer

from app.config import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Generates embeddings for text chunks using the configured
    SentenceTransformer model.
    """

    def __init__(self):

        print(f"\nLoading Embedding Model: {EMBEDDING_MODEL}")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print("Embedding Model Loaded Successfully.\n")

    def generate_embeddings(self, chunks):
        """
        Input:
            List of chunk dictionaries.

        Output:
            List of dictionaries containing metadata + embedding.
        """

        embedded_chunks = []

        print(f"Generating embeddings for {len(chunks)} chunks...\n")

        for chunk in chunks:

            embedding = self.model.encode(
                chunk["text"],
                normalize_embeddings=True
            )

            embedded_chunks.append(
                {
                    "document": chunk["document"],
                    "page": chunk["page"],
                    "chunk": chunk["chunk"],
                    "text": chunk["text"],
                    "embedding": embedding.tolist()
                }
            )

        print("Embedding Generation Completed.")

        return embedded_chunks