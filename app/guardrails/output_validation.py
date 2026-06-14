
class OutputValidator:

    BLOCKLIST = [

        "system prompt",

        "developer instructions",

        "retrieved context",

        "internal prompt",

    ]

    def validate(
        self,
        answer: str,
    ):

        lower = answer.lower()

        for pattern in self.BLOCKLIST:

            if pattern in lower:

                raise ValueError(
                    "Unsafe output detected."
                )

        return answer