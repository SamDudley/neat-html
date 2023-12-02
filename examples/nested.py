from python_html_dsl import h, render


root = h("span", "root")

element = root

for i in range(2_000):
    child = h("span", str(i))
    element.children.append(child)
    element = child

print(render(root))
