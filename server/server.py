import socket
from .request import Request, ParsedRequest
from .router import Router


class Server:
    def __init__(self, ip_address="127.0.0.1"):
        self.IP_ADDRESS = ip_address
        self.PORT = None
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._routes: dict

    def listen(self, port: int=8000, connections_quantity: int=4) -> None:
        """Server starts listening for incoming connections"""
        self.PORT = port
        self._server.bind((self.IP_ADDRESS, self.PORT))
        self._server.listen(connections_quantity)
        print("SERVER conected")
        self._server_loop()

    def add_router(self, router: Router):
        """Take a router and return routes as dict"""
        self._routes = router.get_endpoints()

    def _server_loop(self) -> None:
        """Server keeps the connection open"""
        try:
            while True:
                client_socket, address = self._server.accept() 
                req = Request(client_socket.recv(1024).decode("utf-8"))
                response = self._create_response(req.get_parsed_req())
                client_socket.send(response)
                client_socket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            self._server.close()
            print("\n\nSERVER connection closed")

    def _create_response(self, req: ParsedRequest) -> bytes:
        """Create message with headers for respons"""
        header = "HTTP/1.1 200 OK\nContent-Type: text/html; charser=utf-8\n\n"
        try:
            res = f"{header}{self._routes[req.route][req.method]()}".encode()
            return res
        except:
            headers = "HTTP/1.1 404 OK\nContent=Type: text/html; charset=utf-8\n\n"
            res = f"{headers}Page not found".encode("utf-8")
            return res
            
