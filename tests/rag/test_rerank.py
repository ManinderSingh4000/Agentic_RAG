from app.retrieval.retriever import (
    RetrieverService,
)

service = RetrieverService()

response = service.ask(
    "What is  Langgraph State ?"
)

print()

print("ANSWER")
print(response["answer"])

print()

print("SOURCES")

for source in response["sources"]:

    print(source)