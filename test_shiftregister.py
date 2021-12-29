import shiftregister


def test_logic_xor():
    assert shiftregister.logic_xor(False, False) is False
    assert shiftregister.logic_xor(False, True) is True
    assert shiftregister.logic_xor(True, False) is True
    assert shiftregister.logic_xor(True, True) is False


def test_logic_and():
    assert shiftregister.logic_and(False, False) is False
    assert shiftregister.logic_and(False, True) is False
    assert shiftregister.logic_and(True, False) is False
    assert shiftregister.logic_and(True, True) is True


def test_logic_or():
    assert shiftregister.logic_or(False, False) is False
    assert shiftregister.logic_or(False, True) is True
    assert shiftregister.logic_or(True, False) is True
    assert shiftregister.logic_or(True, True) is True


def test_bool_operation_str_to_function_xor():
    operation, negated = shiftregister.bool_operation_str_to_function('xor')
    assert operation == shiftregister.logic_xor
    assert negated is False


def test_bool_operation_str_to_function_and():
    operation, negated = shiftregister.bool_operation_str_to_function('and')
    assert operation == shiftregister.logic_and
    assert negated is False


def test_bool_operation_str_to_function_nor():
    operation, negated = shiftregister.bool_operation_str_to_function('nor')
    assert operation == shiftregister.logic_or
    assert negated is True


def test_bool_operation_str_to_function_or():
    operation, negated = shiftregister.bool_operation_str_to_function('or')
    assert operation == shiftregister.logic_or
    assert negated is False


def test_bool_operation_str_to_function_nand():
    operation, negated = shiftregister.bool_operation_str_to_function('nand')
    assert operation == shiftregister.logic_and
    assert negated is True


def test_bool_operation_str_to_function_invalid_input_1():
    try:
        shiftregister.bool_operation_str_to_function('x')
        raise AssertionError
    except shiftregister.WrongOperatorStringError as e:
        assert str(e) == "Attempted to convert an invalid string to a "\
                         "Boolean operator function"


def test_bool_operation_str_to_function_invalid_input_2():
    try:
        shiftregister.bool_operation_str_to_function('xor ')
        raise AssertionError
    except shiftregister.WrongOperatorStringError as e:
        assert str(e) == "Attempted to convert an invalid string to a "\
                         "Boolean operator function"
