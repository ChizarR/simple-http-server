from handlers import render_index, render_about
from server.response import Response
from server.router import Router
from server.server import Server
from server.types import StatusCode, ContentType, Charset


app = Server()
router = Router()

router.add_route(method="GET", path="/", handler=render_index)
router.add_route(method="GET", path="/about", handler=render_about)

app.add_router(router)
app.listen()
