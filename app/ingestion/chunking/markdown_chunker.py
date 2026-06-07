import re
from uuid import uuid4


class MarkdownChunker:
    HEADER_PATTERN = r"^(#{1,6})\s+(.*)$"

    def chunk(
        self,
        document: dict,
    ) -> list[dict]:

        content = document["content"]

        lines = content.splitlines()

        chunks = []

        current_title = None
        current_content = []

        chunk_index = 0

        for line in lines:

            match = re.match(
                self.HEADER_PATTERN,
                line,
            )

            if match:

                if current_title:

                    chunks.append(
                        {
                            "chunk_id": str(uuid4()),
                            "document_id": document.get(
                                "document_id"
                            ),
                            "source": document["source"],
                            "title": current_title,
                            "content": "\n".join(
                                current_content
                            ).strip(),
                            "chunk_index": chunk_index,
                        }
                    )

                    chunk_index += 1

                current_title = match.group(2).strip()

                current_content = []

            else:
                current_content.append(line)

        if current_title:

            chunks.append(
                {
                    "chunk_id": str(uuid4()),
                    "document_id": document.get(
                        "document_id"
                    ),
                    "source": document["source"],
                    "title": current_title,
                    "content": "\n".join(
                        current_content
                    ).strip(),
                    "chunk_index": chunk_index,
                }
            )

        return chunks