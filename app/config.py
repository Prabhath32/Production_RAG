import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# ==========================
# Azure OpenAI Configuration
# ==========================

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")


# ==========================
# Qdrant Configuration
# ==========================

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "company_knowledge_base"
)


# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"


# ==========================
# Chunking Configuration
# ==========================

CHUNK_SIZE = 300
CHUNK_OVERLAP = 75


# ==========================
# Retrieval Configuration
# ==========================

TOP_K = 20
FINAL_TOP_K = 5


# ==========================
# PDF Directory
# ==========================

PDF_DIRECTORY = "data/pdfs"