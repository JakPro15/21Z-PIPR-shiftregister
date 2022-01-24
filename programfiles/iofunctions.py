import json
import argparse
from .logicfunction import Logic_Function
from .register import Register


def load_register_from_file(file_handle):
    """
    Loads register data from the given file, returns object of class Register.
    """
    register_data = json.load(file_handle)
    flip_flop_inputs = [Logic_Function(function_data['operation'],
                                       function_data['input_indexes'])
                        for function_data
                        in register_data['flip_flop_functions']]
    return Register(flip_flop_inputs, register_data['starting_state'])


def save_data_to_file(file_handle, outputs):
    """
    Writes the given generated register data into the given file in the JSON
    format.
    """
    sequences = outputs['sequences']
    space_usage = outputs['space_usage']
    average_sequence_diversity = outputs['average_sequence_diversity']

    file_handle.write('{\n'
                      '    "sequences": [\n')
    for sequence in sequences[:-1]:
        file_handle.write(f'        {sequence},\n')
    file_handle.write(f'        {sequences[-1]}\n'
                      '    ],\n'
                      f'    "space_usage": {space_usage},\n'
                      '    "average_sequence_diversity": '
                      f'{average_sequence_diversity}\n'
                      '}')


def get_results_string(outputs):
    """
    Returns the given generated register data as a string.
    """
    sequences = outputs['sequences']
    space_usage = round(outputs['space_usage'] * 100, 4)
    average_sequence_diversity = \
        round(outputs['average_sequence_diversity'], 4)

    results = 'The following sequences have been generated:\n'
    for sequence in sequences:
        results += str(sequence) + '\n'
    results += f'Space usage for this register is {space_usage}%\n'\
               'Average sequence diversity of the generated sequences is '\
               f'{average_sequence_diversity}\n'
    return results


def get_parsed_arguments(arguments):
    """
    Parses arguments given to the program using argparse.
    """
    parser = argparse.ArgumentParser(
        description='Simulates a shift register. For more information see '
                    'dokumentacja.pdf'
    )
    parser.add_argument('source',
                        help='file from which the program loads register data')
    end_condition = parser.add_mutually_exclusive_group(required=True)
    end_condition.add_argument('-s', '--steps', type=int,
                               help='number of steps the program will advance '
                                    'the state of the register by')
    end_condition.add_argument('-l', '--until-looped', action='store_true',
                               help='with this option the program will '
                                    'generate sequences until it returns '
                                    'to the original sequence')
    parser.add_argument('-sv', '--save',
                        help='save the generated sequences into the given '
                             'file')
    parser.add_argument('-sh', '--show', action='store_true',
                        help='show the generated sequences in standard output')
    return parser.parse_args(arguments[1:])
