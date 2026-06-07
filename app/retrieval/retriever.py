from app.ingestion.embeddings.embedder import (
    CohereEmbedder,
)

from app.vectorstore.search import (
    SearchManager,
)

from app.retrieval.context_builder import (
    ContextBuilder,
)

from app.llm.groq_provider import (
    GroqProvider,
)

from app.prompts.retrieval import (
    RETRIEVAL_PROMPT,
)

class RetrieverService:

    def __init__(self):

        self.embedder = CohereEmbedder()

        self.search_manager = SearchManager()

        self.context_builder = ContextBuilder()

        self.llm = GroqProvider()

    def ask(
        self,
        query: str,
    ):

        query_vector = self.embedder.embed(
            query
        )

        results = self.search_manager.similarity_search(
            collection_name="knowledge_base",
            query_vector=query_vector,
            limit=5,
        )


        context_data = (
                        self.context_builder.build(
                            results
                        )
                    )

        context = (
                    context_data["context"]
                )

        sources = (
                    context_data["sources"]
                )

        unique_sources = {}

        for source in sources:

            key = (
                source["source"],
                source["title"]
            )

            if key not in unique_sources:
                unique_sources[key] = source

        sources = list(
            unique_sources.values()
        )

        prompt = RETRIEVAL_PROMPT.format(
            context = context,
            query = query,
        )

        answer = self.llm.generate(
            prompt
        )

        return {
            "query": query,
            "answer": answer,
            "sources" : sources,
        }