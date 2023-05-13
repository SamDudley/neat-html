from .types import HtmlAttributes


class Token:
    pass


# TODO: good use case for dataclasses?
class OpeningTag(Token):
    def __init__(self, name: str, attrs: HtmlAttributes):
        self.name = name
        self.attrs = attrs

    def __repr__(self) -> str:
        return f"OpeningTag({self.name!r}, {self.attrs!r})"


class Content(Token):
    def __init__(self, text: str):
        self.text = text

    def __repr__(self) -> str:
        return f"Content({self.text!r})"


class ClosingTag(Token):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"ClosingTag({self.name!r})"
