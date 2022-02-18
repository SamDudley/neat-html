import pytest
from pyhtmldsl.utils import handle_3_args, handle_2_args


class TestHandle3Args:
    def test_0_args(self):
        with pytest.raises(ValueError):
            handle_3_args()

    def test_1_arg_str(self):
        assert handle_3_args('div') == ('div', {}, [])

    def test_2_args_str_and_dict(self):
        assert handle_3_args('div', {'a': 1}) == ('div', {'a': 1}, [])

    def test_2_args_str_and_list(self):
        assert handle_3_args('div', ['hello']) == ('div', {}, ['hello'])

    def test_2_args_str_and_str(self):
        assert handle_3_args('div', 'hello') == ('div', {}, ['hello'])

    def test_3_args_str_dict_list(self):
        args = handle_3_args('div', {'a': 1}, ['hello'])
        assert args == ('div', {'a': 1}, ['hello'])

    def test_3_args_str_dict_str(self):
        args = handle_3_args('div', {'a': 1}, 'hello')
        assert args == ('div', {'a': 1}, ['hello'])

    def test_4_args(self):
        with pytest.raises(ValueError):
            handle_3_args('div', {}, [], [])


class TestHandle2Args:
    def test_0_args(self):
        assert handle_2_args() == ({}, [])

    def test_1_arg_dict(self):
        assert handle_2_args({'a': 1}) == ({'a': 1}, [])

    def test_1_arg_list(self):
        assert handle_2_args(['hello']) == ({}, ['hello'])

    def test_1_arg_str(self):
        assert handle_2_args('hello') == ({}, ['hello'])

    def test_2_args_dict_list(self):
        assert handle_2_args({'a': 1}, ['hello']) == ({'a': 1}, ['hello'])

    def test_2_args_dict_str(self):
        assert handle_2_args({'a': 1}, 'hello') == ({'a': 1}, ['hello'])

    def test_3_args(self):
        with pytest.raises(ValueError):
            handle_2_args({}, [], [])
