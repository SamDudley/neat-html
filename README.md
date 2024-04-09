# neat-html

A python library for writing and composing HTML.

Features:

- small API to learn
- fully typed API (strict mypy)
- produces "neatly" formatted HTML
- written in pure python
- zero dependencies
- comprehensive test suite (100% coverage)
- no recursion

## Example

Code:

```python
from neat_html import h, render

greeting = h("strong", {"style": {"color": "green"}}, "Hello")
html = h("p", {"id": "foo"}, [greeting, ", World!"])
print(render(html))
```

Output:

```html
<p id="foo"><strong style="color: green">Hello</strong>, World!</p>
```

## Installation

Using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install neat-html
```

Using [poetry](https://python-poetry.org/):

```bash
poetry add neat-html
```

Using [uv](https://github.com/astral-sh/uv):

```bash
uv pip install neat-html
```

## User guide

### Basics

```python
from neat_html import Element, h, render

# define an element
button: Element = h("button", "Submit")
# render the element to html
html: str = render(button)
```

## Integrations

### Django

#### django-neat-html

https://github.com/SamDudley/django-neat-html

A work in progress library that integrates neat-html into Django as a template backend.

## API

I would recommend taking a look at the source code for the details of the API.

The best place to start would be in [neat_html/\_\_init\_\_.py](neat_html/__init__.py).
