from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
)


class QdrantManager:

    def __init__(self):

        self.client = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT
        )

        print("Connected to Qdrant Successfully.")

    def create_collection(self):

        collections = self.client.get_collections().collections

        collection_names = [c.name for c in collections]

        if COLLECTION_NAME in collection_names:

            print(f"Collection '{COLLECTION_NAME}' already exists.")

            return

        self.client.create_collection(

            collection_name=COLLECTION_NAME,

            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )

        )

        print(f"Collection '{COLLECTION_NAME}' created successfully.")

    def store_embeddings(self, embedded_chunks):

        points = []

        for idx, chunk in enumerate(embedded_chunks):

            points.append(

                PointStruct(

                    id=idx,

                    vector=chunk["embedding"],

                    payload={

                        "document": chunk["document"],

                        "page": chunk["page"],

                        "chunk": chunk["chunk"],

                        "text": chunk["text"]

                    }

                )

            )

        self.client.upsert(

            collection_name=COLLECTION_NAME,

            points=points,

            wait=True

        )

        print(f"{len(points)} vectors stored successfully.")

    def search(self, query_vector, top_k=20):

        results = self.client.query_points(

            collection_name=COLLECTION_NAME,

            query=query_vector,

            limit=top_k,

            with_payload=True,

            with_vectors=False

        )

        return results.points