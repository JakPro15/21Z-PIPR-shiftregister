import shiftregister
import pytest
from argparse import Namespace
from io import StringIO


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
    with pytest.raises(shiftregister.EmptyArgumentsListError):
        shiftregister.operation_on_list([], lambda a, b: a + b)
        raise AssertionError


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
        assert str(e) == "Attempted to perform the XOR operation on an empty "\
                         "list of arguments."


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
        assert str(e) == "Attempted to perform the AND operation on an empty "\
                         "list of arguments."


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
        assert str(e) == "Attempted to perform the OR operation on an empty "\
                         "list of arguments."


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
        assert str(e) == "Attempted to perform the OR operation on an empty "\
                         "list of arguments."


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
        assert str(e) == "Attempted to perform the AND operation on an empty "\
                         "list of arguments."


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


def test_convert_to_int_typical_1():
    assert str(shiftregister.convert_to_int([True, True, False])) == \
        '[1, 1, 0]'


def test_convert_to_int_typical_2():
    assert str(shiftregister.convert_to_int([0, 1, False, True])) == \
        '[0, 1, 0, 1]'


def test_convert_to_int_empty_list():
    assert str(shiftregister.convert_to_int([])) == \
        '[]'


def test_register_add_new_state_1():
    list = []
    function0 = shiftregister.Logic_Function('xor', [1, 2])
    function1 = shiftregister.Logic_Function('or', [0])
    function2 = shiftregister.Logic_Function('and', [1])

    register = shiftregister.Register([function0, function1, function2],
                                      [True, False, False])
    register.add_new_state(list)
    assert list == [[False, True, False]]


def test_register_add_new_state_2():
    list = []
    function0 = shiftregister.Logic_Function('nor', [1, 2, 3, 4])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [0, 1])
    function3 = shiftregister.Logic_Function('and', [2])
    function4 = shiftregister.Logic_Function('and', [3])

    register = shiftregister.Register([function0, function1, function2,
                                       function3, function4])
    register.add_new_state(list)
    register.add_new_state(list)
    register.add_new_state(list)
    assert list == [[True, False, False, False, False],
                    [True, True, False, False, False],
                    [False, True, True, False, False]]


def test_register_add_new_state_3():
    list = []
    function0 = shiftregister.Logic_Function('and', [3])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [1])
    function3 = shiftregister.Logic_Function('and', [2])

    register = shiftregister.Register([function0, function1,
                                       function2, function3],
                                      [True, False, True, False])
    register.add_new_state(list)
    register.add_new_state(list)
    assert list == [[False, True, False, True],
                    [True, False, True, False]]


def test_get_sequences_steps_1():
    function0 = shiftregister.Logic_Function('xor', [1, 2])
    function1 = shiftregister.Logic_Function('or', [0])
    function2 = shiftregister.Logic_Function('and', [1])

    register = shiftregister.Register([function0, function1, function2],
                                      [True, False, False])

    arguments = Namespace()
    arguments.steps = 5
    arguments.until_looped = False

    sequences = shiftregister.get_sequences(register, arguments)
    assert sequences == [
        [True, False, False],
        [False, True, False],
        [True, False, True],
        [True, True, False],
        [True, True, True],
        [False, True, True],
    ]


def test_get_sequences_2():
    function0 = shiftregister.Logic_Function('and', [3])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [1])
    function3 = shiftregister.Logic_Function('and', [2])

    register = shiftregister.Register([function0, function1,
                                       function2, function3],
                                      [True, False, False, False])

    arguments = Namespace()
    arguments.steps = 7
    arguments.until_looped = False

    sequences = shiftregister.get_sequences(register, arguments)
    assert sequences == [
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
    ]


def test_get_sequences_until_looped_1():
    function0 = shiftregister.Logic_Function('xor', [3, 4])
    function1 = shiftregister.Logic_Function('xor', [0, 4])
    function2 = shiftregister.Logic_Function('xor', [0, 1])
    function3 = shiftregister.Logic_Function('xor', [1, 2])
    function4 = shiftregister.Logic_Function('and', [0, 1, 2, 3])

    register = shiftregister.Register([function0, function1, function2,
                                       function3, function4],
                                      [True, False, False, False, False])

    arguments = Namespace()
    arguments.until_looped = True

    sequences = shiftregister.get_sequences(register, arguments)
    assert sequences == [
        [True, False, False, False, False],
        [False, True, True, False, False],
        [False, False, True, False, False],
        [False, False, False, True, False],
        [True, False, False, False, False],
    ]


