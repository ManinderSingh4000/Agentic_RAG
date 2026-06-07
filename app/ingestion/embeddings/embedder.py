import cohere

from app.core.config import settings


class CohereEmbedder:

    def __init__(self):
        self.client = cohere.ClientV2(
            api_key=settings.COHERE_API_KEY
        )

    def embed(
        self,
        text: str
    ) -> list[float]:

        if not text or not text.strip():
            raise ValueError(
                "Cannot embed empty text"
            )

        response = self.client.embed(
            model="embed-v4.0",
            texts=[text],
            input_type="search_document",
        )

        return response.embeddings.float_[0]