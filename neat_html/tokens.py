from .types import HtmlAttributes
from .utils import is_block_tag, is_self_closing_tag


class Token:
    pass


# TODO: good use case for dataclasses?
class OpeningTag(Token):
    def __init__(self, name: str, attrs: HtmlAttributes):
        self.name = name
        self.attrs = attrs

    @property
    def is_block(self) -> bool:
        return is_block_tag(self.name)

    @property
    def is_self_closing(self) -> bool:
        return is_self_closing_tag(self.name)

    def __repr__(self) -> str:
        return f"OpeningTag({self.name!r}, {self.attrs!r})"


class Content(Token):
    def __init__(self, text: str, *, safe: bool = False):
        self.text = text
        self.safe = safe

    def __repr__(self) -> str:
        return f"Content({self.text!r}, {self.safe!r})"


class ClosingTag(Token):
    def __init__(self, name: str):
        self.name = name

    @property
    def is_block(self) -> bool:
        return is_block_tag(self.name)

    def __repr__(self) -> str:
        return f"ClosingTag({self.name!r})"
