from collections.abc import Sequence
from typing import Any, overload

from .compiler import Compiler
from .node import Node, NodeType, TextNode
from .tokenizer import Tokenizer
from .types import Children, HtmlAttributes

__all__ = ["h", "render", "safe", "Node"]


@overload
def h(
    tag: str,
    /,
) -> Node:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    /,
) -> Node:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    children: Sequence[NodeType | str] | NodeType | str,
    /,
) -> Node:
    ...  # pragma: no cover


@overload
def h(
    tag: str,
    attrs: HtmlAttributes,
    children: Sequence[NodeType | str] | NodeType | str,
    /,
) -> Node:
    ...  # pragma: no cover


def h(*args: Any) -> Node:
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
    node = Node(tag, attrs, node_children)
    return node


def render(node: Node) -> str:
    tokens = Tokenizer().tokenize(node)
    return Compiler().compile(tokens)


def safe(text: str) -> TextNode:
    return TextNode(text, safe=True)


def _handle_args(
    *args: Any,
) -> tuple[str, "HtmlAttributes", list["Node" | str] | str]:
    match args:
        case [str()]:
            return args[0], {}, []
        case [str(), dict()]:
            return args[0], args[1], []
        case [str(), list()]:
            return args[0], {}, args[1]
        case [str(), Node() | TextNode()]:
            return args[0], {}, [args[1]]
        case [str(), str()]:
            return args[0], {}, [args[1]]
        case [str(), dict(), list()]:
            return args[0], args[1], args[2]
        case [str(), dict(), Node() | TextNode()]:
            return args[0], args[1], [args[2]]
        case [str(), dict(), str()]:
            return args[0], args[1], [args[2]]
        case _:
            raise ValueError("Invalid arguments")
