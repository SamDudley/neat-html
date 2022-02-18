from collections import deque

from .utils import (
    is_block_tag, is_inline_tag, is_self_closing_tag, prettyprint
)


class Compiler:
    def compile(self, tokens, format=True):
        self.tokens = tokens
        self.format = format

        self.depth = 0
        self.stack = deque()
        self.token = tokens.popleft()
        self.code = deque()

        while self.token:
            getattr(self, f'visit_{self.token.__class__.__name__}')(self.token)
            self.eat()

        if self.code[0] == '\n':
            self.code.popleft()

        if self.code[-1] != '\n':
            self.newline()

        return ''.join(self.code)

    def eat(self):
        try:
            self.token = self.tokens.popleft()
        except IndexError:
            self.token = None

    def peek(self):
        try:
            return self.tokens[0]
        except IndexError:
            return None

    def append(self, fragment):
        self.code.append(fragment)

    @prettyprint
    def indent(self):
        self.append('    ' * self.depth)

    @prettyprint
    def newline(self):
        self.append('\n')

    def in_block(self):
        try:
            return is_block_tag(self.stack[-1])
        except IndexError:
            return False

    def in_inline(self):
        try:
            return is_inline_tag(self.stack[-1])
        except IndexError:
            return False

    def visit_OpeningTag(self, tag):
        if self.in_block():
            self.newline()
            self.indent()

        self.append(f'<{tag.name}{self.render_attrs(tag.attrs)}>')
        self.stack.append(tag.name)

        if is_block_tag(tag.name) and not is_self_closing_tag(tag.name):
            self.depth += 1

    def visit_Content(self, content):
        if self.in_block():
            self.newline()
            self.indent()

        self.append(content.text)

    def visit_ClosingTag(self, tag):
        if is_block_tag(tag.name):
            self.depth -= 1
            self.newline()
            self.indent()

        self.append(f'</{tag.name}>')
        self.stack.pop()

    @classmethod
    def render_attrs(cls, attrs):
        if not attrs:
            return ''
        attrs_list = [cls.render_attr(k, v) for k, v in attrs.items()]
        return ' ' + ' '.join(attrs_list)

    @classmethod
    def render_attr(cls, key, value):
        if key == 'style':
            return f'{key}="{cls.render_style(value)}"'
        # Default
        return f'{key}="{value}"'

    @classmethod
    def render_style(cls, style):
        if not style:
            return ''
        style_list = [f'{k}: {v}' for k, v in style.items()]
        return '; '.join(style_list)
