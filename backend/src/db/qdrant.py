import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

# Initialize Qdrant Client
# For local instance, you might use host="localhost", port=6333
# For a remote instance, you'd configure host and potentially api_key
qdrant_client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def get_qdrant_client():
    return qdrant_client
