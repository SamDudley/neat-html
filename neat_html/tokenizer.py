from collections import deque
from collections.abc import Sequence

from .tokens import ClosingTag, Content, OpeningTag, Token
from .types import Children, Element, ElementOrString


class Tokenizer:
    def __init__(self) -> None:
        self.nodes: deque[ElementOrString] = deque()
        self.tokens: deque[Token] = deque()
        self.open_nodes: set[ElementOrString] = set()

    def tokenize(self, root_node: Sequence[Element]) -> deque[Token]:
        # TODO: Use `add_children` when types are fixed.
        self.nodes.extend(reversed(root_node))

        while self.nodes:
            node = self.nodes[-1]

            if isinstance(node, str):
                self.nodes.pop()
                self.add_token(Content(node))

            else:  # Node
                if node not in self.open_nodes:
                    if node.self_closing:
                        # We don't want to come back and process this node again.
                        self.nodes.pop()

                    self.add_children(node.children)
                    self.add_token(OpeningTag(node.tag, node.attrs))

                else:  # Closing
                    self.nodes.pop()
                    self.add_token(ClosingTag(node.tag))
                    self.open_nodes.remove(node)

                self.open_nodes.add(node)

        return self.tokens

    def add_children(self, children: Children) -> None:
        self.nodes.extend(reversed(children))

    def add_token(self, token: Token) -> None:
        self.tokens.append(token)
