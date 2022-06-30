from collections.abc import Callable
from .exceptions import RouteIsExistError, RouteIsNotExist 


class Router:
    def __init__(self):
        self._endpoints = dict()

    def get_endpoints(self) -> dict:
        return self._endpoints

    def add_route(self, method: str, path: str,
                  handler: type[Callable]) -> None:
        """Add Route-Method-Handler to Endpoints"""
        self._request(path=path, handler=handler, method=method)

    def create_response(self, method: str, path: str):
        """Return method, which connected to the route"""
        try:
            return self._endpoints[path][method]()
        except KeyError:
            return RouteIsNotExist()

    def _request(self, path: str, handler: type[Callable],
                 method: str="GET") -> None:
        """Create a new endpoint in requests list"""
        if self._check_if_endpoint_exists(method, path):
            raise RouteIsExistError()
        self._endpoints[path] = {method: handler}

    def _check_if_endpoint_exists(self, method: str, path: str) -> bool:
        """Check if endpoint with such method is exists"""
        try:
            self._endpoints[path][method]
            return True
        except:
            return False
