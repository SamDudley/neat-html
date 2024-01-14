from collections.abc import Sequence

from neat_html import Element, h, render


def page(content: Element | Sequence[Element]) -> Element:
    return h(
        "html",
        {"lang": "en"},
        [
            h(
                "head",
                [
                    h("meta", {"charset": "UTF-8"}),
                    h(
                        "meta",
                        {
                            "name": "viewport",
                            "content": "width=device-width, initial-scale=1.0",
                        },
                    ),
                    h("meta", {"http-equiv": "X-UA-Compatible", "content": "ie=edge"}),
                    h("title", ["Document"]),
                ],
            ),
            h("body", [h("main", content)]),
        ],
    )


def form(*fields: str) -> Element:
    inputs = [
        h(
            "div",
            field(
                name,
                f"id_{name}",
                name.replace("_", " ").capitalize(),
                "text",
            ),
        )
        for name in fields
    ]

    return h("form", [*inputs, h("button", "Submit")])


def field(name: str, id: str, label: str, type: str) -> list[Element]:
    return [
        h("label", {"for": id}, label),
        h("input", {"name": name, "type": type, id: "id"}),
    ]


html = page([form("first_name", "last_name"), form("age", "hair_color")])


print(render(html))
