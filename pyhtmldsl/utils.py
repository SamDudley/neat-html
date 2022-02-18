from .constants import self_closing_tags, block_tags, inline_tags


def is_self_closing_tag(tag):
    return tag in self_closing_tags


def is_block_tag(tag):
    return tag in block_tags


def is_inline_tag(tag):
    return tag in inline_tags


def handle_3_args(*args):
    if len(args) == 0:
        raise ValueError('Not enough arguments')
    if len(args) > 3:
        raise ValueError('Too many arguments')

    if len(args) == 1:
        tag = args[0]
        attrs = {}
        children = []
    elif len(args) == 2:
        tag = args[0]
        if isinstance(args[1], dict):
            attrs = args[1]
            children = []
        elif isinstance(args[1], list):
            attrs = {}
            children = args[1]
        elif isinstance(args[1], str):
            attrs = {}
            children = [args[1]]
        else:
            raise ValueError('Invalid second argument')
    elif len(args) == 3:
        tag = args[0]
        attrs = args[1]
        children = handle_children_arg(args[2])

    return tag, attrs, children


def handle_2_args(*args):
    if len(args) > 2:
        raise ValueError('Too many arguments')

    if len(args) == 0:
        attrs = {}
        children = []
    elif len(args) == 1:
        if isinstance(args[0], dict):
            attrs = args[0]
            children = []
        elif isinstance(args[0], list):
            attrs = {}
            children = args[0]
        elif isinstance(args[0], str):
            attrs = {}
            children = [args[0]]
        else:
            raise ValueError('Invalid single argument')
    elif len(args) == 2:
        attrs = args[0]
        children = handle_children_arg(args[1])

    return attrs, children


def handle_children_arg(children):
    if isinstance(children, str):
        return [children]
    # TODO: check if list or tuple or set?
    return children


def prettyprint(func):
    def decorator(self, *args, **kwargs):
        if self.format:
            return func(self, *args, **kwargs)
    return decorator
