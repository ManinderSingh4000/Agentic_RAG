from qdrant_client.models import (
    PointStruct,
)

from app.vectorstore.qdrant_client import (
    QdrantManager,
)


class PointManager(QdrantManager):

    def upsert_chunks(
        self,
        collection_name: str,
        chunks: list[dict],
    ):

        points = []

        for chunk in chunks:

            points.append(
                PointStruct(
                    id=chunk["chunk_id"],
                    vector=chunk["embedding"],
                    payload={
                        "document_id": chunk["document_id"],
                        "source": chunk["source"],
                        "title": chunk["title"],
                        "content": chunk["content"],
                        "chunk_index": chunk["chunk_index"],
                    },
                )
            )

        self.client.upsert(
            collection_name=collection_name,
            points=points,
        )