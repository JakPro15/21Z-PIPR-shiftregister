from ..programfiles import logicfunction
from ..programfiles import register


def test_register_constructor_setters_getters_1():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0, 2])
    function2 = logicfunction.Logic_Function('and', [1])
    functions = [function0, function1, function2]
    register1 = register.Register(functions)
    assert register1.flip_flop_functions() == functions
    assert register1.starting_state() == [False, False, False]
    assert register1.state() == [False, False, False]

    register1.set_state([False, True, True])
    assert register1.starting_state() == [False, False, False]
    assert register1.state() == [False, True, True]

    register1.set_starting_state([True, True, True])
    assert register1.starting_state() == [True, True, True]
    assert register1.state() == [False, True, True]

    register1.set_flip_flop_functions([function2])
    assert len(register1.flip_flop_functions()) == 1
    assert register1.flip_flop_functions()[0] == function2
    assert register1.starting_state() == [False]
    assert register1.state() == [False]

    try:
        register1.set_starting_state([True, True, True])
        raise AssertionError
    except register.InvalidStateError as e:
        assert str(e) == "Attempted to set the starting state of a register "\
                         "to a list of a different length than the flip-flop "\
                         "functions list of the register"

    try:
        register1.set_state([True, False])
        raise AssertionError
    except register.InvalidStateError as e:
        assert str(e) == "Attempted to set the state of a register to a list "\
                         "of a different length than the flip-flop functions "\
                         "list of the register"


def test_register_constructor_setters_getters_2():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0, 2])
    function2 = logicfunction.Logic_Function('and', [1])
    functions = [function0, function1, function2]
    state = [True, False, True]
    register1 = register.Register(functions, state)
    assert register1.flip_flop_functions() == [function0, function1, function2]
    assert register1.starting_state() == [True, False, True]
    assert register1.state() == [True, False, True]

    functions.remove(function1)
    assert register1.flip_flop_functions() == [function0, function1, function2]
    register1.flip_flop_functions().remove(function1)
    assert register1.flip_flop_functions() == [function0, function1, function2]

    state.pop(1)
    assert register1.starting_state() == [True, False, True]
    assert register1.state() == [True, False, True]

    register1.starting_state().pop(1)
    register1.state().pop(1)
    assert register1.starting_state() == [True, False, True]
    assert register1.state() == [True, False, True]

    register1.set_flip_flop_functions(functions)
    register1.set_starting_state([True, False])
    register1.set_state(state)
    assert register1.flip_flop_functions() == [function0, function2]
    assert register1.starting_state() == [True, False]
    assert register1.state() == [True, True]


def test_register_advance_1():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])
    assert register1.state() == [True, False, False]

    register1.advance()
    assert register1.state() == [False, True, False]

    register1.advance()
    assert register1.state() == [True, False, True]

    register1.advance()
    assert register1.state() == [True, True, False]

    register1.advance()
    assert register1.state() == [True, True, True]

    register1.advance()
    assert register1.state() == [False, True, True]

    register1.advance()
    assert register1.state() == [False, False, True]

    register1.advance()
    assert register1.state() == [True, False, False]


def test_register_advance_2():
    function0 = logicfunction.Logic_Function('nand', [2, 3])
    function1 = logicfunction.Logic_Function('or', [0, 2, 3])
    function2 = logicfunction.Logic_Function('and', [0, 1])
    function3 = logicfunction.Logic_Function('nor', [0, 1, 2])
    register1 = register.Register([function0, function1,
                                   function2, function3])
    assert register1.state() == [False, False, False, False]

    register1.advance()
    assert register1.state() == [True, False, False, True]

    register1.advance()
    assert register1.state() == [True, True, False, False]

    register1.advance()
    assert register1.state() == [True, True, True, False]

    register1.advance()
    assert register1.state() == [True, True, True, False]


def test_register_advance_3():
    function0 = logicfunction.Logic_Function('nor', [1, 2, 3, 4])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [0, 1])
    function3 = logicfunction.Logic_Function('and', [2])
    function4 = logicfunction.Logic_Function('and', [3])

    register1 = register.Register([function0, function1, function2,
                                   function3, function4])
    assert register1.state() == [False, False, False, False, False]

    register1.advance()
    assert register1.state() == [True, False, False, False, False]

    register1.advance()
    assert register1.state() == [True, True, False, False, False]

    register1.advance()
    assert register1.state() == [False, True, True, False, False]

    register1.advance()
    assert register1.state() == [False, False, False, True, False]

    register1.advance()
    assert register1.state() == [False, False, False, False, True]

    register1.advance()
    assert register1.state() == [False, False, False, False, False]


def test_register_looped_1():
    function0 = logicfunction.Logic_Function('and', [3])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [1])
    function3 = logicfunction.Logic_Function('and', [2])

    register1 = register.Register([function0, function1,
                                   function2, function3],
                                  [True, False, True, False])

    assert register1.looped()
    register1.advance()
    assert not register1.looped()
    register1.advance()
    assert register1.looped()


def test_register_looped_2():
    function0 = logicfunction.Logic_Function('nor', [1, 2, 3, 4])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [0, 1])
    function3 = logicfunction.Logic_Function('and', [2])
    function4 = logicfunction.Logic_Function('and', [3])

    register1 = register.Register([function0, function1, function2,
                                   function3, function4])
    assert register1.looped()
    register1.set_state([True, True, False, True, False])
    assert not register1.looped()
    register1.set_state([True, False, False, False, False])
    assert not register1.looped()
    register1.set_state([True, True, True, True, True])
    assert not register1.looped()
    register1.set_state([False, False, False, False, False])
    assert register1.looped()


def test_register_looped_3():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])
    assert register1.looped()

    register1.set_starting_state([False, True, True])
    assert not register1.looped()
    register1.set_state([False, True, False])
    assert not register1.looped()
    register1.set_starting_state([False, True, False])
    assert register1.looped()


def test_convert_to_int_typical_1():
    assert str(register.convert_to_int([True, True, False])) == \
        '[1, 1, 0]'


def test_convert_to_int_typical_2():
    assert str(register.convert_to_int([0, 1, False, True])) == \
        '[0, 1, 0, 1]'


def test_convert_to_int_empty_list():
    assert str(register.convert_to_int([])) == \
        '[]'


def test_register_add_new_state_1():
    list = []
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])
    register1.add_new_state(list)
    assert list == [[False, True, False]]


def test_register_add_new_state_2():
    list = []
    function0 = logicfunction.Logic_Function('nor', [1, 2, 3, 4])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [0, 1])
    function3 = logicfunction.Logic_Function('and', [2])
    function4 = logicfunction.Logic_Function('and', [3])

    register1 = register.Register([function0, function1, function2,
                                   function3, function4])
    register1.add_new_state(list)
    register1.add_new_state(list)
    register1.add_new_state(list)
    assert list == [[True, False, False, False, False],
                    [True, True, False, False, False],
                    [False, True, True, False, False]]


def test_register_add_new_state_3():
    list = []
    function0 = logicfunction.Logic_Function('and', [3])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [1])
    function3 = logicfunction.Logic_Function('and', [2])

    register1 = register.Register([function0, function1,
                                   function2, function3],
                                  [True, False, True, False])
    register1.add_new_state(list)
    register1.add_new_state(list)
    assert list == [[False, True, False, True],
                    [True, False, True, False]]
