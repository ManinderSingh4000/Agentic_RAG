from pathlib import Path


class MarkdownSaver:

    def save(
        self,
        markdown: str,
        file_name: str,
    ):

        output_dir = Path(
            "knowledge_base"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = (
            output_dir / file_name
        )

        file_path.write_text(
            markdown,
            encoding="utf-8",
        )

        return str(file_path)