def test_get_sequences_until_looped_2():
    function0 = shiftregister.Logic_Function('nor', [1, 2, 3, 4])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('and', [0, 1])
    function3 = shiftregister.Logic_Function('and', [2])
    function4 = shiftregister.Logic_Function('and', [3])

    register = shiftregister.Register([function0, function1, function2,
                                       function3, function4])

    arguments = Namespace()
    arguments.until_looped = True

    sequences = shiftregister.get_sequences(register, arguments)
    assert sequences == [
        [False, False, False, False, False],
        [True, False, False, False, False],
        [True, True, False, False, False],
        [False, True, True, False, False],
        [False, False, False, True, False],
        [False, False, False, False, True],
        [False, False, False, False, False]
    ]


def test_get_sequences_until_looped_no_return_to_beginning_1():
    function0 = shiftregister.Logic_Function('and', [1, 3])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('or', [1, 3])
    function3 = shiftregister.Logic_Function('and', [2])

    register = shiftregister.Register([function0, function1, function2,
                                       function3],
                                      [True, False, False, False])

    arguments = Namespace()
    arguments.until_looped = True

    sequences = shiftregister.get_sequences(register, arguments)
    assert sequences == [
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False],
    ]


def test_get_sequences_until_looped_no_return_to_beginning_2():
    function0 = shiftregister.Logic_Function('or', [1, 2])
    function1 = shiftregister.Logic_Function('and', [0])
    function2 = shiftregister.Logic_Function('nor', [0, 1])

    register = shiftregister.Register([function0, function1, function2],
                                      [False, True, True])

    arguments = Namespace()
    arguments.until_looped = True

    sequences = shiftregister.get_sequences(register, arguments)
    assert sequences == [
        [False, True, True],
        [True, False, False],
        [False, True, False],
        [True, False, False],
        [False, True, False],
        [True, False, False],
        [False, True, False],
        [True, False, False],
        [False, True, False]
    ]


def test_get_sequence_diversity_typical_1():
    assert shiftregister.get_sequence_diversity([True, True, False, True]) == 2


def test_get_sequence_diversity_typical_2():
    assert shiftregister.get_sequence_diversity([True, False, False]) == 1


def test_get_sequence_diversity_one_element():
    assert shiftregister.get_sequence_diversity([True]) == 0


def test_get_sequence_diversity_all_elements_the_same_1():
    assert shiftregister.get_sequence_diversity([False, False]) == 0


def test_get_sequence_diversity_all_elements_the_same_2():
    assert shiftregister.get_sequence_diversity([True, True, True,
                                                 True, True]) == 0


def test_get_sequence_diversity_max_diversity():
    assert shiftregister.get_sequence_diversity([True, False, True,
                                                 False, True, False]) == 5


def test_get_average_sequence_diversity_1():
    sequences = [
        [True, False, True, True],
        [True, False, False, True],
        [True, False, True, False],
        [False, True, False, True],
    ]
    assert shiftregister.get_average_sequence_diversity(sequences) == \
        pytest.approx(2.5)


def test_get_average_sequence_diversity_2():
    sequences = [
        [True, True, False, True],
        [True, False, False],
        [True],
        [False, False],
        [True, True, True, True, True],
        [True, False, True, False, True, False]
    ]
    assert shiftregister.get_average_sequence_diversity(sequences) == \
        pytest.approx(1.333, abs=1e-2)


def test_get_average_sequence_diversity_3():
    sequences = [
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True]
    ]
    assert shiftregister.get_average_sequence_diversity(sequences) == \
        pytest.approx(2)


def test_get_number_of_unique_sequences_all_the_same():
    sequences = [
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True]
    ]
    assert shiftregister.get_number_of_unique_sequences(sequences) == 1


def test_get_number_of_unique_sequences_all_different():
    sequences = [
        [True, False, True, True],
        [True, False, False, True],
        [True, False, True, False],
        [False, True, False, True],
    ]
    assert shiftregister.get_number_of_unique_sequences(sequences) == 4


