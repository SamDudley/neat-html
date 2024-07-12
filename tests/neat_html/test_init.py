import pytest

from neat_html import _handle_args
from neat_html.types import Element


class TestHandleArgs:
    def test_0_args(self) -> None:
        with pytest.raises(TypeError):
            _handle_args()  # type: ignore

    def test_1_arg_str(self) -> None:
        assert _handle_args("div") == ("div", {}, [])

    def test_2_args_str_and_dict(self) -> None:
        assert _handle_args("div", {"a": 1}) == ("div", {"a": 1}, [])

    def test_2_args_str_and_list(self) -> None:
        assert _handle_args("div", ["hello"]) == ("div", {}, ["hello"])

    def test_2_args_str_and_str(self) -> None:
        assert _handle_args("div", "hello") == ("div", {}, ["hello"])

    def test_2_args_str_and_element(self) -> None:
        element = Element("div")
        assert _handle_args("div", element) == ("div", {}, [element])

    def test_3_args_str_dict_list(self) -> None:
        args = _handle_args("div", {"a": 1}, ["hello"])
        assert args == ("div", {"a": 1}, ["hello"])

    def test_3_args_str_dict_str(self) -> None:
        args = _handle_args("div", {"a": 1}, "hello")
        assert args == ("div", {"a": 1}, ["hello"])

    def test_3_args_str_dict_element(self) -> None:
        element = Element("div")
        args = _handle_args("div", {"a": 1}, element)
        assert args == ("div", {"a": 1}, [element])

    def test_4_args(self) -> None:
        with pytest.raises(TypeError):
            _handle_args("div", {}, [], [])  # type: ignore
