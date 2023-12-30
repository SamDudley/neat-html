from .constants import block_tags, self_closing_tags


def is_self_closing_tag(tag: str) -> bool:
    return tag in self_closing_tags


def is_block_tag(tag: str) -> bool:
    return tag in block_tags
