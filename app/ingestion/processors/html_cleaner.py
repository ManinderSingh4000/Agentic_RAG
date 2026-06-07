from bs4 import BeautifulSoup


class HtmlCleaner:

    def clean(
        self,
        html: str,
    ) -> str:

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        # Remove scripts
        for tag in soup.find_all("script"):
            tag.decompose()

        # Remove styles
        for tag in soup.find_all("style"):
            tag.decompose()

        # Remove navigation
        for tag in soup.find_all(
            ["nav", "header", "footer", "aside"]
        ):
            tag.decompose()

        # Prefer article content
        article = (
            soup.find("article")
            or soup.find("main")
        )

        if article:
            return str(article)

        return str(soup)