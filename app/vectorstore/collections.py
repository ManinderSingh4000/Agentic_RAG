from qdrant_client.models import (
    VectorParams,
    Distance,
)

from app.vectorstore.qdrant_client import (
    QdrantManager,
)


class CollectionManager(QdrantManager):

    def create_collection(
        self,
        collection_name: str,
        vector_size: int = 1536,
    ):

        collections = self.client.get_collections()

        names = [
            c.name
            for c in collections.collections
        ]

        if collection_name in names:
            return

        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )