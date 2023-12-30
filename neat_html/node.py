from typing import TYPE_CHECKING, Optional

from .utils import is_self_closing_tag

if TYPE_CHECKING:
    from .types import HtmlAttributes


Children = list["NodeType"]


class Node:
    def __init__(
        self,
        tag: str,
        attrs: Optional["HtmlAttributes"] = None,
        children: Optional["Children"] = None,
    ):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = children or []

    @property
    def self_closing(self) -> bool:
        return is_self_closing_tag(self.tag)


class TextNode:
    def __init__(self, text: str, *, safe: bool = False):
        self.text = text
        self.safe = safe


NodeType = Node | TextNode