def test_get_number_of_unique_sequences_mixed_1():
    sequences = [
        [True, False, True, True],
        [True, False, False, True],
        [True, False, True, False],
        [True, False, True, True],
        [False, True, False, True],
        [True, False, False, True],
        [True, True, True, True],
    ]
    assert shiftregister.get_number_of_unique_sequences(sequences) == 5


def test_get_number_of_unique_sequences_mixed_2():
    sequences = [
        [True, False],
        [True, False],
        [False, True],
        [True, False],
        [True, False],
        [False, True],
        [True, False],
        [True, True]
    ]
    assert shiftregister.get_number_of_unique_sequences(sequences) == 3


def test_get_space_usage_1():
    sequences = [
        [True, False],
        [True, False],
        [False, True],
        [True, False],
        [True, False],
        [False, True],
        [True, False],
        [True, True]
    ]
    assert shiftregister.get_space_usage(sequences) == pytest.approx(75)


def test_get_space_usage_2():
    sequences = [
        [True, False, True, True],
        [True, False, False, True],
        [True, False, True, False],
        [True, False, True, True],
        [False, True, False, True],
        [True, False, False, True],
        [True, True, True, True],
    ]
    assert shiftregister.get_space_usage(sequences) == pytest.approx(31.25)


def test_get_space_usage_3():
    sequences = [
        [False, False, False, False, False],
        [True, False, False, False, False],
        [True, True, False, False, False],
        [False, True, True, False, False],
        [False, False, False, True, False],
        [False, False, False, False, True],
        [False, False, False, False, False]
    ]
    assert shiftregister.get_space_usage(sequences) == pytest.approx(18.75)


def test_load_register_from_file_1():
    register_file = StringIO("""{
    "flip_flop_functions": [
        {
            "operation": "nand",
            "input_indexes": [2, 3]
        },
        {
            "operation": "or",
            "input_indexes": [0, 2, 3]
        },
        {
            "operation": "and",
            "input_indexes": [0, 1]
        },
        {
            "operation": "nor",
            "input_indexes": [0, 1, 2]
        }
    ],
    "starting_state": [1, 0, 0, 1]
}""")
    register = shiftregister.load_register_from_file(register_file)

    assert register.starting_state() == [True, False, False, True]
    assert register.state() == [True, False, False, True]

    functions = register.flip_flop_functions()
    assert functions[0].operation()([True, True]) is False
    assert functions[0].operation()([True, False]) is True
    assert functions[0].operation()([False, False]) is True
    assert functions[0].input_indexes() == [2, 3]

    assert functions[1].operation()([True, True]) is True
    assert functions[1].operation()([True, False]) is True
    assert functions[1].operation()([False, False]) is False
    assert functions[1].input_indexes() == [0, 2, 3]

    assert functions[2].operation()([True, True]) is True
    assert functions[2].operation()([True, False]) is False
    assert functions[2].operation()([False, False]) is False
    assert functions[2].input_indexes() == [0, 1]

    assert functions[3].operation()([True, True]) is False
    assert functions[3].operation()([True, False]) is False
    assert functions[3].operation()([False, False]) is True
    assert functions[3].input_indexes() == [0, 1, 2]


def test_load_register_from_file_2():
    register_file = StringIO("""{
    "flip_flop_functions": [
        {
            "operation": "xor",
            "input_indexes": [1, 2]
        },
        {
            "operation": "or",
            "input_indexes": [0]
        },
        {
            "operation": "and",
            "input_indexes": [1]
        }
    ],
    "starting_state": [0, 1, 1]
}""")
    register = shiftregister.load_register_from_file(register_file)

    assert register.starting_state() == [False, True, True]
    assert register.state() == [False, True, True]

    functions = register.flip_flop_functions()
    assert functions[0].operation()([True, True]) is False
    assert functions[0].operation()([True, False]) is True
    assert functions[0].operation()([False, False]) is False
    assert functions[0].input_indexes() == [1, 2]

    assert functions[1].operation()([True, True]) is True
    assert functions[1].operation()([True, False]) is True
    assert functions[1].operation()([False, False]) is False
    assert functions[1].input_indexes() == [0]

    assert functions[2].operation()([True, True]) is True
    assert functions[2].operation()([True, False]) is False
    assert functions[2].operation()([False, False]) is False
    assert functions[2].input_indexes() == [1]


