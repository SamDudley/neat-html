from textwrap import dedent

import pytest

from neat_html import h, render, safe


def test_single_tag() -> None:
    html = render(h("div", {}, []))
    assert html == "<div>\n</div>\n"


def test_self_closing_tag() -> None:
    html = render(h("input", {}, []))
    assert html == "<input>\n"


def test_nested_tags() -> None:
    html = render(h("div", {}, [h("p", {}, [])]))
    assert html == "<div>\n    <p>\n    </p>\n</div>\n"


def test_one_attr() -> None:
    html = render(h("div", {"class": "wrapper-div"}, []))
    assert html == '<div class="wrapper-div">\n</div>\n'


def test_multiple_attrs() -> None:
    html = render(h("input", {"class": "text-input", "type": "text"}, []))
    assert html == '<input class="text-input" type="text">\n'


def test_single_style_attr() -> None:
    html = render(h("div", {"style": {"background-color": "red"}}, []))
    assert html == '<div style="background-color: red">\n</div>\n'


def test_multiple_style_attrs() -> None:
    html = render(
        h("div", {"style": {"background-color": "red", "color": "white"}}, [])
    )
    assert html == '<div style="background-color: red; color: white">\n</div>\n'


def test_style_not_dict() -> None:
    with pytest.raises(ValueError, match="A style value must be a dict"):
        render(h("div", {"style": "color: red;"}))


def test_style_empty_dict() -> None:
    html = render(h("div", {"style": {}}))
    assert html == '<div style="">\n</div>\n'


def test_unsafe_text() -> None:
    html = render(h("div", safe("<script>alert(1)</script>")))
    assert html == dedent(
        """\
        <div>
            <script>alert(1)</script>
        </div>
        """
    )


def test_safe_text() -> None:
    html = render(h("div", "<script>alert(1)</script>"))
    assert html == dedent(
        """\
        <div>
            &lt;script&gt;alert(1)&lt;/script&gt;
        </div>
        """
    )


def test_empty_string_boolean_attribute() -> None:
    html = render(h("input", {"disabled": ""}))
    assert html == "<input disabled>\n"


def test_can_produce_doctype_tag() -> None:
    html = render(h("!DOCTYPE", {"html": ""}))
    assert html == "<!DOCTYPE html>\n"


class TestFormatting:
    def test_block(self) -> None:
        html = render(h("div", ["hello"]))
        assert html == dedent(
            """\
            <div>
                hello
            </div>
            """
        )

    def test_inline(self) -> None:
        html = render(h("span", ["hello"]))
        assert html == "<span>hello</span>\n"

    def test_nested_block_block(self) -> None:
        html = render(h("div", [h("div", ["hello"])]))
        assert html == dedent(
            """\
            <div>
                <div>
                    hello
                </div>
            </div>
            """
        )

    def test_nested_inline_inline(self) -> None:
        html = render(h("span", [h("span", ["hello"])]))
        assert html == "<span><span>hello</span></span>\n"

    def test_nested_block_inline(self) -> None:
        html = render(h("div", [h("span", ["hello"])]))
        assert html == dedent(
            """\
            <div>
                <span>hello</span>
            </div>
            """
        )

    def test_nested_inline_block(self) -> None:
        html = render(h("span", [h("div", ["hello"])]))
        assert html == dedent(
            """\
            <span>
                <div>
                    hello
                </div>
            </span>
            """
        )

    def test_flat_div_div(self) -> None:
        html = render(
            h(
                "div",
                [
                    h("div", ["hello"]),
                    h("div", ["hello"]),
                ],
            )
        )
        assert html == dedent(
            """\
            <div>
                <div>
                    hello
                </div>
                <div>
                    hello
                </div>
            </div>
            """
        )

    def test_nested_inline_flat_div(self) -> None:
        html = render(
            h(
                "div",
                [
                    h("div", [h("span")]),
                    h("div"),
                ],
            )
        )
        assert html == dedent(
            """\
            <div>
                <div>
                    <span></span>
                </div>
                <div>
                </div>
            </div>
            """
        )

    def test_block_inline_inline(self) -> None:
        html = h("div", [h("span", "foo"), h("span", "bar")])
        assert render(html) == dedent(
            """\
            <div>
                <span>foo</span><span>bar</span>
            </div>
            """
        )

    def test_block_inline_text(self) -> None:
        html = h("div", [h("span", "foo"), "bar"])
        assert render(html) == dedent(
            """\
            <div>
                <span>foo</span>bar
            </div>
            """
        )

    def test_block_following_content(self) -> None:
        html = h("div", ["hello", h("div", "world")])
        assert render(html) == dedent(
            """\
            <div>
                hello
                <div>
                    world
                </div>
            </div>
            """
        )
