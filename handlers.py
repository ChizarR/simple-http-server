from pathlib import Path
from server.render import render


def render_index() -> str:
    path_to_index_page = "./views/index.html"
    return render(path_to_index_page)


def render_about() -> str:
    path_to_about_page = "./views/about.html"
    return render(path_to_about_page)
