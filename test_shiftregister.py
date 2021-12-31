import shiftregister
import pytest


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
    assert shiftregister.bool_operation_str_to_function('xor') == \
        shiftregister.logic_xor


def test_bool_operation_str_to_function_and():
    assert shiftregister.bool_operation_str_to_function('and') == \
        shiftregister.logic_and


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
    assert shiftregister.bool_operation_str_to_function('or') == \
        shiftregister.logic_or


def test_bool_operation_str_to_function_nand_2_arguments():
    logic_nand = shiftregister.bool_operation_str_to_function('nand')
    assert logic_nand([False, False]) is True
    assert logic_nand([False, True]) is True
    assert logic_nand([True, False]) is True
    assert logic_nand([True, True]) is False


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
        shiftregister.bool_operation_str_to_function('u')
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


def test_logic_function_constructor_setters_getters():
    indexes_list = [2, 4, 5]
    logic_function = shiftregister.Logic_Function('xor', indexes_list)
    assert logic_function.operation() == shiftregister.logic_xor
    assert logic_function.input_indexes() == [2, 4, 5]

    indexes_list.remove(5)
    assert logic_function.input_indexes() == [2, 4, 5]
    logic_function.input_indexes().remove(5)
    assert logic_function.input_indexes() == [2, 4, 5]

    logic_function.set_operation('nand')
    logic_function.set_input_indexes(indexes_list)

    logic_nand = logic_function.operation()
    assert logic_nand([False]) is True
    assert logic_nand([False, True]) is True
    assert logic_nand([True, False, False]) is True
    assert logic_nand([True, True, True, True, True]) is False
    assert logic_function.input_indexes() == [2, 4]


def test_logic_function_calculate_1():
    logic_function = shiftregister.Logic_Function('xor', [2, 4, 5])
    assert logic_function.calculate([True, False, True,
                                     False, True, False]) is False
    logic_function.set_input_indexes([0, 1])
    assert logic_function.calculate([True, False]) is True
    assert logic_function.calculate([False, False]) is False
    logic_function.set_input_indexes([4])
    assert logic_function.calculate([True, False, True,
                                     False, True, False]) is True
    with pytest.raises(IndexError):
        logic_function.calculate([True, False, True])


def test_logic_function_calculate_2():
    logic_function = shiftregister.Logic_Function('nand', [2, 4, 5])
    assert logic_function.calculate([True, False, True,
                                     False, True, False]) is True
    logic_function.set_input_indexes([0, 1])
    assert logic_function.calculate([True, True]) is False
    assert logic_function.calculate([False, True]) is True
    logic_function.set_input_indexes([4])
    assert logic_function.calculate([True, False, True,
                                     False, True, False]) is False
    with pytest.raises(IndexError):
        logic_function.calculate([True, False, True])


def test_register_constructor_setters_getters_1():
    function0 = shiftregister.Logic_Function('xor', [1, 2])
    function1 = shiftregister.Logic_Function('or', [0, 2])
    function2 = shiftregister.Logic_Function('and', [1])
    functions = [function0, function1, function2]
    register = shiftregister.Register(functions)
    assert register.flip_flop_functions() == functions
    assert register.starting_state() == [False, False, False]
    assert register.state() == [False, False, False]

    register.set_state([False, True, True])
    assert register.starting_state() == [False, False, False]
    assert register.state() == [False, True, True]

    register.set_starting_state([True, True, True])
    assert register.starting_state() == [True, True, True]
    assert register.state() == [False, True, True]

    register.set_flip_flop_functions([function2])
    assert len(register.flip_flop_functions()) == 1
    assert register.flip_flop_functions()[0] == function2
    assert register.starting_state() == [False]
    assert register.state() == [False]

    try:
        register.set_starting_state([True, True, True])
        raise AssertionError
    except shiftregister.InvalidStateError as e:
        assert str(e) == "Attempted to set the starting state of a register "\
                         "to a list of a different length than the flip-flop "\
                         "functions list of the register"

    try:
        register.set_state([True, False])
        raise AssertionError
    except shiftregister.InvalidStateError as e:
        assert str(e) == "Attempted to set the state of a register to a list "\
                         "of a different length than the flip-flop functions "\
                         "list of the register"


