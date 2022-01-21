from .iofunctions import load_register_from_file
from .resultsfunctions import get_sequences
from json.decoder import JSONDecodeError
from .exceptions import (
    EmptyArgumentsListError,
    InputIndexesNotAListError,
    InvalidFlipFlopIndexError,
    TooManyArgumentsError,
    WrongFlipFlopStateError,
    WrongOperationStringError,
    WrongRegisterStateError
)


def attempt_to_load_register(source):
    try:
        with open(source, 'r') as source_file:
            register = load_register_from_file(source_file)
    except FileNotFoundError:
        return 'main.py: error: the given source file does not exist'
    except JSONDecodeError:
        return f'main.py: error: {source} is not a valid JSON file'
    except KeyError:
        return f'main.py: error: {source} must contain both '\
               '"flip_flop_functions" list and "starting_state" list. Each '\
               'element of the flip-flop functions list must contain both '\
               '"operation" string and "input_indexes" list.'
    except WrongOperationStringError as e:
        return f'main.py: error: (in {source}) {e.invalid_string} is not '\
               'a valid Boolean operation'
    except WrongRegisterStateError:
        return f'main.py: error: (in {source}) the starting state of a '\
               'register must be valid for this register - its number of '\
               'elements must be the same as the amount of flip-flops in the '\
               'register'
    except WrongFlipFlopStateError:
        return f'main.py: error: (in {source}) the starting state of the '\
               'register must only contain integers 0 and 1, in order to '\
               'represent valid states of the flip-flops'
    except InputIndexesNotAListError:
        return f'main.py: error: (in {source}) input indexes data for a '\
               'flip-flop should be given as a list'
    except TypeError:
        return f'main.py: error: (in {source}) "flip_flop_functions" and '\
               '"starting_state" should be lists, elements of '\
               '"flip_flop_functions" list should be dictionaries'
    if not register.flip_flop_functions():
        return f'main.py: error: (in {source}) the register must contain '\
               'at least one flip-flop - flip_flop_functions list cannot be '\
               'empty'
    return register


def attempt_to_calculate_sequences(register, args):
    try:
        sequences = get_sequences(register, args)
    except EmptyArgumentsListError:
        return f'main.py: error: (in {args.source}) a flip-flop function '\
               'must take at least one argument - its input_indexes list '\
               'cannot be empty'
    except TooManyArgumentsError:
        return f'main.py: error: (in {args.source}) the NOT operation cannot '\
               'take more than 1 argument - input_indexes list of a '\
               'flip-flop function with operation NOT must contain only one '\
               'index'
    except InvalidFlipFlopIndexError:
        return f'main.py: error: (in {args.source}) one of the given '\
               'flip-flop indexes does not represent a valid flip-flop index'
    return sequences
