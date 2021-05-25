import pytest
from roboparse import BaseRouter

import ast


class SampleRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_something(self):
        response = self.create_router_response(
            path="https://habr.com/ru/",  # Path is just meta data. It uses for nothing
            linter={
                "type": "LIST",
                "tag": "li",
                "attrs": {"class": "content-list__item"},
                "children": {
                    "type": "ELEMENT",
                    "tag": "h2",
                    "attrs": {"class": "post__title"},
                    "children": {
                        "type": "ELEMENT",
                        "tag": "a",
                        "attrs": {"class": "post__title_link"}
                    }
                }
            }
        )
        return response


class Helpers:
    def get_html(self, filename: str) -> bytes:
        with open(filename, "r") as f:
            html = f.read().encode()
        return html

    def read_file(self, filename):
        with open(filename, "r") as f:
            data = f.read()
        return ast.literal_eval(data)


@pytest.fixture
def helpers():
    return Helpers()


@pytest.fixture
def router() -> SampleRouter:
    return SampleRouter("username", "password")
