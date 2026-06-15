
class ContentFilter:

    BLOCKLIST = [
        "hate",
        "kill",
        "terrorist",
    ]

    def validate(
        self,
        text: str,
    ):

        lower = text.lower()

        for word in self.BLOCKLIST:

            if word in lower:

                raise ValueError(
                    "Unsafe content detected."
                )

        return text