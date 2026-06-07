from app.retrieval.retriever import (
    RetrieverService,
)

service = RetrieverService()

response = service.ask(
    "How does LangGraph state work?"
)

print()

print("=" * 80)

print("QUESTION")

print(response["query"])

print()

print("=" * 80)

print("ANSWER")

print(response["answer"])