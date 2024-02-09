from qdrant_client import QdrantClient, models
from uuid import uuid4
from .embeddings import embeddings
import json

__client = QdrantClient(host="localhost")
COLLECTION = "MAIN"


def upload(input: dict):
    embedding_text = json.dumps(input)
    point = models.PointStruct(
        id=uuid4().hex,
        vector=embeddings(embedding_text),
        payload={"content": embedding_text},
    )
    __client.upsert(collection_name=COLLECTION, wait=True, points=[point])


def search(query: dict):
    search_results = __client.search(
        collection_name=COLLECTION,
        query_vector=embeddings(json.dumps(query)),
        limit=3,
        with_payload=True,
        search_params=models.SearchParams(hnsw_ef=512, exact=True),
    )
    return search_results


def init():
    return __client.recreate_collection(
        collection_name=COLLECTION,
        hnsw_config=models.HnswConfigDiff(
            m=16,
            ef_construct=512,
            full_scan_threshold=10000,
        ),
        vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    )
