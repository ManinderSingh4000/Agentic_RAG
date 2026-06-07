import asyncio

from app.ingestion.loaders.web_loaders import (
    WebLoader
)

loader = WebLoader()

result = asyncio.run(
    loader.load(
        "https://fastapi.tiangolo.com"
    )
)

print(result["markdown"][:1000])