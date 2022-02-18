from .tokenizer import Tokenizer
from .compiler import Compiler
from .node import Node, TextNode
from .utils import handle_3_args


def h(*args):
    """
    Used for building html using python functions.

    1 arg - tag
    2 args - tag, attrs or children
    3 args - tag, attrs, and children
    """
    tag, attrs, children = handle_3_args(*args)
    children = [
        TextNode(child) if isinstance(child, str) else child
        for child in children
    ]
    node = Node(tag, attrs, children)
    node.html = lambda: html(node, format)
    return node


def html(node, format=True):
    tokens = Tokenizer().tokenize(node)
    return Compiler().compile(tokens, format=format)
