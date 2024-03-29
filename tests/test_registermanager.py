from ..programfiles import logicfunction
from ..programfiles import register
from ..programfiles import registermanager
import pytest
from argparse import Namespace


def test_get_sequences_steps_1():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])

    arguments = Namespace()
    arguments.steps = 5
    arguments.until_looped = False

    manager = registermanager.Register_Manager(register1)
    sequences = manager._get_sequences(arguments)
    assert sequences == [
        [True, False, False],
        [False, True, False],
        [True, False, True],
        [True, True, False],
        [True, True, True],
        [False, True, True],
    ]


def test_get_sequences_steps_2():
    function0 = logicfunction.Logic_Function('and', [3])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [1])
    function3 = logicfunction.Logic_Function('and', [2])

    register1 = register.Register([function0, function1,
                                   function2, function3],
                                  [True, False, False, False])

    arguments = Namespace()
    arguments.steps = 7
    arguments.until_looped = False

    manager = registermanager.Register_Manager(register1)
    sequences = manager._get_sequences(arguments)
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
    function0 = logicfunction.Logic_Function('xor', [3, 4])
    function1 = logicfunction.Logic_Function('xor', [0, 4])
    function2 = logicfunction.Logic_Function('xor', [0, 1])
    function3 = logicfunction.Logic_Function('xor', [1, 2])
    function4 = logicfunction.Logic_Function('and', [0, 1, 2, 3])

    register1 = register.Register([function0, function1, function2,
                                   function3, function4],
                                  [True, False, False, False, False])

    arguments = Namespace()
    arguments.until_looped = True

    manager = registermanager.Register_Manager(register1)
    sequences = manager._get_sequences(arguments)
    assert sequences == [
        [True, False, False, False, False],
        [False, True, True, False, False],
        [False, False, True, False, False],
        [False, False, False, True, False],
        [True, False, False, False, False],
    ]


def test_get_sequences_until_looped_2():
    function0 = logicfunction.Logic_Function('nor', [1, 2, 3, 4])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [0, 1])
    function3 = logicfunction.Logic_Function('and', [2])
    function4 = logicfunction.Logic_Function('and', [3])

    register1 = register.Register([function0, function1, function2,
                                   function3, function4])

    arguments = Namespace()
    arguments.until_looped = True

    manager = registermanager.Register_Manager(register1)
    sequences = manager._get_sequences(arguments)
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
    function0 = logicfunction.Logic_Function('and', [1, 3])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('or', [1, 3])
    function3 = logicfunction.Logic_Function('and', [2])

    register1 = register.Register([function0, function1, function2,
                                   function3],
                                  [True, False, False, False])

    arguments = Namespace()
    arguments.until_looped = True

    manager = registermanager.Register_Manager(register1)
    sequences = manager._get_sequences(arguments)
    assert sequences == [
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False]
    ]


def test_get_sequences_until_looped_no_return_to_beginning_2():
    function0 = logicfunction.Logic_Function('or', [1, 2])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('nor', [0, 1])

    register1 = register.Register([function0, function1, function2],
                                  [False, True, True])

    arguments = Namespace()
    arguments.until_looped = True

    manager = registermanager.Register_Manager(register1)
    sequences = manager._get_sequences(arguments)
    assert sequences == [
        [False, True, True],
        [True, False, False],
        [False, True, False],
        [True, False, False]
    ]


def test_get_sequence_diversity_typical_1():
    assert registermanager.get_sequence_diversity([True, True,
                                                   False, True]) == 2


def test_get_sequence_diversity_typical_2():
    assert registermanager.get_sequence_diversity([True, False, False]) == 1


def test_get_sequence_diversity_one_element():
    assert registermanager.get_sequence_diversity([True]) == 0


def test_get_sequence_diversity_all_elements_the_same_1():
    assert registermanager.get_sequence_diversity([False, False]) == 0


def test_get_sequence_diversity_all_elements_the_same_2():
    assert registermanager.get_sequence_diversity([True, True, True,
                                                   True, True]) == 0


def test_get_sequence_diversity_max_diversity():
    assert registermanager.get_sequence_diversity([True, False, True,
                                                   False, True, False]) == 5


def test_get_average_sequence_diversity_1():
    sequences = [
        [True, False, True, True],
        [True, False, False, True],
        [True, False, True, False],
        [False, True, False, True],
    ]

    function = logicfunction.Logic_Function('or', [0])
    register1 = register.Register([function])
    manager = registermanager.Register_Manager(register1)
    manager.outputs['sequences'] = sequences
    assert manager._get_average_sequence_diversity() == pytest.approx(2.5)


