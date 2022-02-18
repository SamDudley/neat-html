from .utils import is_self_closing_tag


class Node:
    def __init__(self, tag, attrs={}, children=[]):
        self.tag = tag
        self.attrs = attrs
        self.children = children

    @property
    def self_closing(self):
        return is_self_closing_tag(self.tag)

    def __repr__(self):
        return self.tag


class TextNode:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text
