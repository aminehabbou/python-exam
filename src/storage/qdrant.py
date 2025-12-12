from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6359)
Collection_name = "messages"

if not client.collection_exists(collection_name=Collection_name):
    client.create_collection(
        collection_name=Collection_name,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )
