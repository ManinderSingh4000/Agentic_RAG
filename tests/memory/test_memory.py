from app.retrieval.retriever import (
    RetrieverService,
)

service = RetrieverService()

response = service.ask(
    "What is LangGraph?"
)

print(response["answer"])

print("\n" + "=" * 80 + "\n")

response = service.ask(
    "How does state work?"
)

print(response["answer"])

print(response)