import pytest

from neat_html import _handle_args
from neat_html.node import Node


class TestHandleArgs:
    def test_0_args(self) -> None:
        with pytest.raises(ValueError):
            _handle_args()

    def test_1_arg_str(self) -> None:
        assert _handle_args("div") == ("div", {}, [])

    def test_2_args_str_and_dict(self) -> None:
        assert _handle_args("div", {"a": 1}) == ("div", {"a": 1}, [])

    def test_2_args_str_and_list(self) -> None:
        assert _handle_args("div", ["hello"]) == ("div", {}, ["hello"])

    def test_2_args_str_and_str(self) -> None:
        assert _handle_args("div", "hello") == ("div", {}, ["hello"])

    def test_2_args_str_and_node(self) -> None:
        node = Node("div")
        assert _handle_args("div", node) == ("div", {}, [node])

    def test_3_args_str_dict_list(self) -> None:
        args = _handle_args("div", {"a": 1}, ["hello"])
        assert args == ("div", {"a": 1}, ["hello"])

    def test_3_args_str_dict_str(self) -> None:
        args = _handle_args("div", {"a": 1}, "hello")
        assert args == ("div", {"a": 1}, ["hello"])

    def test_3_args_str_dict_node(self) -> None:
        node = Node("div")
        args = _handle_args("div", {"a": 1}, node)
        assert args == ("div", {"a": 1}, [node])

    def test_4_args(self) -> None:
        with pytest.raises(ValueError):
            _handle_args("div", {}, [], [])
