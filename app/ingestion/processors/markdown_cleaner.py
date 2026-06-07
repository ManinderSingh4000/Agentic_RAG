# import re


# class MarkdownCleaner:

#     def clean(
#         self,
#         content: str,
#     ) -> str:

#         patterns = [
#             r"\[Edit this page\]",
#             r"^Previous$",
#             r"^Next$",
#         ]

#         for pattern in patterns:

#             content = re.sub(
#                 pattern,
#                 "",
#                 content,
#                 flags=re.MULTILINE,
#             )

#         return content.strip()


import re


class MarkdownCleaner:

    def clean(
        self,
        markdown: str,
    ) -> str:

        # Keep link text only
        markdown = re.sub(
            r"\[([^\]]+)\]\([^)]+\)",
            r"\1",
            markdown,
        )

        markdown = re.sub(
            r"## On this page.*?(?=\n#|\n##|\Z)",
                "",
            markdown,
            flags=re.DOTALL,
        )

        footer_markers = [
            "Suggest edits",
            "Raise issue",
            "Powered by",
        ]

        for marker in footer_markers:

            idx = markdown.find(marker)

            if idx != -1:
                markdown = markdown[:idx]

        # Remove images
        markdown = re.sub(
            r"!\[.*?\]\(.*?\)",
            "",
            markdown,
        )

        # Remove excessive blank lines
        markdown = re.sub(
            r"\n{3,}",
            "\n\n",
            markdown,
        )


        navigation_patterns = [
                                r"Firecrawl Docs home page",
                                r"Search\.\.\.",
                                r"Navigation",
                                r"DocumentationSDKsIntegrationsAPI ReferenceBuild with AI",
                                r"Playground",
                                r"Blog",
                                r"Community",
                                r"Changelog",
                                r"Get Started",
                                r"What's New",
                                r"Core Endpoints",
                                r"Quickstarts",
                                r"Developer Guides",
                                r"Webhooks",
                                r"Contributing",
                            ]

        return markdown.strip()