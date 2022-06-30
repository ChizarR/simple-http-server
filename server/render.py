from pathlib import Path
from .response import Response
from .types import StatusCode, ContentType, Charset


def render(file_path: str, status_code: StatusCode,
           content_type: ContentType, charset: Charset) -> bytes:
    """Return Response object to controllers"""
    html_file = Path(file_path).read_text()
    return Response(status_code, content_type, charset, html_file).get()
