from collections import deque
from .node import Node, TextNode
from .tokens import OpeningTag, Content, ClosingTag


class Tokenizer:
    def __init__(self):
        self.nodes = None
        self.tokens = None

    def tokenize(self, root_node):
        self.nodes = deque()
        self.tokens = deque()

        self.nodes.append(self.wrap_node(root_node))

        while self.nodes:
            node = self.nodes[-1]

            if isinstance(node, TextNode):
                self.nodes.pop()
                self.add_token(Content(node.text))

            else:  # Node
                if not node.opened:
                    if node.self_closing:
                        # We don't want to come back and process this node again.
                        self.nodes.pop()

                    self.add_children(node.children)
                    self.add_token(OpeningTag(node.tag, node.attrs))

                else:  # Closing
                    self.nodes.pop()
                    self.add_token(ClosingTag(node.tag))

                node.opened = True

        return self.tokens

    def add_children(self, children):
        self.nodes.extend(
            reversed([self.wrap_node(child) for child in children])
        )

    def add_token(self, token):
        self.tokens.append(token)

    def wrap_node(self, node):
        if isinstance(node, Node):
            return NodeWrapper(node)
        return node


class NodeWrapper:
    def __init__(self, node):
        self._node = node
        self.opened = False

    def __getattr__(self, name):
        return getattr(self._node, name)
