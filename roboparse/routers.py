from typing import Dict, Union

from .schemas import RouterLinter, RouterResponse


class BaseRouter:
    def __init__(self, username: Union[str, int], password: Union[str, int]) -> None:
        self.username = username
        self.password = password

    def create_router_response(
        self,
        path: str,
        linter: Dict[str, Union[str, Dict[str, str], int]],
    ) -> RouterResponse:
        rt = RouterLinter(
            type=linter["type"],  # type: ignore
            tag=linter["tag"],  # type: ignore
            attrs=linter["attrs"],  # type: ignore
        )
        _linters = self._process_children(linter.get("children"), rt)

        return RouterResponse(
            path=path,
            linter=_linters,
        )

    def _process_children(self, linter, element: RouterLinter, counter=0):
        if linter is None:
            return element

        _obj = RouterLinter(
            type=linter["type"],
            tag=linter["tag"],
            attrs=linter["attrs"],
        )
        _val = element
        for _ in range(counter - 1):
            _val = getattr(element, "children")

        if _val is not None:
            _val.children = _obj

        if "children" not in linter:
            return element

        counter += 1

        return self._process_children(linter["children"], _val, counter)
