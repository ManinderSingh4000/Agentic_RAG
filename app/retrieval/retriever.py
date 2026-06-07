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

        context = self.context_builder.build(
            results
        )

        prompt = f"""
                    You are a helpful assistant.

                    Answer ONLY using the provided context.

                    If the answer is not present in the context,
                    say you do not know.

                    Context:
                    {context}

                    Question:
                    {query}
                """

        answer = self.llm.generate(
            prompt
        )

        return {
            "query": query,
            "context": context,
            "answer": answer,
        }