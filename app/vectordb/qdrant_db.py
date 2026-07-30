from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

from app.config import (
    QDRANT_HOST,
    QDRANT_PORT,
    QDRANT_COLLECTION
)


class QdrantManager:

    def __init__(self):

        print("Connecting to Qdrant...")

        self.client = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT
        )

        print("Connected Successfully.")

    def create_collection(self):

        collections = self.client.get_collections().collections

        collection_names = [c.name for c in collections]

        if QDRANT_COLLECTION not in collection_names:

            self.client.create_collection(
                collection_name=QDRANT_COLLECTION,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

            print(f"Collection '{QDRANT_COLLECTION}' Created.")

        else:

            print(f"Collection '{QDRANT_COLLECTION}' Already Exists.")

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
            collection_name=QDRANT_COLLECTION,
            points=points
        )

        print(f"{len(points)} embeddings stored successfully.")

    def search(self, query_vector, top_k):

        response = self.client.query_points(
            collection_name=QDRANT_COLLECTION,
            query=query_vector,
            limit=top_k,
            with_payload=True,
            with_vectors=False
        )

        return response.points