from app.llm.groq_provider import (
    GroqProvider,
)

from app.llm.gemini_provider import (
    GeminiProvider,
)


class LLMRouter:

    def __init__(self):

        self.providers = {
            "groq" : GroqProvider(),
            "gemini" : GeminiProvider()
        }

    def generate(
        self,
        prompt: str,
        provider : str = "groq"
    ) -> str:

        if provider not in self.providers:

            raise ValueError(
                f"Unknown provider: {provider}"
            )

        return (
            self.providers[
                provider
            ].generate(prompt)
        )

    def generate_auto(
                        self,
                        prompt: str,
                    ):

        providers = [
            "groq",
            "gemini",
        ]

        for provider in providers:

            try:

                response = (
                    self.providers[
                        provider
                    ].generate(prompt)
                )

                return {
                    "provider": provider,
                    "response": response,
                }

            except Exception as e:

                print(
                    f"{provider} failed: {e}"
                )
                