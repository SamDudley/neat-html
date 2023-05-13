from .constants import block_tags, inline_tags, self_closing_tags


def is_self_closing_tag(tag: str) -> bool:
    return tag in self_closing_tags


def is_block_tag(tag: str) -> bool:
    return tag in block_tags


def is_inline_tag(tag: str) -> bool:
    return tag in inline_tags
