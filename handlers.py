from server.render import render
from server.response import Response
from server.types import StatusCode, ContentType, Charset



def render_index():
    path_to_index_page = "./views/index.html"
    return render(path_to_index_page, StatusCode.OK,
                  ContentType.TEXT_HTML, Charset.UTF_8)


def render_about():
    path_to_about_page = "./views/about.html"
    return render(path_to_about_page, StatusCode.OK,
                  ContentType.TEXT_HTML, Charset.UTF_8)