def test_load_register_from_file_3():
    register_file = StringIO("""{
    "flip_flop_functions": [
        {
            "operation": "nand",
            "input_indexes": [1, 2]
        },
        {
            "operation": "nor",
            "input_indexes": [0, 2]
        },
        {
            "operation": "xor",
            "input_indexes": [0, 1]
        }
    ],
    "starting_state": [0, 0, 0]
}""")
    register = shiftregister.load_register_from_file(register_file)

    assert register.starting_state() == [False, False, False]
    assert register.state() == [False, False, False]

    functions = register.flip_flop_functions()
    assert functions[0].operation()([True, True]) is False
    assert functions[0].operation()([True, False]) is True
    assert functions[0].operation()([False, False]) is True
    assert functions[0].input_indexes() == [1, 2]

    assert functions[1].operation()([True, True]) is False
    assert functions[1].operation()([True, False]) is False
    assert functions[1].operation()([False, False]) is True
    assert functions[1].input_indexes() == [0, 2]

    assert functions[2].operation()([True, True]) is False
    assert functions[2].operation()([True, False]) is True
    assert functions[2].operation()([False, False]) is False
    assert functions[2].input_indexes() == [0, 1]


def test_save_data_to_file_1():
    output_file = StringIO()

    sequences = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]
    ]
    space_usage = 35.25
    average_sequence_diversity = 1.155

    shiftregister.save_data_to_file(output_file, sequences, space_usage,
                                    average_sequence_diversity)

    assert output_file.getvalue() == """{
    "sequences": [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]
    ],
    "space_usage": 35.25,
    "average_sequence_diversity": 1.155
}"""


def test_save_data_to_file_2():
    output_file = StringIO()

    sequences = [
        [1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 1]
    ]
    space_usage = 0.2435
    average_sequence_diversity = 5

    shiftregister.save_data_to_file(output_file, sequences, space_usage,
                                    average_sequence_diversity)

    assert output_file.getvalue() == """{
    "sequences": [
        [1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 1]
    ],
    "space_usage": 0.2435,
    "average_sequence_diversity": 5
}"""


def test_save_data_to_file_3():
    output_file = StringIO()

    sequences = [
        [1, 0],
        [1, 1],
        [0, 0],
        [0, 1]
    ]
    space_usage = 12
    average_sequence_diversity = 1.1111

    shiftregister.save_data_to_file(output_file, sequences, space_usage,
                                    average_sequence_diversity)

    assert output_file.getvalue() == """{
    "sequences": [
        [1, 0],
        [1, 1],
        [0, 0],
        [0, 1]
    ],
    "space_usage": 12,
    "average_sequence_diversity": 1.1111
}"""


def test_get_results_string_1():
    sequences = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]
    ]
    space_usage = 18.75
    average_sequence_diversity = 1.1667

    assert shiftregister.get_results_string(sequences, space_usage,
                                            average_sequence_diversity) == \
        """The following sequences have been generated:
[1, 0, 0, 1]
[1, 1, 0, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
Space usage for this register is 18.75%
Average sequence diversity of the generated sequences is 1.1667
"""


def test_get_results_string_2():
    sequences = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]
    ]
    space_usage = 35.25
    average_sequence_diversity = 1.155

    assert shiftregister.get_results_string(sequences, space_usage,
                                            average_sequence_diversity) == \
        """The following sequences have been generated:
[1, 0, 0, 1]
[1, 1, 0, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
[1, 1, 1, 0]
Space usage for this register is 35.25%
Average sequence diversity of the generated sequences is 1.155
"""


def test_get_results_string_3():
    sequences = [
        [1, 0],
        [1, 1],
        [0, 0],
        [0, 1]
    ]
    space_usage = 12
    average_sequence_diversity = 1.1111

    assert shiftregister.get_results_string(sequences, space_usage,
                                            average_sequence_diversity) == \
        """The following sequences have been generated:
[1, 0]
[1, 1]
[0, 0]
[0, 1]
Space usage for this register is 12%
Average sequence diversity of the generated sequences is 1.1111
"""
