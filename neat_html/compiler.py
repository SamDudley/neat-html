from collections import deque
from html import escape
from typing import TYPE_CHECKING, Any

from .tokens import ClosingTag, Content, OpeningTag, Token

if TYPE_CHECKING:
    from .types import HtmlAttributes


class Compiler:
    def compile(self, tokens: deque[Token]) -> str:
        self.tokens = tokens

        self.depth: int = 0
        self.token: Token | None = tokens.popleft()
        self.code: deque[str] = deque()

        while self.token:
            getattr(self, f"visit_{self.token.__class__.__name__}")(self.token)
            self.move_cursor(self.token, self.peek())
            self.eat()

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

    def visit_OpeningTag(self, tag: OpeningTag) -> None:
        attrs = self.render_attrs(tag.attrs)
        attrs = " " + attrs if attrs else ""
        self.append(f"<{tag.name}{attrs}>")

    def visit_Content(self, content: Content) -> None:
        text = escape(content.text) if not content.safe else content.text
        self.append(text)

    def visit_ClosingTag(self, tag: ClosingTag) -> None:
        self.append(f"</{tag.name}>")

    def move_cursor(self, token: Token, next_token: Token | None) -> None:
        if not next_token:
            return

        match (token, next_token):
            case [OpeningTag(is_self_closing=False), ClosingTag()]:
                self.depth = self.depth
            case [OpeningTag(is_self_closing=False), _]:
                self.depth += 1
            case [_, ClosingTag()]:
                self.depth -= 1

        match (token, next_token):
            # current or next token is an opening block tag
            case [OpeningTag(is_block=True), _] | [_, OpeningTag(is_block=True)]:
                self.newline()
                self.indent()
            # current or next token is a closing block tag
            case [ClosingTag(is_block=True), _] | [_, ClosingTag(is_block=True)]:
                self.newline()
                self.indent()

    @classmethod
    def render_attrs(cls, attrs: "HtmlAttributes") -> str:
        if not attrs:
            return ""
        attrs_list = [cls.render_attr(k, v) for k, v in attrs.items()]
        return " ".join(attrs_list)

    @classmethod
    def render_attr(cls, key: str, value: Any) -> str:
        if value == "":
            return key

        if value is True:
            return key

        if value is False:
            return ""

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
