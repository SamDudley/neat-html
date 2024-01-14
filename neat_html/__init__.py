from collections.abc import Sequence
from typing import Any, Union, overload

from .compiler import Compiler
from .node import Element, NodeType, TextNode
from .tokenizer import Tokenizer
from .types import Children, HtmlAttributes

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
    children: Sequence[NodeType | str] | NodeType | str,
    /,
) -> Element:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    children: Sequence[NodeType | str] | NodeType | str,
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
    node_children: Children = [
        TextNode(child) if isinstance(child, str) else child for child in children
    ]
    node = Element(tag, attrs, node_children)
    return node


def render(node: Element) -> str:
    tokens = Tokenizer().tokenize(node)
    return Compiler().compile(tokens)


def safe(text: str) -> TextNode:
    return TextNode(text, safe=True)


def _handle_args(
    *args: Any,
) -> tuple[str, "HtmlAttributes", list[Union["Element", str]] | str]:
    match args:
        case [str()]:
            return args[0], {}, []
        case [str(), dict()]:
            return args[0], args[1], []
        case [str(), list()]:
            return args[0], {}, args[1]
        case [str(), Element() | TextNode()]:
            return args[0], {}, [args[1]]
        case [str(), str()]:
            return args[0], {}, [args[1]]
        case [str(), dict(), list()]:
            return args[0], args[1], args[2]
        case [str(), dict(), Element() | TextNode()]:
            return args[0], args[1], [args[2]]
        case [str(), dict(), str()]:
            return args[0], args[1], [args[2]]
        case _:
            raise ValueError("Invalid arguments")
