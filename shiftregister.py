import sys
import argparse
import json


class EmptyArgumentsListError(Exception):
    """
    Exception raised when boolean_operation_on_list function or one of the
    logic functions receives an empty list of arguments.
    """
    pass


class WrongOperationStringError(Exception):
    """
    Exception raised when bool_operation_str_to_function function receives a
    string which does not represent a valid Boolean operation.
    """
    pass


class InvalidStateError(Exception):
    """
    Exception raised when attempting to set the state of a Register to a list
    of different length than the number of flip-flops of the register.
    """
    pass


def operation_on_list(arguments, operation):
    """
    Performs the given operation (a function accepting two arguments) on the
    given list of arguments (going from lower to higher indexes) and returns
    the result.
    """
    if not arguments:
        raise EmptyArgumentsListError
    result = arguments[0]
    for argument in arguments[1:]:
        result = operation(result, argument)
    return result


def logic_xor(arguments):
    """
    Performs the XOR operation on the given list of Boolean values, returns
    the result.
    """
    if not arguments:
        raise EmptyArgumentsListError("Attempted to perform the XOR operation"
                                      " on an empty list of arguments.")
    one_true = False
    for argument in arguments:
        if argument:
            if not one_true:
                one_true = True
            else:
                return False
    return one_true


def logic_and(arguments):
    """
    Performs the AND operation on the given list of Boolean values, returns
    the result.
    """
    try:
        return operation_on_list(arguments, lambda p, q: p and q)
    except EmptyArgumentsListError as e:
        raise EmptyArgumentsListError("Attempted to perform the AND operation"
                                      " on an empty list of arguments.") from e


def logic_or(arguments):
    """
    Performs the OR operation on the given list of Boolean values, returns
    the result.
    """
    try:
        return operation_on_list(arguments, lambda p, q: p or q)
    except EmptyArgumentsListError as e:
        raise EmptyArgumentsListError("Attempted to perform the OR operation"
                                      " on an empty list of arguments.") from e


def bool_operation_str_to_function(function_as_str):
    """
    Converts the given string representing a Boolean operation (xor, and, nor,
    or, nand) to a function. If the string does not represent any of these 5
    operations, WrongOperationStringError is raised.
    """
    if function_as_str == 'xor':
        return logic_xor
    if function_as_str == 'and':
        return logic_and
    if function_as_str == 'nor':
        return lambda arguments: not logic_or(arguments)
    if function_as_str == 'or':
        return logic_or
    if function_as_str == 'nand':
        return lambda arguments: not logic_and(arguments)
    raise WrongOperationStringError("Attempted to convert an invalid string to"
                                    " a Boolean operator function")


class Logic_Function:
    """
    Class Logic_Function. Represents a logic function being a Boolean
    operation (xor, and, nor, or, nand) performed on some of the flip-flop
    outputs. Attributes:
    :param _operation: Boolean operation to be performed on the inputs of the
                       function.
    :type _operation: function
    :param _input_indexes: Indexes of the flip-flops outputs of which are taken
                           as inputs of the logic function.
    :type _input_indexes: list[int]
    """
    def __init__(self, operation, input_indexes):
        """
        Creates an object of class Logic_Function. Takes two arguments:
         - a string representing the Boolean operation the function is supposed
           to perform
         - a list of indexes of the flip-flops outputs of which are taken as
           inputs of the logic function.
        """
        self.set_operation(operation)
        self.set_input_indexes(input_indexes)

    def operation(self):
        return self._operation

    def set_operation(self, new_operation):
        self._operation = bool_operation_str_to_function(new_operation)

    def input_indexes(self):
        return self._input_indexes.copy()

    def set_input_indexes(self, new_input_indexes):
        self._input_indexes = new_input_indexes.copy()

    def calculate(self, flip_flop_outputs):
        """
        Returns the output of the logic function given the list of flip-flop
        outputs.
        """
        # @TODO Handle IndexError and TypeError in this function
        function_inputs = [flip_flop_outputs[index]
                           for index
                           in self._input_indexes]
        return self._operation(function_inputs)


