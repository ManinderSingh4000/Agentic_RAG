import cohere

from app.core.config import (
    settings,
)


class CohereReranker:

    def __init__(self):

        self.client = cohere.ClientV2(
            api_key=settings.COHERE_API_KEY,
        )

    def rerank(
        self,
        query: str,
        search_results: list,
        top_n: int = 5,
    ):

        documents = []

        for result in search_results:

            payload = result.payload

            documents.append(
                f"""
                Title:
                {payload['title']}

                Content:
                {payload['content']}
                """
            )

        response = self.client.rerank(
            model="rerank-v3.5",
            query=query,
            documents=documents,
            top_n=top_n,
        )

        reranked_results = []

        for item in response.results:

            reranked_results.append(
                search_results[
                    item.index
                ]
            )

        return reranked_results