from .exceptions import EmptyArgumentsListError, WrongOperationStringError


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
        # These exceptions signify invalid input in the file
        function_inputs = [flip_flop_outputs[index]
                           for index
                           in self._input_indexes]
        return self._operation(function_inputs)
