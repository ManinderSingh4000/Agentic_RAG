class ContextBuilder:

    def build(
        self,
        search_results,
    ) -> str:

        contexts = []

        for result in search_results:

            payload = result.payload

            contexts.append(
                    f"""
                        Source: {payload['title']}

                        {payload['content']}
                    """
            )

        return "\n\n".join(contexts)