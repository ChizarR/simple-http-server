from enum import Enum
from typing import NamedTuple


class ParsedRequest(NamedTuple):
    method: str
    route: str


class StatusCode(Enum):
    OK = "200 OK"
    MOVED_PERMANENTLY = "301 Moved Permanently"
    BAD_REQUEST = "400 Bad Request"
    FORBIDDEN = "403 Forbidden"
    NOT_FOUND = "404 Not Found"
    INTERNAL_SERVER_ERROR = "500 Internal Server Error"


class ContentType(Enum):
    TEXT_HTML = "text/html"
    APPLICATION_JSON = "application/json"
    TEXT_PLANE = "text/plane"


class Charset(Enum):
    UTF_8 = "utf-8"
