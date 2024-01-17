from collections.abc import Sequence
from typing import Any, overload

from .compiler import Compiler
from .tokenizer import Tokenizer
from .types import Element, HtmlAttributes, SafeString

__all__ = ["h", "render", "safe", "Element"]


@overload
def h(
    tag: str,
    /,
) -> Element:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    /,
) -> Element:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    children: Sequence[Element | str] | Element | str,
    /,
) -> Element:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    children: Sequence[Element | str] | Element | str,
    /,
) -> Element:
    ...  # pragma: no cover


def h(*args: Any) -> Element:
    """
    Used for building html using python functions.

    1 arg - tag
    2 args - tag, attrs or children
    3 args - tag, attrs, and children
    """
    tag, attrs, children = _handle_args(*args)
    return Element(tag, attrs, children)


def render(element: Element) -> str:
    tokens = Tokenizer().tokenize(element)
    return Compiler().compile(tokens)


def safe(string: str) -> SafeString:
    return SafeString(string)


def _handle_args(*args: Any) -> tuple[str, HtmlAttributes, list[Element | str]]:
    match args:
        # 1: h("p")
        case [str()]:
            return args[0], {}, []
        # 2: h("p", {"color": "red"})
        case [str(), dict()]:
            return args[0], args[1], []
        # 2: h("p", [...])
        case [str(), list()]:
            return args[0], {}, args[1]
        # 2: h("p", h("p")) OR h("p", "foo")
        case [str(), Element() | str()]:
            return args[0], {}, [args[1]]
        # 3: h("p", {"color": "red"}, [...])
        case [str(), dict(), list()]:
            return args[0], args[1], args[2]
        # 3: h("p", {"color": "red"}, h("p")) OR h("p", {"color": "red"}, "foo")
        case [str(), dict(), Element() | str()]:
            return args[0], args[1], [args[2]]
        case _:
            raise ValueError("Invalid arguments")
