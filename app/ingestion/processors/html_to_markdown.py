from markdownify import markdownify


class HtmlToMarkdown:

    def convert(
        self,
        html: str,
    ) -> str:

        markdown = markdownify(
            html,
            heading_style="ATX",
        )

        return markdown