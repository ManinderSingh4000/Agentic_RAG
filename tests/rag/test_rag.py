from app.retrieval.retriever import (
    RetrieverService,
)

service = RetrieverService()


response = service.ask(
    "What is Langgraph State ?"
)

print()

print("=" * 80)

print("QUESTION")

print(response["query"])

print()

print("=" * 80)

print("ANSWER")

print(response["answer"])

print(response)