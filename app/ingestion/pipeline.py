from uuid import uuid4


from app.ingestion.chunking.markdown_chunker import (
    MarkdownChunker,
)

from app.ingestion.loaders.markdown_loader import (
    MarkdownLoader,
)

from app.ingestion.processors.markdown_cleaner import (
    MarkdownCleaner,
)

class IngestionPipeline:
    def __init__(self):
        self.loader = MarkdownLoader()
        self.cleaner = MarkdownCleaner()
        self.chunker = MarkdownChunker()

    def run(
        self,
        file_path: str,
    ) -> list[dict]:

        document = self.loader.load(
            file_path
        )

        document["content"] = self.cleaner.clean(
            document["content"]
        )

        document["document_id"] = str(
            uuid4()
        )

        chunks = self.chunker.chunk(
            document
        )

        return chunks