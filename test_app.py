from handlers import render_index, render_about
from server.server import Server
from server.router import Router


app = Server()
router = Router()

router.add_route(method="GET", path="/", handler=render_index)
router.add_route(method="GET", path="/about", handler=render_about)

app.add_router(router)
app.listen()
