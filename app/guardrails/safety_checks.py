class SafetyChecks:

    MAX_QUERY_LENGTH = 5000

    def validate_query(
        self,
        query: str,
    ):

        if not query.strip():

            raise ValueError(
                "Query cannot be empty."
            )

        if len(query) > self.MAX_QUERY_LENGTH:

            raise ValueError(
                "Query exceeds allowed length."
            )

        return query