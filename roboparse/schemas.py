from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class RouterLoop:
    exp: str
    value: Any


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
