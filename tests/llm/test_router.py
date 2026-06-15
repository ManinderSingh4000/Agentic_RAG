from app.router.llm_router import (
    LLMRouter,
)

router = LLMRouter()

for provider in [
    "groq",
    "gemini"
    ]:
    print()

    print(
        "="*50
    )

    print(provider)

    print(
        "="*50
    )

    response = router.generate(
        prompt="What is LangGraph?",
        provider= provider,
    )

    print()

    print(response)