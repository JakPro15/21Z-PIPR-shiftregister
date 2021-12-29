import shiftregister


def test_operation_on_list_addition():
    assert shiftregister.operation_on_list([1, 2, -4],
                                           lambda a, b: a + b) == -1


def test_operation_on_list_multiplication():
    assert shiftregister.operation_on_list([1, 2, -4],
                                           lambda a, b: a * b) == -8


def test_operation_on_list_boolean_implication():
    assert shiftregister.operation_on_list([True, True, False, True],
                                           lambda p, q: (not p) or q) is True


def test_operation_on_list_empty_list():
    try:
        shiftregister.operation_on_list([], lambda a, b: a + b)
        raise AssertionError
    except shiftregister.EmptyArgumentsListError as e:
        assert str(e) == "Attempted to perform an operation on an empty list "\
                         "of arguments."


def test_logic_xor_2_arguments():
    assert shiftregister.logic_xor([False, False]) is False
    assert shiftregister.logic_xor([False, True]) is True
    assert shiftregister.logic_xor([True, False]) is True
    assert shiftregister.logic_xor([True, True]) is False


def test_logic_xor_more_arguments():
    assert shiftregister.logic_xor([False, False, False]) is False
    assert shiftregister.logic_xor([False, True, True, False]) is False
    assert shiftregister.logic_xor([True, False, False]) is True
    assert shiftregister.logic_xor([True, True, True, True, True]) is False


def test_logic_xor_one_argument():
    assert shiftregister.logic_xor([False]) is False
    assert shiftregister.logic_xor([True]) is True


def test_logic_xor_no_arguments():
    try:
        shiftregister.logic_xor([])
        raise AssertionError
    except shiftregister.EmptyArgumentsListError as e:
        assert str(e) == "Attempted to perform an operation on an empty list "\
                         "of arguments."


def test_logic_and_2_arguments():
    assert shiftregister.logic_and([False, False]) is False
    assert shiftregister.logic_and([False, True]) is False
    assert shiftregister.logic_and([True, False]) is False
    assert shiftregister.logic_and([True, True]) is True


def test_logic_and_more_arguments():
    assert shiftregister.logic_and([False, False, False]) is False
    assert shiftregister.logic_and([False, True, True, False]) is False
    assert shiftregister.logic_and([True, False, False]) is False
    assert shiftregister.logic_and([True, True, True, True, True]) is True


def test_logic_and_one_argument():
    assert shiftregister.logic_and([False]) is False
    assert shiftregister.logic_and([True]) is True


def test_logic_and_no_arguments():
    try:
        shiftregister.logic_and([])
        raise AssertionError
    except shiftregister.EmptyArgumentsListError as e:
        assert str(e) == "Attempted to perform an operation on an empty list "\
                         "of arguments."


def test_logic_or_2_arguments():
    assert shiftregister.logic_or([False, False]) is False
    assert shiftregister.logic_or([False, True]) is True
    assert shiftregister.logic_or([True, False]) is True
    assert shiftregister.logic_or([True, True]) is True


def test_logic_or_more_arguments():
    assert shiftregister.logic_or([False, False, False]) is False
    assert shiftregister.logic_or([False, True, True, False]) is True
    assert shiftregister.logic_or([True, False, False]) is True
    assert shiftregister.logic_or([True, True, True, True, True]) is True


def test_logic_or_one_argument():
    assert shiftregister.logic_or([False]) is False
    assert shiftregister.logic_or([True]) is True


def test_logic_or_no_arguments():
    try:
        shiftregister.logic_or([])
        raise AssertionError
    except shiftregister.EmptyArgumentsListError as e:
        assert str(e) == "Attempted to perform an operation on an empty list "\
                         "of arguments."


def test_bool_operation_str_to_function_xor():
    operation = shiftregister.bool_operation_str_to_function('xor')
    assert operation == shiftregister.logic_xor


def test_bool_operation_str_to_function_and():
    operation = shiftregister.bool_operation_str_to_function('and')
    assert operation == shiftregister.logic_and


def test_bool_operation_str_to_function_nor_2_arguments():
    logic_nor = shiftregister.bool_operation_str_to_function('nor')
    assert logic_nor([False, False]) is True
    assert logic_nor([False, True]) is False
    assert logic_nor([True, False]) is False
    assert logic_nor([True, True]) is False


def test_bool_operation_str_to_function_nor_more_arguments():
    logic_nor = shiftregister.bool_operation_str_to_function('nor')
    assert logic_nor([False, False, False]) is True
    assert logic_nor([False, True, True, False]) is False
    assert logic_nor([True, False, False]) is False
    assert logic_nor([True, True, True, True, True]) is False


def test_bool_operation_str_to_function_nor_one_argument():
    logic_nor = shiftregister.bool_operation_str_to_function('nor')
    assert logic_nor([False]) is True
    assert logic_nor([True]) is False


def test_bool_operation_str_to_function_nor_no_arguments():
    logic_nor = shiftregister.bool_operation_str_to_function('nor')
    try:
        logic_nor([])
        raise AssertionError
    except shiftregister.EmptyArgumentsListError as e:
        assert str(e) == "Attempted to perform an operation on an empty list "\
                         "of arguments."


def test_bool_operation_str_to_function_or():
    operation = shiftregister.bool_operation_str_to_function('or')
    assert operation == shiftregister.logic_or


def test_bool_operation_str_to_function_nand_2_arguments():
    operation = shiftregister.bool_operation_str_to_function('nand')
    assert operation([False, False]) is True
    assert operation([False, True]) is True
    assert operation([True, False]) is True
    assert operation([True, True]) is False


def test_bool_operation_str_to_function_nand_more_arguments():
    logic_nand = shiftregister.bool_operation_str_to_function('nand')
    assert logic_nand([False, False, False]) is True
    assert logic_nand([False, True, True, False]) is True
    assert logic_nand([True, False, False]) is True
    assert logic_nand([True, True, True, True, True]) is False


def test_bool_operation_str_to_function_nand_one_argument():
    logic_nand = shiftregister.bool_operation_str_to_function('nand')
    assert logic_nand([False]) is True
    assert logic_nand([True]) is False


def test_bool_operation_str_to_function_nand_no_arguments():
    logic_nand = shiftregister.bool_operation_str_to_function('nand')
    try:
        logic_nand([])
        raise AssertionError
    except shiftregister.EmptyArgumentsListError as e:
        assert str(e) == "Attempted to perform an operation on an empty list "\
                         "of arguments."


def test_bool_operation_str_to_function_invalid_input_1():
    try:
        shiftregister.bool_operation_str_to_function('x')
        raise AssertionError
    except shiftregister.WrongOperationStringError as e:
        assert str(e) == "Attempted to convert an invalid string to a "\
                         "Boolean operator function"


def test_bool_operation_str_to_function_invalid_input_2():
    try:
        shiftregister.bool_operation_str_to_function('xor ')
        raise AssertionError
    except shiftregister.WrongOperationStringError as e:
        assert str(e) == "Attempted to convert an invalid string to a "\
                         "Boolean operator function"
