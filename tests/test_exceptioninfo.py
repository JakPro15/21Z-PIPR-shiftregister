from programfiles.resultsfunctions import get_sequences
from ..programfiles import exceptioninfo
from ..programfiles import iofunctions
from io import StringIO
from argparse import Namespace


def test_nonexistent_file():
    try:
        with open('drg', 'r') as file_handle:
            iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, '') == \
            'main.py: error: the given source file does not exist'


def test_invalid_json_file():
    file_handle = StringIO('rsgv')
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'a') == \
            'main.py: error: a is not a valid JSON file'


def test_json_file_not_containing_proper_elements():
    file_handle = StringIO('{"starting_state": [1, 0, 1]}')
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'a') == \
            'main.py: error: a must contain both '\
            '"flip_flop_functions" list and "starting_state" list. Each '\
            'element of the flip-flop functions list must contain both '\
            '"operation" string and "input_indexes" list.'


def test_wrong_operation_string():
    file = """{
    "flip_flop_functions": [
        {
            "operation": "ad",
            "input_indexes": [1]
        },
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": [0, 0]
}"""
    file = StringIO(file)
    try:
        iofunctions.load_register_from_file(file)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'a') == \
            'main.py: error: (in a) ad is not a valid Boolean operation'


def test_wrong_starting_state_1():
    file = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": [1]
        },
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": [0, 0, 0]
}"""
    file = StringIO(file)
    try:
        iofunctions.load_register_from_file(file)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'a') == \
            'main.py: error: (in a) the starting state of a register must be '\
            'valid for this register - its number of elements must be the '\
            'same as the amount of flip-flops in the register'


def test_wrong_starting_state_2():
    file_handle = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": [1]
        },
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": [0, "0"]
}"""
    file_handle = StringIO(file_handle)
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'a') == \
            'main.py: error: (in a) the starting state '\
            'of the register must only contain integers 0 and 1, in order '\
            'to represent valid states of the flip-flops'


def test_input_indexes_not_a_list():
    file_handle = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": 1
        },
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": [0, 0]
}"""
    file_handle = StringIO(file_handle)
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'a') == \
            'main.py: error: (in a) input indexes data '\
            'for a flip-flop should be given as a list'


def test_flip_flop_functions_list_not_a_list():
    file_handle = """{
    "flip_flop_functions": 2,
    "starting_state": [0, 0]
}"""
    file_handle = StringIO(file_handle)
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'b') == \
            'main.py: error: (in b) '\
            '"flip_flop_functions" and "starting_state" should be lists, '\
            'elements of "flip_flop_functions" list should be dictionaries'


def test_starting_state_not_a_list():
    file_handle = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": [1]
        },
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": 2
}"""
    file_handle = StringIO(file_handle)
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'b') == \
            'main.py: error: (in b) '\
            '"flip_flop_functions" and "starting_state" should be lists, '\
            'elements of "flip_flop_functions" list should be dictionaries'


def test_flip_flop_function_not_a_dict():
    file_handle = """{
    "flip_flop_functions": [
        ["and", [1]],
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": [0, 0]
}"""
    file_handle = StringIO(file_handle)
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'b') == \
            'main.py: error: (in b) '\
            '"flip_flop_functions" and "starting_state" should be lists, '\
            'elements of "flip_flop_functions" list should be dictionaries'


def test_empty_register():
    file_handle = """{
    "flip_flop_functions": [],
    "starting_state": []
}"""
    file_handle = StringIO(file_handle)
    try:
        iofunctions.load_register_from_file(file_handle)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'b') == \
            'main.py: error: (in b) the register must '\
            'contain at least one flip-flop - flip_flop_functions list '\
            'cannot be empty'


def test_empty_input_indexes_list():
    file_handle = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": []
        },
        {
            "operation": "or",
            "input_indexes": [0]
        }
    ],
    "starting_state": [0, 0]
}"""
    file_handle = StringIO(file_handle)

    register = iofunctions.load_register_from_file(file_handle)
    arguments = Namespace()
    arguments.until_looped = True
    try:
        get_sequences(register, arguments)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'abc') == \
            'main.py: error: (in abc) a flip-flop function'\
            ' must take at least one argument - its input_indexes list '\
            'cannot be empty'


def test_input_indexes_list_too_large():
    file_handle = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": [1]
        },
        {
            "operation": "not",
            "input_indexes": [0, 1]
        }
    ],
    "starting_state": [0, 0]
}"""
    file_handle = StringIO(file_handle)

    register = iofunctions.load_register_from_file(file_handle)
    arguments = Namespace()
    arguments.until_looped = True
    try:
        get_sequences(register, arguments)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'abc') == \
            'main.py: error: (in abc) the NOT operation '\
            'cannot take more than 1 argument - input_indexes list of a '\
            'flip-flop function with operation NOT must contain only one '\
            'index'


def test_input_index_not_valid():
    file_handle = """{
    "flip_flop_functions": [
        {
            "operation": "and",
            "input_indexes": [1]
        },
        {
            "operation": "not",
            "input_indexes": [0.1]
        }
    ],
    "starting_state": [0, 0]
}"""
    file_handle = StringIO(file_handle)

    register = iofunctions.load_register_from_file(file_handle)
    arguments = Namespace()
    arguments.until_looped = True
    try:
        get_sequences(register, arguments)
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'abc') == \
            'main.py: error: (in abc) one of the given flip-flop indexes does'\
            ' not represent a valid flip-flop index'


def test_unknown_exception():
    try:
        raise AssertionError
    except Exception as exception:
        assert exceptioninfo.get_exception_info(exception, 'abc') == \
            'main.py: error: an unknown error has occurred'
