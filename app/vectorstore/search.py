from app.vectorstore.qdrant_client import (
    QdrantManager,
)


class SearchManager(QdrantManager):

    def similarity_search(
        self,
        collection_name: str,
        query_vector: list[float],
        limit: int = 5,
    ):

        results = self.client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=limit,
        )

        return results.points