
from app.ingestion.website_ingestion_pipeline import (
    WebsiteIngestionPipeline,
)

pipeline = (
    WebsiteIngestionPipeline()
)

result = pipeline.ingest(
    url=(
        "https://docs.firecrawl.dev/"
    ),
    file_name="firecrawl_lead_enrichment.md",
)

print()

print("Saved To:")

print(result)