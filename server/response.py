from .types import StatusCode, ContentType, Charset


class Response:
    def __init__(self, status: StatusCode, content_type: ContentType,
                 charset: Charset, body: str):
        self._status = status.value
        self._content_type = content_type.value
        self._charset = charset.value
        self._body = body 
        self._headers = self._create_headers()
        self._response = self._create_response()

    def get(self) -> bytes:
        return self._response

    def _create_response(self):
        return f"{self._headers}{self._body}".encode("utf-8")

    def _create_headers(self) -> str:
        return (f"HTTP/1.1 {self._status}\n"
                f"Content-Type: {self._content_type}; "
                f"charset={self._charset}\n\n")

        

