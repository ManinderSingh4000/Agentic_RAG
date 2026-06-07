from app.ingestion.pipeline import (
    IngestionPipeline,
)

from app.ingestion.embeddings.embedder import (
    CohereEmbedder,
)

from app.vectorstore.points import (
    PointManager,
)


pipeline = IngestionPipeline()

embedder = CohereEmbedder()

manager = PointManager()

chunks = pipeline.run(
    "knowledge_base/firecrawl_lead_enrichment.md"
)

for chunk in chunks:

    print("=" * 50)
    print("TITLE:", chunk["title"])
    print("CONTENT:", repr(chunk["content"]))

valid_chunks = []

for chunk in chunks:

    content = chunk.get("content", "")

    if not content or not content.strip():

        print(
            f"Skipping empty chunk: {chunk['title']}"
        )

        continue

    try:

        chunk["embedding"] = embedder.embed(
            content
        )

        valid_chunks.append(chunk)

    except Exception as e:

        print(
            f"Embedding failed for chunk '{chunk['title']}': {e}"
        )

if not valid_chunks:

    raise ValueError(
        "No valid chunks available for upsert."
    )

manager.upsert_chunks(
    "knowledge_base",
    valid_chunks,
)

print(
    f"{len(valid_chunks)} chunks stored successfully."
)