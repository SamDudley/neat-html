from collections.abc import Sequence
from typing import overload

from .compiler import Compiler
from .tokenizer import Tokenizer
from .types import Element, HtmlAttributes, SafeString

__all__ = ["h", "render", "safe", "Element", "SafeString"]


@overload
def h(
    tag: str,
    /,
) -> Element: ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    /,
) -> Element: ...  # pragma: no cover


@overload
def h(
    tag: str,
    children: Sequence[Element | str] | Element | str,
    /,
) -> Element: ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    children: Sequence[Element | str] | Element | str,
    /,
) -> Element: ...  # pragma: no cover


def h(
    tag: str,
    attrs_or_children: (
        HtmlAttributes | Sequence[Element | str] | Element | str | None
    ) = None,
    children: Sequence[Element | str] | Element | str | None = None,
    /,
) -> Element:
    """
    Used for building html using python functions.

    1 arg - tag
    2 args - tag, attrs or children
    3 args - tag, attrs, and children
    """
    tag, attrs, children = _handle_args(tag, attrs_or_children, children)
    return Element(tag, attrs, children)


def render(elements: Element | Sequence[Element]) -> str:
    if isinstance(elements, Element):
        elements = [elements]

    tokens = Tokenizer().tokenize(elements)
    return Compiler().compile(tokens)


def safe(string: str) -> SafeString:
    return SafeString(string)


def _handle_args(
    tag: str,
    attrs_or_children: (
        HtmlAttributes | Sequence[Element | str] | Element | str | None
    ) = None,
    children: Sequence[Element | str] | Element | str | None = None,
    /,
) -> tuple[str, HtmlAttributes, list[Element | str]]:
    args = (tag, attrs_or_children, children)
    match args:
        # 1: h("")
        case [str(), None, None]:
            return args[0], {}, []
        # 2: h("", {})
        case [str(), dict(), None]:
            return args[0], args[1], []
        # 2: h("", [])
        case [str(), list(), None]:
            return args[0], {}, args[1]
        # 2: h("", h("")) OR h("", "")
        case [str(), Element() | str(), None]:
            return args[0], {}, [args[1]]
        # 3: h("", {}, [])
        case [str(), dict(), list()]:
            return args[0], args[1], args[2]
        # 3: h("", {}, h("")) OR h("", {}, "")
        case [str(), dict(), Element() | str()]:
            return args[0], args[1], [args[2]]
        case _:
            raise ValueError("Invalid arguments")
