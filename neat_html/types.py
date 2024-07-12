from typing import Protocol, Union

from .utils import is_self_closing_tag


class SupportsStr(Protocol):
    def __str__(self) -> str: ...


HtmlAttributeValue = bool | SupportsStr
HtmlAttributes = dict[str, HtmlAttributeValue]
ElementOrString = Union["Element", str]
Children = list[ElementOrString]


class Element:
    def __init__(
        self,
        tag: str,
        attrs: HtmlAttributes | None = None,
        children: Children | None = None,
    ):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = children or []

    @property
    def self_closing(self) -> bool:
        return is_self_closing_tag(self.tag)


class SafeString(str): ...
