from collections.abc import Sequence
from typing import Union

from .utils import is_self_closing_tag

HtmlAttributes = dict[str, object]
HtmlChild = Union["Element", str]
HtmlChildren = Sequence[HtmlChild] | HtmlChild


class Element:
    def __init__(
        self,
        tag: str,
        attrs: HtmlAttributes | None = None,
        children: list[HtmlChild] | None = None,
    ):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = children or []

    @property
    def self_closing(self) -> bool:
        return is_self_closing_tag(self.tag)


class SafeString(str): ...
