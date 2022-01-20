from ..programfiles import iofunctions
from io import StringIO


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
    register = iofunctions.load_register_from_file(register_file)

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
    register = iofunctions.load_register_from_file(register_file)

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
    register = iofunctions.load_register_from_file(register_file)

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

    iofunctions.save_data_to_file(output_file, sequences, space_usage,
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

    iofunctions.save_data_to_file(output_file, sequences, space_usage,
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

    iofunctions.save_data_to_file(output_file, sequences, space_usage,
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

    assert iofunctions.get_results_string(sequences, space_usage,
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

    assert iofunctions.get_results_string(sequences, space_usage,
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

    assert iofunctions.get_results_string(sequences, space_usage,
                                          average_sequence_diversity) == \
        """The following sequences have been generated:
[1, 0]
[1, 1]
[0, 0]
[0, 1]
Space usage for this register is 12%
Average sequence diversity of the generated sequences is 1.1111
"""


def test_get_parsed_arguments_save_and_show():
    arguments = ['main.py', 'example.json', '-s', '5',
                 '-sv', 'results.json', '-sh']
    args = iofunctions.get_parsed_arguments(arguments)
    assert args.source == 'example.json'
    assert args.steps == 5
    assert args.until_looped is False
    assert args.save == 'results.json'
    assert args.show is True


def test_get_parsed_arguments_dont_save():
    arguments = ['main.py', 'example.json', '-l', '-sh']
    args = iofunctions.get_parsed_arguments(arguments)
    assert args.source == 'example.json'
    assert args.steps is None
    assert args.until_looped is True
    assert args.save is None
    assert args.show is True


def test_get_parsed_arguments_dont_show():
    arguments = ['main.py', 'ex.json', '-s', '1',
                 '-sv', 'res.json']
    args = iofunctions.get_parsed_arguments(arguments)
    assert args.source == 'ex.json'
    assert args.steps == 1
    assert args.until_looped is False
    assert args.save == 'res.json'
    assert args.show is False
