# neat-html

A python library for writing and composing HTML.

Features:

- small API to learn (2 functions)
- fully typed API (strict mypy)
- produces "neatly" formatted HTML
- written in pure python
- zero dependencies
- comprehensive test suite (100% coverage)
- no recursion

Install using pip:

```bash
pip install neat-html
```

Take it for a spin:

```python
>>> from neat_html import h, render
>>> greeting = h("strong", {"style": {"color": "green"}}, "Hello")
>>> html = h("p", {"id": "foo"}, [greeting, ", World!"])
>>> print(render(html))
<p id="foo">
    <strong style="color: green">Hello</strong>, World!
</p>

```

## API

### `h(...) -> Element`

`h` is an overloaded function with the following signitures:

```python
def h(tag): ...
def h(tag, attrs): ...
def h(tag, children): ...
def h(tag, attrs, children): ...
```

As you can see `h` supports 4 signitures with 3 different parameters.

Let's take a closer look at the parameters `h` takes:

#### tag

```python
# should be a `str`
h("div")

# can be a standard tag
h("div")

# or anything you want (useful for web components)
h("my-web-component")
```

#### attrs

```python
# should be a `dict`, the key should be a `str`

# the value can be a `str`
h("p", {"class": "my-class"})

# or a `bool` (for boolean attributes)
h("input", {"required": True})

# or any value which can be converted to a `str`
h("input", {"tabindex": 1})

# or in the case of "style", a `dict[str, Any]`
h("p": {"style": {"color": "red"}})
```

#### children

```python
# `children` can be...

# an `Element` (usually constructed with `h`)
h("ul", h("li"))

# or a `str`
h("h1", "My heading")

# or `Iterable` of either
h("div", ["Some text", h("button")])
```

### `render(element: Element) -> str`

`render` takes in an `Element` and compiles it to a HTML `str`.

```python
render(h("span", "Hello, World!"))  # <span>Hello, World!</span>
```
