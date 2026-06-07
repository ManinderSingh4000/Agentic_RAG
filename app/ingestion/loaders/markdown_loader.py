from pathlib import Path


class MarkdownLoader:
    def load(self, file_path: str) -> dict:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        content = path.read_text(
            encoding="utf-8"
        )

        return {
            "filename": path.name,
            "source": str(path),
            "content": content,
        }