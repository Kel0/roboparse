from typing import Optional, Union

from bs4 import BeautifulSoup, ResultSet

from .filters import FilterFactory
from .schemas import RouterLinter, RouterResponse


class Parser:
    def __init__(self):
        self.bs4 = BeautifulSoup

    def _process_linter_with_children(self, soup: BeautifulSoup, linter: RouterLinter):
        if linter is None:
            return soup

        _meth = "find_all"
        if linter.type == "ELEMENT":
            _meth = "find"

        soup = (
            [getattr(el, _meth)(linter.tag, attrs=linter.attrs) for el in soup]
            if isinstance(soup, ResultSet)
            else getattr(soup, _meth)(linter.tag, attrs=linter.attrs)
        )
        if linter.children is None:
            return soup

        return self._process_linter_with_children(soup, linter.children)

    def _process_filters(self, element, filters):
        for _filter in filters.get():  # type: ignore
            element = _filter(element)
        return element

    def process_linters(
        self,
        soup: BeautifulSoup,
        linter: RouterLinter,
    ):
        element = self._process_linter_with_children(soup, linter)
        return element

    def load(
        self,
        html: Union[str, bytes],
        response: RouterResponse,
        filters: Optional[FilterFactory] = None,
    ):
        soup = self.bs4(html, "lxml")
        linted_element = self.process_linters(soup=soup, linter=response.linter)
        if filters is not None:
            linted_element = self._process_filters(linted_element, filters)

        return linted_element
