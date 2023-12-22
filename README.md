# python-html-dsl

python-html-dsl is a python library for writing and composing HTML.

Features:

- small API to learn (2 functions)
- fully typed API
- produces formatted HTML
- writting in pure python
- zero dependencies
- comprehensive test suite

Install using pip:

```bash
pip install python-html-dsl
```

Take it for a spin:

```python
>>> from python_html_dsl import h, render
>>> greeting = h("strong", {"style", {"color": "green"}}, "Hello")
>>> html = h("p", {"id": "foo"}, [greeting, ", World!"])
>>> print(render(html))
<p id="foo">
    <strong style="color: green;">Hello</strong> World!
</p>
```
