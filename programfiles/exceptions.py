class EmptyArgumentsListError(Exception):
    """
    Exception raised when boolean_operation_on_list function or one of the
    logic functions receives an empty list of arguments.
    """
    pass


class TooManyArgumentsError(Exception):
    """
    Exception raised when the logic function NOT receives more than one
    argument.
    """
    pass


class WrongOperationStringError(Exception):
    """
    Exception raised when bool_operation_str_to_function function receives a
    string which does not represent a valid Boolean operation. Attributes:
    :param invalid_string: The invalid string which caused the exception.
    :type invalid_string: str
    """
    def __init__(self, invalid_string):
        super().__init__(self)
        self.invalid_string = invalid_string


class WrongRegisterStateError(Exception):
    """
    Exception raised when attempting to set the state of a Register to a list
    of different length than the number of flip-flops of the register.
    """
    pass


class WrongFlipFlopStateError(Exception):
    """
    Exception raised when attempting to set the state of a Register to a list
    containing elements different than Boolean values or integers 0 or 1.
    """
    pass


class InvalidFlipFlopIndexError(Exception):
    """
    Exception raised when attempting to use Logic_Function.calculate when one
    of its flip-flop indexes does not represent any flip-flop in the register.
    """
    pass


class InputIndexesNotAListError(Exception):
    """
    Exception raised when attempting to use Logic_Function.calculate when one
    of its flip-flop indexes does not represent any flip-flop in the register.
    """
    pass


class EmptyRegisterError(Exception):
    """
    Exception raised when attempting to create a register with no flip-flops.
    """
    pass


class NegativeStepsNumberError(Exception):
    """
    Exception raised when attempting to calculate the outputs from a register
    when a negative number of steps is given.
    """
    pass
