from typing import NamedTuple


class ParsedRequest(NamedTuple):
    method: str
    route: str


class Request:
    def __init__(self, request):
        self.method, self.route = self._parse_request(request)

    def get_parsed_req(self) -> ParsedRequest:
        return ParsedRequest(method=self.method, route=self.route)

    def _parse_request(self, request) -> ParsedRequest:
        raw_req = request.split(" ")[:2]
        return ParsedRequest(method=raw_req[0], route=raw_req[1])
