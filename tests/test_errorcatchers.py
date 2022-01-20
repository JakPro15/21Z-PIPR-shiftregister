from ..programfiles import errorcatchers
from ..programfiles import logicfunction
from ..programfiles import register
from argparse import Namespace


def test_attempt_to_load_register_nonexistent_file():
    assert errorcatchers.attempt_to_load_register('grfe') == \
        'main.py: error: the given source file does not exist'


def test_attempt_to_calculate_sequences_noerror():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])

    arguments = Namespace()
    arguments.steps = 2
    arguments.until_looped = False

    sequences = [
        [True, False, False],
        [False, True, False],
        [True, False, True]
    ]
    assert errorcatchers.attempt_to_calculate_sequences(
        register1,
        arguments
    ) == sequences


def test_attempt_to_calculate_sequences_empty_arguments_list_error():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])

    arguments = Namespace()
    arguments.source = 'source'
    arguments.steps = 2
    arguments.until_looped = False

    assert errorcatchers.attempt_to_calculate_sequences(
        register1,
        arguments
    ) == 'main.py: error: (in source) a flip-flop function '\
         'must take at least one argument - its input_indexes list '\
         'cannot be empty'


def test_attempt_to_calculate_sequences_too_many_arguments_error():
    function0 = logicfunction.Logic_Function('not', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])

    arguments = Namespace()
    arguments.source = 'source'
    arguments.steps = 2
    arguments.until_looped = False

    assert errorcatchers.attempt_to_calculate_sequences(
        register1,
        arguments
    ) == 'main.py: error: (in source) the NOT operation cannot '\
         'take more than 1 argument - input_indexes list of a '\
         'flip-flop function with operation NOT must contain only one '\
         'index'


def test_attempt_to_calculate_sequences_invalid_flip_flop_index_error():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [3])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])

    arguments = Namespace()
    arguments.source = 'source'
    arguments.steps = 2
    arguments.until_looped = False

    assert errorcatchers.attempt_to_calculate_sequences(
        register1,
        arguments
    ) == 'main.py: error: (in source) one of the given '\
         'flip-flop indexes does not represent a valid flip-flop index '\
         '- all values in input_indexes must be nonnegative integers '\
         'smaller than the number of flip-flops in the register'
