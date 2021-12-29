class EmptyArgumentsListError(Exception):
    """
    Raised when boolean_operation_on_list function or one of the logic
    functions receives an empty list of arguments.
    """
    pass


class WrongOperatorStringError(Exception):
    """
    Exception raised when bool_operation_str_to_function function receives a
    string which does not represent a valid Boolean operation.
    """
    pass


class InvalidStateError(Exception):
    """
    Raised when attempting to set the state of a Register to a list of
    different length than the number of flip-flops of the register.
    """
    pass


def boolean_operation_on_list(arguments, operation):
    """
    Performs the given operation (a function accepting two arguments) on the
    given list of arguments and returns the result.
    """
    if not arguments:
        raise EmptyArgumentsListError("Attempted to perform a Boolean "
                                      "operation on an empty list of "
                                      "arguments.")
    result = arguments[0]
    first = True
    for argument in arguments:
        if first:
            first = False
        else:
            result = operation(result, argument)
    return result


def logic_xor(arguments):
    """
    Performs the XOR operation on the given list of Boolean values, returns
    the result.
    """
    return boolean_operation_on_list(arguments, lambda p, q: p ^ q)


def logic_and(arguments):
    """
    Performs the AND operation on the given list of Boolean values, returns
    the result.
    """
    return boolean_operation_on_list(arguments, lambda p, q: p and q)


def logic_nor(arguments):
    """
    Performs the NOR operation on the given list of Boolean values, returns
    the result.
    """
    return not boolean_operation_on_list(arguments, lambda p, q: p or q)


def logic_or(arguments):
    """
    Performs the OR operation on the given list of Boolean values, returns
    the result.
    """
    return boolean_operation_on_list(arguments, lambda p, q: p or q)


def logic_nand(arguments):
    """
    Performs the NAND operation on the given list of Boolean values, returns
    the result.
    """
    return not boolean_operation_on_list(arguments, lambda p, q: p and q)


def bool_operation_str_to_function(function_as_str):
    """
    Converts the given string representing a Boolean operation (xor, and, nor,
    or, nand) to a function. If the string does not represent any of these 5
    operations, WrongOperatorStringError is raised.
    """
    if function_as_str == 'xor':
        return logic_xor
    if function_as_str == 'and':
        return logic_and
    if function_as_str == 'nor':
        return logic_nor
    if function_as_str == 'or':
        return logic_or
    if function_as_str == 'nand':
        return logic_nand
    raise WrongOperatorStringError("Attempted to convert an invalid string to "
                                   "a Boolean operator function")


class Logic_Function:
    """
    Class Logic_Function. Represents a logic function being a Boolean
    operation (xor, and, nor, or, nand) performed on some of the flip-flop
    outputs. Attributes:
    :param _operation: Boolean operation to be performed on the inputs of the
                       function.
    :type _operation: function
    :param input_indexes: Indexes of the flip-flops outputs of which are taken
                          as inputs of the logic function.
    :type input_indexes: list[int]
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
        self.input_indexes = input_indexes.copy()

    def operation(self):
        return self._operation

    def set_operation(self, new_operation_as_str: str):
        self._operation = bool_operation_str_to_function(new_operation_as_str)

    def calculate(self, flip_flop_outputs):
        """
        Returns the output of the logic function given the list of flip-flop
        outputs.
        """
        function_inputs = [flip_flop_outputs[index]
                           for index
                           in self.input_indexes]
        return self._operation(function_inputs)


class Register:
    """
    Class Register. Represents a shift register where the input of each
    flip-flop is a single Boolean operation performed on the outputs of some
    of the other flip-flops. Attributes:
    :param _flip_flop_functions: List of logic functions being the inputs of
                                 the register's flip-flops.
    :type _flip_flop_functions: list[Logic_Function]
    :param _state: List of Boolean values representing states of the
                   register's flip-flops.
    :type _state: list[bool]
    """
    def __init__(self, flip_flop_functions, starting_state):
        """
        Creates an object of type Register.
        """
        pass

    def flip_flop_functions(self):
        return self._flip_flop_functions

    def set_flip_flop_functions(self, flip_flop_functions):
        """
        Sets the flip-flop functions list of the register to a copy of the
        given list and resets the state of all flip-flops to False.
        """
        self._flip_flop_functions = flip_flop_functions.copy()
        self.set_state([False for function in flip_flop_functions])

    def state(self):
        return self._state

    def set_state(self, new_state):
        if len(new_state) != len(self._flip_flop_functions):
            raise InvalidStateError("Attempted to set the state of a register "
                                    "to a list of a different length than the "
                                    "flip-flop functions list of the register")
        self._state = new_state

    def advance(self):
        """
        Advances the state of the register by one step.
        """
        self.set_state([flip_flop_function.calculate(self._state)
                        for flip_flop_function
                        in self._flip_flop_functions])
