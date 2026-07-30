import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# Azure OpenAI Configuration
# ==========================
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# ==========================
# Embedding Model
# ==========================
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Vector Dimension
VECTOR_SIZE = 384

# ==========================
# Qdrant Configuration
# ==========================
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
QDRANT_COLLECTION = "company_knowledge_base"

# ==========================
# Retrieval Configuration
# ==========================
TOP_K = 5

# ==========================
# Chunking Configuration
# ==========================
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ==========================
# PDF Directory
# ==========================
PDF_DIRECTORY = "data/pdfs"