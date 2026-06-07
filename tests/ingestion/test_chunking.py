from app.ingestion.pipeline import (
    IngestionPipeline,
)

pipeline = IngestionPipeline()

chunks = pipeline.run(
    "data/samples/langgraph.md"
)

for chunk in chunks:
    print(chunk)
    print("=" * 80)