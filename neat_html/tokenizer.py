from collections import deque
from collections.abc import Sequence

from .tokens import ClosingTag, Content, OpeningTag, Token
from .types import Element, HtmlChild


class Tokenizer:
    def __init__(self) -> None:
        self.nodes: deque[HtmlChild] = deque()
        self.tokens: deque[Token] = deque()
        self.open_nodes: set[HtmlChild] = set()

    def tokenize(self, root_nodes: Sequence[Element]) -> deque[Token]:
        self.add_children(root_nodes)

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

    def add_children(self, children: Sequence[HtmlChild]) -> None:
        self.nodes.extend(reversed(children))

    def add_token(self, token: Token) -> None:
        self.tokens.append(token)
