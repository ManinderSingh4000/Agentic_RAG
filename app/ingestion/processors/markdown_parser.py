# Responsibilities
"""
Markdown
   ↓
Extract Sections
   ↓
Structured Objects
"""
# Input
"""
# Pydantic AI

## Why use Pydantic AI

Pydantic AI is ...

## Hello World

Example ...
"""
# Output

"""
[
    {
        "h1": "Pydantic AI",
        "h2": "Why use Pydantic AI",
        "content": "Pydantic AI is ..."
    },
    {
        "h1": "Pydantic AI",
        "h2": "Hello World",
        "content": "Example ..."
    }
]
"""

import re


class MarkdownParser:

    def parse(
        self,
        markdown: str,
    ) -> list[dict]:

        sections = []

        current_h1 = None
        current_h2 = None

        content_buffer = []

        lines = markdown.splitlines()

        for line in lines:

            if line.startswith("# "):

                current_h1 = line.replace(
                    "# ",
                    "",
                ).strip()

            elif line.startswith("## "):

                if current_h2 and content_buffer:

                    sections.append(
                        {
                            "h1": current_h1,
                            "h2": current_h2,
                            "content": "\n".join(
                                content_buffer
                            ).strip(),
                        }
                    )

                current_h2 = line.replace(
                    "## ",
                    "",
                ).strip()

                content_buffer = []

            else:

                content_buffer.append(line)

        if current_h2 and content_buffer:

            sections.append(
                {
                    "h1": current_h1,
                    "h2": current_h2,
                    "content": "\n".join(
                        content_buffer
                    ).strip(),
                }
            )

        return sections