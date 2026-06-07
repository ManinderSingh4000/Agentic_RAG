from app.ingestion.embeddings.embedder import (
    CohereEmbedder
)

embedder = CohereEmbedder()

vector = embedder.embed(
    "LangGraph uses shared state."
)

print(len(vector))
print(vector[:10])