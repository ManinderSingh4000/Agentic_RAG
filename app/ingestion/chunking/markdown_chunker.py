import re
from uuid import uuid4


class MarkdownChunker:

    HEADER_PATTERN = r"^(#{1,6})\s+(.*)$"

    MAX_WORDS = 800

    OVERLAP = 150

    def _split_large_content(
        self,
        content: str,
    ) -> list[str]:

        words = content.split()

        if len(words) <= self.MAX_WORDS:
            return [content]

        chunks = []

        start = 0

        while start < len(words):

            end = start + self.MAX_WORDS

            chunk_words = words[start:end]

            chunks.append(
                " ".join(chunk_words)
            )

            start = (
                end
                - self.OVERLAP
            )

        return chunks

    def _append_chunk(
        self,
        chunks: list,
        document: dict,
        title: str,
        content: str,
        chunk_index: int,
    ) -> int:

        split_contents = (
            self._split_large_content(
                content
            )
        )

        for split_content in split_contents:

            if not split_content.strip():
                continue

            chunks.append(
                {
                    "chunk_id": str(
                        uuid4()
                    ),
                    "document_id": document.get(
                        "document_id"
                    ),
                    "source": document[
                        "source"
                    ],
                    "title": title,
                    "content": split_content,
                    "chunk_index": chunk_index,
                }
            )

            chunk_index += 1

        return chunk_index

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

                    section_content = (
                        "\n".join(
                            current_content
                        ).strip()
                    )

                    chunk_index = (
                        self._append_chunk(
                            chunks=chunks,
                            document=document,
                            title=current_title,
                            content=section_content,
                            chunk_index=chunk_index,
                        )
                    )

                current_title = (
                    match.group(2)
                    .strip()
                )

                current_content = []

            else:

                current_content.append(
                    line
                )

        if current_title:

            section_content = (
                "\n".join(
                    current_content
                ).strip()
            )

            chunk_index = (
                self._append_chunk(
                    chunks=chunks,
                    document=document,
                    title=current_title,
                    content=section_content,
                    chunk_index=chunk_index,
                )
            )

        return chunks