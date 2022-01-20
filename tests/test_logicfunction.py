from ..programfiles import exceptions
from ..programfiles import logicfunction
import pytest


def test_operation_on_list_addition():
    assert logicfunction.operation_on_list([1, 2, -4],
                                           lambda a, b: a + b) == -1


def test_operation_on_list_multiplication():
    assert logicfunction.operation_on_list((1, 2, -4),
                                           lambda a, b: a * b) == -8


def test_operation_on_list_boolean_implication():
    assert logicfunction.operation_on_list([True, True, False, True],
                                           lambda p, q: (not p) or q) is True


def test_operation_on_list_empty_list():
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logicfunction.operation_on_list([], lambda a, b: a + b)


def test_logic_xor_2_arguments():
    assert logicfunction.logic_xor((False, False)) is False
    assert logicfunction.logic_xor((False, True)) is True
    assert logicfunction.logic_xor((True, False)) is True
    assert logicfunction.logic_xor((True, True)) is False


def test_logic_xor_more_arguments():
    assert logicfunction.logic_xor((False, False, False)) is False
    assert logicfunction.logic_xor((False, True, True, False)) is False
    assert logicfunction.logic_xor((True, False, False)) is True
    assert logicfunction.logic_xor((True, True, True, True, True)) is False


def test_logic_xor_one_argument():
    assert logicfunction.logic_xor((False,)) is False
    assert logicfunction.logic_xor((True,)) is True


def test_logic_xor_no_arguments():
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logicfunction.logic_xor(())


def test_logic_and_2_arguments():
    assert logicfunction.logic_and((False, False)) is False
    assert logicfunction.logic_and((False, True)) is False
    assert logicfunction.logic_and((True, False)) is False
    assert logicfunction.logic_and((True, True)) is True


def test_logic_and_more_arguments():
    assert logicfunction.logic_and((False, False, False)) is False
    assert logicfunction.logic_and((False, True, True, False)) is False
    assert logicfunction.logic_and((True, False, False)) is False
    assert logicfunction.logic_and((True, True, True, True, True)) is True


def test_logic_and_one_argument():
    assert logicfunction.logic_and((False,)) is False
    assert logicfunction.logic_and((True,)) is True


def test_logic_and_no_arguments():
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logicfunction.logic_and(())


def test_logic_or_2_arguments():
    assert logicfunction.logic_or((False, False)) is False
    assert logicfunction.logic_or((False, True)) is True
    assert logicfunction.logic_or((True, False)) is True
    assert logicfunction.logic_or((True, True)) is True


def test_logic_or_more_arguments():
    assert logicfunction.logic_or((False, False, False)) is False
    assert logicfunction.logic_or((False, True, True, False)) is True
    assert logicfunction.logic_or((True, False, False)) is True
    assert logicfunction.logic_or((True, True, True, True, True)) is True


def test_logic_or_one_argument():
    assert logicfunction.logic_or((False,)) is False
    assert logicfunction.logic_or((True,)) is True


def test_logic_or_no_arguments():
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logicfunction.logic_or(())


def test_logic_not_more_arguments():
    with pytest.raises(exceptions.TooManyArgumentsError):
        logicfunction.logic_not((False, False, False)) is False
    with pytest.raises(exceptions.TooManyArgumentsError):
        logicfunction.logic_not((False, True, True, False)) is True
    with pytest.raises(exceptions.TooManyArgumentsError):
        logicfunction.logic_not((True, False)) is True


def test_logic_not_one_argument():
    assert logicfunction.logic_not((False,)) is True
    assert logicfunction.logic_not((True,)) is False


def test_logic_not_no_arguments():
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logicfunction.logic_not(())


def test_bool_operation_str_to_function_xor():
    assert logicfunction.bool_operation_str_to_function('xor') == \
        logicfunction.logic_xor


def test_bool_operation_str_to_function_and():
    assert logicfunction.bool_operation_str_to_function('and') == \
        logicfunction.logic_and


def test_bool_operation_str_to_function_nor_2_arguments():
    logic_nor = logicfunction.bool_operation_str_to_function('nor')
    assert logic_nor((False, False)) is True
    assert logic_nor((False, True)) is False
    assert logic_nor((True, False)) is False
    assert logic_nor((True, True)) is False


def test_bool_operation_str_to_function_nor_more_arguments():
    logic_nor = logicfunction.bool_operation_str_to_function('nor')
    assert logic_nor((False, False, False)) is True
    assert logic_nor((False, True, True, False)) is False
    assert logic_nor((True, False, False)) is False
    assert logic_nor((True, True, True, True, True)) is False


