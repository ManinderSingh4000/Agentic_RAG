from app.ingestion.embeddings.embedder import (
    CohereEmbedder,
)

from app.vectorstore.search import (
    SearchManager,
)

embedder = CohereEmbedder()

manager = SearchManager()

query = "Why Firecrawl?"

query_vector = embedder.embed(
    query
)

results = manager.similarity_search(
    collection_name="knowledge_base",
    query_vector=query_vector,
    limit=3,
)

def pretty_print(
    results,
):

    for result in results:

        print()

        print("=" * 80)

        print(
            f"Score: {result.score}"
        )

        print(
            f"Title: {result.payload['title']}"
        )

        print(
            f"Content: { result.payload['content']}"
        )

pretty_print(results)