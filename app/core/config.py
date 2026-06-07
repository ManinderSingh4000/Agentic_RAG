from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    COHERE_API_KEY: str

    QDRANT_URL: str

    QDRANT_API_KEY: str

    GROQ_API_KEY : str

    class Config:
        env_file = ".env"


settings = Settings()