# neat-html

A python library for writing and composing HTML.

Features:

- small API to learn (2 functions)
- fully typed API
- produces "neatly" formatted HTML
- written in pure python
- zero dependencies
- comprehensive test suite
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
