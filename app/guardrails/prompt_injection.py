
class PromptInjectionDetector:

    PATTERNS = [

        "ignore previous instructions",

        "ignore all instructions",

        "reveal system prompt",

        "show system prompt",

        "developer prompt",

        "print context",

        "show retrieved documents",

        "bypass restrictions",

    ]

    def validate(
        self,
        query: str,
    ):

        lower_query = query.lower()

        for pattern in self.PATTERNS:

            if pattern in lower_query:

                raise ValueError(
                    "Prompt injection detected."
                )

        return query