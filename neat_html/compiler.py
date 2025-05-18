from collections import deque
from html import escape as html_escape
from typing import TYPE_CHECKING, TypedDict, Unpack

from .tokens import ClosingTag, Content, OpeningTag, Token
from .types import SafeString

if TYPE_CHECKING:
    from .types import HtmlAttributes


class CompilerOptions(TypedDict):
    escape_attributes: bool


class Compiler:
    def __init__(self, **options: Unpack[CompilerOptions]) -> None:
        self.options = options

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
        string = self.escape(content.string)
        self.append(string)

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

    def render_attrs(self, attrs: "HtmlAttributes") -> str:
        if not attrs:
            return ""
        attrs_list = [self.render_attr(k, v) for k, v in attrs.items()]
        return " ".join(attrs_list)

    def render_attr(self, key: str, value: object) -> str:
        if value == "":
            return key

        if value is True:
            return key

        if value is False:
            return ""

        if key == "style":
            if not isinstance(value, dict):
                raise ValueError("A style value must be a dict")

            return f'{key}="{self.render_style(value)}"'

        # Default
        return f'{key}="{self.render_attr_value(value)}"'

    def render_style(self, style: dict[str, str]) -> str:
        if not style:
            return ""
        style_list = [f"{k}: {self.render_attr_value(v)}" for k, v in style.items()]
        return "; ".join(style_list)

    def render_attr_value(self, value: object) -> str:
        if self.options["escape_attributes"] is False:
            return str(value)

        if not isinstance(value, (str, SafeString)):
            value = str(value)

        return self.escape(value)

    @staticmethod
    def escape(string: str) -> str:
        return string if isinstance(string, SafeString) else html_escape(string)
