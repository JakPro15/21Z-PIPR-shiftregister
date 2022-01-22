from json.decoder import JSONDecodeError
from .exceptions import (
    EmptyArgumentsListError,
    InputIndexesNotAListError,
    InvalidFlipFlopIndexError,
    NegativeStepsNumberError,
    TooManyArgumentsError,
    WrongFlipFlopStateError,
    WrongOperationStringError,
    WrongRegisterStateError,
    EmptyRegisterError
)


def get_exception_info(exception, source_file_name):
    if isinstance(exception, FileNotFoundError):
        info = 'main.py: error: the given source file does not exist'
    elif isinstance(exception, JSONDecodeError):
        info = f'main.py: error: {source_file_name} is not a valid JSON file'
    elif isinstance(exception, KeyError):
        info = f'main.py: error: {source_file_name} must contain both '\
               '"flip_flop_functions" list and "starting_state" list. Each '\
               'element of the flip-flop functions list must contain both '\
               '"operation" string and "input_indexes" list.'
    elif isinstance(exception, WrongOperationStringError):
        info = f'main.py: error: (in {source_file_name}) '\
               f'{exception.invalid_string} is not a valid Boolean operation'
    elif isinstance(exception, WrongRegisterStateError):
        info = f'main.py: error: (in {source_file_name}) the starting state '\
               'of a register must be valid for this register - its number of'\
               ' elements must be the same as the amount of flip-flops in the'\
               ' register'
    elif isinstance(exception, WrongFlipFlopStateError):
        info = f'main.py: error: (in {source_file_name}) the starting state '\
               'of the register must only contain integers 0 and 1, in order '\
               'to represent valid states of the flip-flops'
    elif isinstance(exception, InputIndexesNotAListError):
        info = f'main.py: error: (in {source_file_name}) input indexes data '\
               'for a flip-flop should be given as a list'
    elif isinstance(exception, TypeError):
        info = f'main.py: error: (in {source_file_name}) '\
               '"flip_flop_functions" and "starting_state" should be lists, '\
               'elements of "flip_flop_functions" list should be dictionaries'
    elif isinstance(exception, EmptyRegisterError):
        info = f'main.py: error: (in {source_file_name}) the register must '\
              'contain at least one flip-flop - flip_flop_functions list '\
              'cannot be empty'
    elif isinstance(exception, EmptyArgumentsListError):
        info = f'main.py: error: (in {source_file_name}) a flip-flop function'\
               ' must take at least one argument - its input_indexes list '\
               'cannot be empty'
    elif isinstance(exception, TooManyArgumentsError):
        info = f'main.py: error: (in {source_file_name}) the NOT operation '\
               'cannot take more than 1 argument - input_indexes list of a '\
               'flip-flop function with operation NOT must contain only one '\
               'index'
    elif isinstance(exception, InvalidFlipFlopIndexError):
        info = f'main.py: error: (in {source_file_name}) one of the given '\
               'flip-flop indexes does not represent a valid flip-flop index'
    elif isinstance(exception, NegativeStepsNumberError):
        info = 'main.py: error: steps number cannot be negative'
    else:
        info = 'main.py: error: an unknown error has occurred'
    return info
