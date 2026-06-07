from qdrant_client import QdrantClient

from app.core.config import settings



class QdrantManager:

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )

    