def test_register_constructor_setters_getters_2():
    function0 = shiftregister.Logic_Function('xor', [1, 2])
    function1 = shiftregister.Logic_Function('or', [0, 2])
    function2 = shiftregister.Logic_Function('and', [1])
    functions = [function0, function1, function2]
    state = [True, False, True]
    register = shiftregister.Register(functions, state)
    assert register.flip_flop_functions() == [function0, function1, function2]
    assert register.starting_state() == [True, False, True]
    assert register.state() == [True, False, True]

    functions.remove(function1)
    assert register.flip_flop_functions() == [function0, function1, function2]
    register.flip_flop_functions().remove(function1)
    assert register.flip_flop_functions() == [function0, function1, function2]

    state.pop(1)
    assert register.starting_state() == [True, False, True]
    assert register.state() == [True, False, True]

    register.starting_state().pop(1)
    register.state().pop(1)
    assert register.starting_state() == [True, False, True]
    assert register.state() == [True, False, True]

    register.set_flip_flop_functions(functions)
    register.set_starting_state([True, False])
    register.set_state(state)
    assert register.flip_flop_functions() == [function0, function2]
    assert register.starting_state() == [True, False]
    assert register.state() == [True, True]


def test_register_advance_1():
    function0 = shiftregister.Logic_Function('xor', [1, 2])
    function1 = shiftregister.Logic_Function('or', [0])
    function2 = shiftregister.Logic_Function('and', [1])

    register = shiftregister.Register([function0, function1, function2],
                                      [True, False, False])
    assert register.state() == [True, False, False]

    register.advance()
    assert register.state() == [False, True, False]

    register.advance()
    assert register.state() == [True, False, True]

    register.advance()
    assert register.state() == [True, True, False]

    register.advance()
    assert register.state() == [True, True, True]

    register.advance()
    assert register.state() == [False, True, True]

    register.advance()
    assert register.state() == [False, False, True]

    register.advance()
    assert register.state() == [True, False, False]


def test_register_advance_2():
    function0 = shiftregister.Logic_Function('nand', [2, 3])
    function1 = shiftregister.Logic_Function('or', [0, 2, 3])
    function2 = shiftregister.Logic_Function('and', [0, 1])
    function3 = shiftregister.Logic_Function('nor', [0, 1, 2])
    register = shiftregister.Register([function0, function1,
                                       function2, function3])
    assert register.state() == [False, False, False, False]

    register.advance()
    assert register.state() == [True, False, False, True]

    register.advance()
    assert register.state() == [True, True, False, False]

    register.advance()
    assert register.state() == [True, True, True, False]

    register.advance()
    assert register.state() == [True, True, True, False]


def test_register_advance_3():
    function0 = shiftregister.Logic_Function('nor', [1, 2, 3, 4])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [0, 1])
    function3 = shiftregister.Logic_Function('and', [2])
    function4 = shiftregister.Logic_Function('and', [3])

    register = shiftregister.Register([function0, function1, function2,
                                       function3, function4])
    assert register.state() == [False, False, False, False, False]

    register.advance()
    assert register.state() == [True, False, False, False, False]

    register.advance()
    assert register.state() == [True, True, False, False, False]

    register.advance()
    assert register.state() == [False, True, True, False, False]

    register.advance()
    assert register.state() == [False, False, False, True, False]

    register.advance()
    assert register.state() == [False, False, False, False, True]

    register.advance()
    assert register.state() == [False, False, False, False, False]


def test_register_looped_1():
    function0 = shiftregister.Logic_Function('and', [3])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [1])
    function3 = shiftregister.Logic_Function('and', [2])

    register = shiftregister.Register([function0, function1,
                                       function2, function3],
                                      [True, False, True, False])

    assert register.looped()
    register.advance()
    assert not register.looped()
    register.advance()
    assert register.looped()


def test_register_looped_2():
    function0 = shiftregister.Logic_Function('nor', [1, 2, 3, 4])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [0, 1])
    function3 = shiftregister.Logic_Function('and', [2])
    function4 = shiftregister.Logic_Function('and', [3])

    register = shiftregister.Register([function0, function1, function2,
                                       function3, function4])
    assert register.looped()
    register.set_state([True, True, False, True, False])
    assert not register.looped()
    register.set_state([True, False, False, False, False])
    assert not register.looped()
    register.set_state([True, True, True, True, True])
    assert not register.looped()
    register.set_state([False, False, False, False, False])
    assert register.looped()


def test_register_looped_3():
    function0 = shiftregister.Logic_Function('xor', [1, 2])
    function1 = shiftregister.Logic_Function('or', [0])
    function2 = shiftregister.Logic_Function('and', [1])

    register = shiftregister.Register([function0, function1, function2],
                                      [True, False, False])
    assert register.looped()

    register.set_starting_state([False, True, True])
    assert not register.looped()
    register.set_state([False, True, False])
    assert not register.looped()
    register.set_starting_state([False, True, False])
    assert register.looped()
