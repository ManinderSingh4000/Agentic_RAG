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

        markdown = re.sub(
            r"\n{3,}",
            "\n\n",
            markdown,
        )

        markdown = re.sub(
            r"\[.*?\]\(javascript:.*?\)",
            "",
            markdown,
        )

        markdown = re.sub(
            r"^\s*$",
            "",
            markdown,
            flags=re.MULTILINE,
        )

        return markdown.strip()