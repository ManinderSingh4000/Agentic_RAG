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

from app.retrieval.reranker import (
    CohereReranker,
)

from app.observability.langfuse_client import (
    langfuse,
)

from app.prompts.retrieval import (
    RETRIEVAL_PROMPT,
)

from app.router.llm_router import (
    LLMRouter,
)

class RetrieverService:

    def __init__(self):

        self.embedder = CohereEmbedder()

        self.search_manager = SearchManager()

        self.context_builder = ContextBuilder()

        self.reranker = CohereReranker()

        # self.llm = GroqProvider()
        self.llm = LLMRouter()

    def ask(
        self,
        query: str,
    ):

        with langfuse.start_as_current_observation(
            as_type="span",
            name="rag-query",
        ):

            # --------------------------
            # Embedding
            # --------------------------

            with langfuse.start_as_current_observation(
                as_type="span",
                name="embedding",
            ):

                query_vector = (
                    self.embedder.embed(
                        query
                    )
                )

            # --------------------------
            # Retrieval
            # --------------------------

            with langfuse.start_as_current_observation(
                as_type="span",
                name="retrieval",
            ):

                results = (
                    self.search_manager.similarity_search(
                        collection_name="knowledge_base",
                        query_vector=query_vector,
                        limit=20,
                    )
                )

            # --------------------------
            # Reranking
            # --------------------------

            with langfuse.start_as_current_observation(
                as_type="span",
                name="reranking",
            ):

                results = (
                    self.reranker.rerank(
                        query=query,
                        search_results=results,
                        top_n=5,
                    )
                )

            # --------------------------
            # Context Building
            # --------------------------

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
                    source["title"],
                )

                if key not in unique_sources:

                    unique_sources[
                        key
                    ] = source

            sources = list(
                unique_sources.values()
            )

            # --------------------------
            # Prompt
            # --------------------------

            prompt = (
                RETRIEVAL_PROMPT.format(
                    context=context,
                    query=query,
                )
            )

            # --------------------------
            # Generation
            # --------------------------

            with langfuse.start_as_current_observation(
                as_type="generation",
                name="groq-generation",
            ) as generation:

                generation.update(
                    input=prompt,
                    model="llama-3.3-70b-versatile",
                )

                # answer = (
                #     self.llm.generate(
                #         prompt
                #     )
                # )

                llm_response = (
                                self.llm.generate_auto(
                                    prompt
                                )
                            )
                answer = (
                    llm_response["response"]
                )

                provider = (
                    llm_response["provider"]
                )

                generation.update(
                    output=answer,
                )

            langfuse.flush()

            return {
                "query": query ,
                "provider" : provider ,
                "answer": answer,
                "sources": sources,
            }