class Register:
    """
    Class Register. Represents a shift register where the input of each
    flip-flop is a single Boolean operation performed on the outputs of some
    of the other flip-flops. Attributes:
    :param _flip_flop_functions: List of logic functions being the inputs of
                                 the register's flip-flops.
    :type _flip_flop_functions: list[Logic_Function]
    :param _starting_state: List of Boolean values representing the starting
                            states of the register's flip-flops.
    :type _starting_state: list[bool]
    :param _state: List of Boolean values representing states of the
                   register's flip-flops.
    :type _state: list[bool]
    """
    def __init__(self, flip_flop_functions, starting_state=None):
        """
        Creates an object of type Register.
        """
        if starting_state is None:
            self.set_flip_flop_functions(flip_flop_functions)
        else:
            self._flip_flop_functions = flip_flop_functions.copy()
            self.set_starting_state(starting_state)
            self.set_state(starting_state)

    def flip_flop_functions(self):
        return self._flip_flop_functions.copy()

    def set_flip_flop_functions(self, flip_flop_functions):
        """
        Sets the flip-flop functions list of the register to a copy of the
        given list and resets the state of all flip-flops to False.
        """
        self._flip_flop_functions = flip_flop_functions.copy()
        self.set_starting_state([False for function in flip_flop_functions])
        self.set_state([False for function in flip_flop_functions])

    def starting_state(self):
        return self._starting_state.copy()

    def set_starting_state(self, new_starting_state):
        if len(new_starting_state) != len(self._flip_flop_functions):
            raise InvalidStateError("Attempted to set the starting state of a "
                                    "register to a list of a different length "
                                    "than the flip-flop functions list of the "
                                    "register")
        self._starting_state = new_starting_state.copy()

    def state(self):
        return self._state.copy()

    def set_state(self, new_state):
        if len(new_state) != len(self._flip_flop_functions):
            raise InvalidStateError("Attempted to set the state of a register "
                                    "to a list of a different length than the "
                                    "flip-flop functions list of the register")
        self._state = new_state.copy()

    def advance(self):
        """
        Advances the state of the register by one step.
        """
        self.set_state([flip_flop_function.calculate(self._state)
                        for flip_flop_function
                        in self._flip_flop_functions])

    def looped(self):
        """
        Returns True if the current state of the register is the same as the
        starting state of the register. Otherwise, returns False.
        """
        return self._starting_state == self._state

    def add_new_state(self, list):
        """
        Advances the register by one step and appends the resulting state of
        the register to the given list.
        """
        self.advance()
        list.append(convert_to_int(self.state()))


def convert_to_int(list):
    """
    Converts each of the given list's contents to type int.
    """
    return [int(value) for value in list]


def get_sequences(register, arguments):
    """
    Returns a list of sequences generated for the given shift register and
    arguments. Includes the starting state of the register.
    """
    sequences = [convert_to_int(register.state())]
    if arguments.until_looped:
        register.add_new_state(sequences)
        max_sequences_amount = 2**len(register.flip_flop_functions())
        while not register.looped() and len(sequences) <= max_sequences_amount:
            register.add_new_state(sequences)
    else:
        for i in range(0, arguments.steps):
            register.add_new_state(sequences)
    return sequences


def get_sequence_diversity(sequence):
    """
    Returns the number of pairs of neighbouring different bits in the given
    sequence of Boolean values.
    """
    result = 0
    for bit1, bit2 in zip(sequence[:-1], sequence[1:]):
        if bit1 ^ bit2:
            result += 1
    return result


def get_average_sequence_diversity(sequences):
    """
    Returns the average number of pairs of neighbouring different bits in the
    given list of sequences of Boolean values.
    """
    return sum([get_sequence_diversity(sequence)
                for sequence
                in sequences]) / len(sequences)


def get_number_of_unique_sequences(sequences):
    """
    Returns the number of unique sequences in the given list.
    """
    unique_sequences = {tuple(sequence) for sequence in sequences}
    return len(unique_sequences)


def get_space_usage(sequences):
    """
    Returns the space usage of the given sequences in %. Space usage is how
    many unique sequences were generated divided by the maximum number of
    sequences generated by a register of this size.
    """
    return (get_number_of_unique_sequences(sequences) /
            (2 ** len(sequences[0]))) * 100


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


def save_data_to_file(file_handle, sequences, space_usage,
                      average_sequence_diversity):
    """
    Writes the given generated register data into the given file in the JSON
    format.
    """
    file_handle.write('{\n'
                      '\t"sequences": [\n')
    for sequence in sequences[:-1]:
        file_handle.write(f'\t\t{sequence},\n')
    file_handle.write(f'\t\t{sequences[-1]}\n'
                      '\t],\n'
                      f'\t"space_usage": {space_usage},\n'
                      '\t"average_sequence_diversity": '
                      f'{average_sequence_diversity}\n'
                      '}')


def get_results_string(sequences, space_usage, average_sequence_diversity):
    """
    Returns the given generated register data as a string.
    """
    results = 'The following sequences have been generated:\n'
    for sequence in sequences:
        results += str(sequence) + '\n'
    results += 'Average sequence diversity of the generated sequences is '\
               f'{average_sequence_diversity}\n'\
               f'Space usage for this register is {space_usage}%\n'
    return results


def main(arguments):
    parser = argparse.ArgumentParser(description='Simulates a shift register. '
                                                 'For more information see '
                                                 'instruction.txt.')
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
    args = parser.parse_args(arguments[1:])

    with open(args.source, 'r') as source_file:
        register = load_register_from_file(source_file)

    sequences = get_sequences(register, args)
    average_sequence_diversity = round(
        get_average_sequence_diversity(sequences), 4)
    space_usage = round(get_space_usage(sequences), 4)

    if args.save:
        with open(args.save, 'w') as file_handle:
            save_data_to_file(file_handle, sequences, space_usage,
                              average_sequence_diversity)

    if args.show:
        print(get_results_string(sequences, space_usage,
                                 average_sequence_diversity))


if __name__ == '__main__':
    main(sys.argv)
