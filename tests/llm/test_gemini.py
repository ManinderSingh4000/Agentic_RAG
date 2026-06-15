from app.llm.gemini_provider import (
    GeminiProvider,
)

provider = GeminiProvider()

response = provider.generate(
    "Explain LangGraph State in one sentence."
)

print(response)