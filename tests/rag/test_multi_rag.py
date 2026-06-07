from pprint import pprint

from app.retrieval.retriever import (
    RetrieverService,
)


service = RetrieverService()

response = service.ask(
    "What is LangGraph State?"
)

print("\n" + "=" * 80)
print("QUERY")
print("=" * 80)

print(
    response["query"]
)

print("\n" + "=" * 80)
print("PROVIDER")
print("=" * 80)

print(
    response["provider"]
)

print("\n" + "=" * 80)
print("ANSWER")
print("=" * 80)

print(
    response["answer"]
)

print("\n" + "=" * 80)
print("SOURCES")
print("=" * 80)

for index, source in enumerate(
    response["sources"],
    start=1,
):

    print(
        f"\nSource #{index}"
    )

    pprint(source)

print("\n" + "=" * 80)
print("TEST COMPLETED")
print("=" * 80)