def test_bool_operation_str_to_function_nor_one_argument():
    logic_nor = logicfunction.bool_operation_str_to_function('nor')
    assert logic_nor((False,)) is True
    assert logic_nor((True,)) is False


def test_bool_operation_str_to_function_nor_no_arguments():
    logic_nor = logicfunction.bool_operation_str_to_function('nor')
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logic_nor(())


def test_bool_operation_str_to_function_or():
    assert logicfunction.bool_operation_str_to_function('or') == \
        logicfunction.logic_or


def test_bool_operation_str_to_function_nand_2_arguments():
    logic_nand = logicfunction.bool_operation_str_to_function('nand')
    assert logic_nand((False, False)) is True
    assert logic_nand((False, True)) is True
    assert logic_nand((True, False)) is True
    assert logic_nand((True, True)) is False


def test_bool_operation_str_to_function_nand_more_arguments():
    logic_nand = logicfunction.bool_operation_str_to_function('nand')
    assert logic_nand((False, False, False)) is True
    assert logic_nand((False, True, True, False)) is True
    assert logic_nand((True, False, False)) is True
    assert logic_nand((True, True, True, True, True)) is False


def test_bool_operation_str_to_function_nand_one_argument():
    logic_nand = logicfunction.bool_operation_str_to_function('nand')
    assert logic_nand((False,)) is True
    assert logic_nand((True,)) is False


def test_bool_operation_str_to_function_nand_no_arguments():
    logic_nand = logicfunction.bool_operation_str_to_function('nand')
    with pytest.raises(exceptions.EmptyArgumentsListError):
        logic_nand(())


def test_bool_operation_str_to_function_not():
    assert logicfunction.bool_operation_str_to_function('not') == \
        logicfunction.logic_not


def test_bool_operation_str_to_function_invalid_input_1():
    with pytest.raises(exceptions.WrongOperationStringError):
        logicfunction.bool_operation_str_to_function('u')


def test_bool_operation_str_to_function_invalid_input_2():
    with pytest.raises(exceptions.WrongOperationStringError):
        logicfunction.bool_operation_str_to_function('xor ')


def test_logic_function_constructor_setters_getters():
    indexes_list = [2, 4, 5]
    logic_function = logicfunction.Logic_Function('xor', indexes_list)
    assert logic_function.operation() == logicfunction.logic_xor
    assert logic_function.input_indexes() == [2, 4, 5]

    indexes_list.remove(5)
    assert logic_function.input_indexes() == [2, 4, 5]
    logic_function.input_indexes().remove(5)
    assert logic_function.input_indexes() == [2, 4, 5]

    logic_function.set_operation('nand')
    logic_function.set_input_indexes(indexes_list)

    logic_nand = logic_function.operation()
    assert logic_nand((False,)) is True
    assert logic_nand((False, True)) is True
    assert logic_nand((True, False, False)) is True
    assert logic_nand((True, True, True, True, True)) is False
    assert logic_function.input_indexes() == [2, 4]


def test_logic_function_calculate_1():
    logic_function = logicfunction.Logic_Function('xor', [2, 4, 5])
    assert logic_function.calculate((True, False, True,
                                     False, True, False)) is False
    logic_function.set_input_indexes([0, 1])
    assert logic_function.calculate((True, False)) is True
    assert logic_function.calculate((False, False)) is False
    logic_function.set_input_indexes([4])
    assert logic_function.calculate((True, False, True,
                                     False, True, False)) is True
    with pytest.raises(exceptions.InvalidFlipFlopIndexError):
        logic_function.calculate((True, False, True))


def test_logic_function_calculate_2():
    logic_function = logicfunction.Logic_Function('nand', [2, 4, 5])
    assert logic_function.calculate((True, False, True,
                                     False, True, False)) is True
    logic_function.set_input_indexes([0, 1])
    assert logic_function.calculate((True, True)) is False
    assert logic_function.calculate((False, True)) is True
    logic_function.set_input_indexes([4])
    assert logic_function.calculate((True, False, True,
                                     False, True, False)) is False
    with pytest.raises(exceptions.InvalidFlipFlopIndexError):
        logic_function.calculate((True, False, True))


def test_logic_function_calculate_invalid_index():
    logic_function = logicfunction.Logic_Function('nand', [2, 0, 2.3])
    with pytest.raises(exceptions.InvalidFlipFlopIndexError):
        logic_function.calculate((True, False, True, False))
