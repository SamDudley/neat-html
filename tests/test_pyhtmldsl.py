from textwrap import dedent

from pyhtmldsl import h


def test_single_tag():
    html = h('div', {}, []).html()
    assert html == '<div>\n</div>\n'


def test_self_closing_tag():
    html = h('input', {}, []).html()
    assert html == '<input>\n'


def test_nested_tags():
    html = h('div', {}, [h('p', {}, [])]).html()
    assert html == '<div>\n    <p>\n    </p>\n</div>\n'


def test_one_attr():
    html = h('div', {'class': 'wrapper-div'}, []).html()
    assert html == '<div class="wrapper-div">\n</div>\n'


def test_multiple_attrs():
    html = h('input', {'class': 'text-input', 'type': 'text'}, []).html()
    assert html == '<input class="text-input" type="text">\n'


def test_single_style_attr():
    html = h('div', {'style': {'background-color': 'red'}}, []).html()
    assert html == '<div style="background-color: red">\n</div>\n'


def test_multiple_style_attrs():
    html = h(
        'div',
        {'style': {'background-color': 'red', 'color': 'white'}},
        []
    ).html()
    assert html == '<div style="background-color: red; color: white">\n</div>\n'


class TestFormatting:
    def test_block(self):
        html = h('div', ['hello']).html()
        assert html == dedent("""\
            <div>
                hello
            </div>
        """)

    def test_inline(self):
        html = h('span', ['hello']).html()
        assert html == '<span>hello</span>\n'

    def test_nested_block_block(self):
        html = h('div', [h('div', ['hello'])]).html()
        assert html == dedent("""\
            <div>
                <div>
                    hello
                </div>
            </div>
        """)

    def test_nested_inline_inline(self):
        html = h('span', [h('span', ['hello'])]).html()
        assert html == '<span><span>hello</span></span>\n'

    def test_nested_block_inline(self):
        html = h('div', [h('span', ['hello'])]).html()
        assert html == dedent("""\
            <div>
                <span>hello</span>
            </div>
        """)

    def test_nested_inline_block(self):
        html = h('span', [h('div', ['hello'])]).html()
        assert html == dedent("""\
            <span><div>
                hello
            </div></span>
        """)

    def test_flat_div_div(self):
        html = h('div', [
            h('div', ['hello']),
            h('div', ['hello']),
        ]).html()
        assert html == dedent("""\
            <div>
                <div>
                    hello
                </div>
                <div>
                    hello
                </div>
            </div>
        """)

    def test_nested_inline_flat_div(self):
        html = h('div', [
            h('div', [h('span')]),
            h('div'),
        ]).html()
        assert html == dedent("""\
            <div>
                <div>
                    <span></span>
                </div>
                <div>
                </div>
            </div>
        """)
