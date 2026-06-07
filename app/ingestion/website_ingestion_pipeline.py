from app.ingestion.loaders.web_loaders import (
    WebLoader,
)

from app.ingestion.processors.html_to_markdown import (
    HtmlToMarkdown,
)

from app.ingestion.processors.markdown_cleaner import (
    MarkdownCleaner,
)

from app.storage.markdown_saver import (
    MarkdownSaver,
)


class WebsiteIngestionPipeline:

    def __init__(self):

        self.loader = WebLoader()

        self.converter = (
            HtmlToMarkdown()
        )

        self.cleaner = (
            MarkdownCleaner()
        )

        self.saver = (
            MarkdownSaver()
        )

    def ingest(
        self,
        url: str,
        file_name: str,
    ):

        html = self.loader.load(
            url
        )

        markdown = (
            self.converter.convert(
                html
            )
        )

        markdown = (
            self.cleaner.clean(
                markdown
            )
        )

        saved_file = (
            self.saver.save(
                markdown,
                file_name,
            )
        )

        return saved_file