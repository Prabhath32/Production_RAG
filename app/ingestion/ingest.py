from app.ingestion.loader import PDFLoader
from app.ingestion.cleaner import TextCleaner
from app.ingestion.chunker import TextChunker
from app.ingestion.embedder import EmbeddingGenerator

from app.vectordb.qdrant_db import QdrantManager


def run_ingestion():

    print("=" * 80)
    print("STARTING INGESTION PIPELINE")
    print("=" * 80)

    # ------------------------------------
    # Load PDFs
    # ------------------------------------

    loader = PDFLoader()

    documents = loader.load_documents()

    print(f"\nDocuments Loaded : {len(documents)}")

    # ------------------------------------
    # Clean Text
    # ------------------------------------

    cleaner = TextCleaner()

    cleaned_documents = cleaner.clean_documents(documents)

    print(f"Cleaned Pages : {len(cleaned_documents)}")

    # ------------------------------------
    # Chunk Documents
    # ------------------------------------

    chunker = TextChunker()

    chunks = chunker.chunk_documents(cleaned_documents)

    print(f"Chunks Created : {len(chunks)}")

    # ------------------------------------
    # Generate Embeddings
    # ------------------------------------

    embedder = EmbeddingGenerator()

    embedded_chunks = embedder.generate_embeddings(chunks)

    print(f"Embeddings Generated : {len(embedded_chunks)}")

    # ------------------------------------
    # Store in Qdrant
    # ------------------------------------

    qdrant = QdrantManager()

    qdrant.create_collection()

    qdrant.store_embeddings(embedded_chunks)

    print("\n" + "=" * 80)
    print("INGESTION COMPLETED SUCCESSFULLY")
    print("=" * 80)


if __name__ == "__main__":

    run_ingestion()