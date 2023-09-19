from collections import deque

from .node import Children, Node, NodeType, TextNode
from .tokens import ClosingTag, Content, OpeningTag, Token


class Tokenizer:
    def __init__(self) -> None:
        self.nodes: deque[NodeType] = deque()
        self.tokens: deque[Token] = deque()
        self.open_nodes: set[NodeType] = set()

    def tokenize(self, root_node: Node) -> deque[Token]:
        self.nodes.append(root_node)

        while self.nodes:
            node = self.nodes[-1]

            if isinstance(node, TextNode):
                self.nodes.pop()
                self.add_token(Content(node.text, safe=node.safe))

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
