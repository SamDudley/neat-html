# TODO: good use case for dataclasses?
class OpeningTag:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return (type(other) is self.__class__
                and other.name == self.name
                and other.attrs == self.attrs)

    def __repr__(self):
        return f'OpeningTag({self.name}, {self.attrs})'


class Content:
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return (type(other) is self.__class__
                and other.text == self.text)

    def __repr__(self):
        return self.text


class ClosingTag:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return (type(other) is self.__class__
                and other.name == self.name)

    def __repr__(self):
        return f'ClosingTag({self.name})'
