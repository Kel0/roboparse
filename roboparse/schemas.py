from dataclasses import dataclass
from typing import Callable, Dict, Optional


@dataclass
class Filter:
    method: Callable

    def __call__(self, *args, **kwargs):
        return self.method(*args, **kwargs)


@dataclass
class RouterLinter:
    type: str
    tag: str
    attrs: Dict[str, str]
    children: Optional["RouterLinter"] = None
    index: Optional[int] = None


@dataclass
class RouterResponse:
    path: str
    linter: RouterLinter
