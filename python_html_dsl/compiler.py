from collections import deque
from typing import TYPE_CHECKING, Any

from .tokens import ClosingTag, Content, OpeningTag, Token
from .utils import is_block_tag, is_inline_tag, is_self_closing_tag

if TYPE_CHECKING:
    from .types import HtmlAttributes


class Compiler:
    def compile(self, tokens: deque[Token]) -> str:
        self.tokens = tokens

        self.depth: int = 0
        self.stack: deque[str] = deque()
        self.token: Token | None = tokens.popleft()
        self.code: deque[str] = deque()

        while self.token:
            getattr(self, f"visit_{self.token.__class__.__name__}")(self.token)
            self.eat()

        if self.code[0] == "\n":
            self.code.popleft()

        if self.code[-1] != "\n":
            self.newline()

        return "".join(self.code)

    def eat(self) -> None:
        try:
            self.token = self.tokens.popleft()
        except IndexError:
            self.token = None

    def peek(self) -> Token | None:
        try:
            return self.tokens[0]
        except IndexError:
            return None

    def append(self, fragment: str) -> None:
        self.code.append(fragment)

    def indent(self) -> None:
        self.append("    " * self.depth)

    def newline(self) -> None:
        self.append("\n")

    def in_block(self) -> bool:
        try:
            return is_block_tag(self.stack[-1])
        except IndexError:
            return False

    def in_inline(self) -> bool:
        try:
            return is_inline_tag(self.stack[-1])
        except IndexError:
            return False

    def visit_OpeningTag(self, tag: OpeningTag) -> None:
        if self.in_block():
            self.newline()
            self.indent()

        self.append(f"<{tag.name}{self.render_attrs(tag.attrs)}>")
        self.stack.append(tag.name)

        if is_block_tag(tag.name) and not is_self_closing_tag(tag.name):
            self.depth += 1

    def visit_Content(self, content: Content) -> None:
        if self.in_block():
            self.newline()
            self.indent()

        self.append(content.text)

    def visit_ClosingTag(self, tag: ClosingTag) -> None:
        if is_block_tag(tag.name):
            self.depth -= 1
            self.newline()
            self.indent()

        self.append(f"</{tag.name}>")
        self.stack.pop()

    @classmethod
    def render_attrs(cls, attrs: "HtmlAttributes") -> str:
        if not attrs:
            return ""
        attrs_list = [cls.render_attr(k, v) for k, v in attrs.items()]
        return " " + " ".join(attrs_list)

    @classmethod
    def render_attr(cls, key: str, value: Any) -> str:
        if key == "style":
            if not isinstance(value, dict):
                raise ValueError("A style value must be a dict")

            return f'{key}="{cls.render_style(value)}"'
        # Default
        return f'{key}="{value}"'

    @classmethod
    def render_style(cls, style: dict[str, str]) -> str:
        if not style:
            return ""
        style_list = [f"{k}: {v}" for k, v in style.items()]
        return "; ".join(style_list)