def test_get_average_sequence_diversity_2():
    sequences = [
        [True, True, False, True],
        [True, False, False],
        [True],
        [False, False],
        [True, True, True, True, True],
        [True, False, True, False, True, False]
    ]

    function = logicfunction.Logic_Function('or', [0])
    register1 = register.Register([function])
    manager = registermanager.Register_Manager(register1)
    manager.outputs['sequences'] = sequences
    assert manager._get_average_sequence_diversity() == \
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

    function = logicfunction.Logic_Function('or', [0])
    register1 = register.Register([function])
    manager = registermanager.Register_Manager(register1)
    manager.outputs['sequences'] = sequences
    assert manager._get_average_sequence_diversity() == pytest.approx(2)


def test_get_number_of_unique_sequences_all_the_same():
    sequences = [
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True],
        [True, False, True]
    ]
    assert registermanager.get_number_of_unique_sequences(sequences) == 1


def test_get_number_of_unique_sequences_all_different():
    sequences = [
        [True, False, True, True],
        [True, False, False, True],
        [True, False, True, False],
        [False, True, False, True],
    ]
    assert registermanager.get_number_of_unique_sequences(sequences) == 4


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
    assert registermanager.get_number_of_unique_sequences(sequences) == 5


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
    assert registermanager.get_number_of_unique_sequences(sequences) == 3


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

    function = logicfunction.Logic_Function('or', [0])
    register1 = register.Register([function])
    manager = registermanager.Register_Manager(register1)
    manager.outputs['sequences'] = sequences
    assert manager._get_space_usage() == pytest.approx(0.75)


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

    function = logicfunction.Logic_Function('or', [0])
    register1 = register.Register([function])
    manager = registermanager.Register_Manager(register1)
    manager.outputs['sequences'] = sequences
    assert manager._get_space_usage() == pytest.approx(0.3125)


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

    function = logicfunction.Logic_Function('or', [0])
    register1 = register.Register([function])
    manager = registermanager.Register_Manager(register1)
    manager.outputs['sequences'] = sequences
    assert manager._get_space_usage() == pytest.approx(0.1875)


def test_calculate_outputs_1():
    function0 = logicfunction.Logic_Function('xor', [1, 2])
    function1 = logicfunction.Logic_Function('or', [0])
    function2 = logicfunction.Logic_Function('and', [1])

    register1 = register.Register([function0, function1, function2],
                                  [True, False, False])

    arguments = Namespace()
    arguments.steps = 5
    arguments.until_looped = False

    manager = registermanager.Register_Manager(register1)
    manager.calculate_outputs(arguments)
    assert manager.outputs['sequences'] == [
        [True, False, False],
        [False, True, False],
        [True, False, True],
        [True, True, False],
        [True, True, True],
        [False, True, True]
    ]
    assert manager.outputs['average_sequence_diversity'] == \
        pytest.approx(1.1667, abs=1e-4)
    assert manager.outputs['space_usage'] == pytest.approx(0.75)


def test_calculate_outputs_2():
    function0 = logicfunction.Logic_Function('nor', [1, 2, 3, 4])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('and', [0, 1])
    function3 = logicfunction.Logic_Function('and', [2])
    function4 = logicfunction.Logic_Function('and', [3])

    register1 = register.Register([function0, function1, function2,
                                   function3, function4])

    arguments = Namespace()
    arguments.until_looped = True

    manager = registermanager.Register_Manager(register1)
    manager.calculate_outputs(arguments)
    assert manager.outputs['sequences'] == [
        [False, False, False, False, False],
        [True, False, False, False, False],
        [True, True, False, False, False],
        [False, True, True, False, False],
        [False, False, False, True, False],
        [False, False, False, False, True],
        [False, False, False, False, False]
    ]
    assert manager.outputs['average_sequence_diversity'] == pytest.approx(1)
    assert manager.outputs['space_usage'] == pytest.approx(0.1875)


def test_calculate_outputs_3():
    function0 = logicfunction.Logic_Function('and', [1, 3])
    function1 = logicfunction.Logic_Function('and', [0])
    function2 = logicfunction.Logic_Function('or', [1, 3])
    function3 = logicfunction.Logic_Function('and', [2])

    register1 = register.Register([function0, function1, function2,
                                   function3],
                                  [True, False, False, False])

    arguments = Namespace()
    arguments.until_looped = True

    manager = registermanager.Register_Manager(register1)
    manager.calculate_outputs(arguments)
    assert manager.outputs['sequences'] == [
        [True, False, False, False],
        [False, True, False, False],
        [False, False, True, False],
        [False, False, False, True],
        [False, False, True, False]
    ]
    assert manager.outputs['average_sequence_diversity'] == pytest.approx(1.6)
    assert manager.outputs['space_usage'] == pytest.approx(0.25)
