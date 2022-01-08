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
