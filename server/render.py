from pathlib import Path


def render(file_path: str) -> str:
    html_file = Path(file_path)
    return html_file.read_text()
