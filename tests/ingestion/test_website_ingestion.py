
from app.ingestion.website_ingestion_pipeline import (
    WebsiteIngestionPipeline,
)

pipeline = (
    WebsiteIngestionPipeline()
)

result = pipeline.ingest(
    url=(
        "https://pydantic.dev/docs/ai/overview/"
    ),
    file_name="pydantic_ai.md",
)

print()

print("Saved To:")

print(result)