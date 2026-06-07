class ContextBuilder:

    def build(
        self,
        search_results,
    ):

        contexts = []

        sources = []

        for result in search_results:

            payload = result.payload


            contexts.append(
                            f"""
                                Source File : {payload['source']}
                                Section: {payload['title']}
                                Relevance Score: {result.score:.4f}

                                {payload['content']}
                            """
                        )

            sources.append(
                {
                    "source": payload.get(
                        "source"
                    ),
                    "title": payload.get(
                        "title"
                    ),
                    "score": result.score,
                }
            )

        return {
            "context": "\n\n".join(
                contexts
            ),
            "sources": sources,
        }