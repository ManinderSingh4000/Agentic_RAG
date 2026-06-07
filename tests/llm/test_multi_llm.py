from app.retrieval.retriever import (
    RetrieverService,
)

service = RetrieverService()

response = service.ask(
    "What is LangGraph State?"
)

print()

print(
    response["answer"]
)

print()

print(
    response["sources"]
)