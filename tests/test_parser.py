import pytest

from roboparse import Parser


@pytest.fixture
def parser() -> Parser:
    return Parser()


def test_parser(router, parser, helpers):
    html = helpers.get_html("samples/html_sample.txt")

    data = [str(e) for e in parser.load(html, router.get_something())]
    data.sort()

    expected_output = helpers.read_file("samples/response_sample.txt")
    expected_output.sort()

    assert data == expected_output
