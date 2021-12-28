class WrongLogicOperatorString(Exception):
    pass


def logic_xor(p, q):
    return p ^ q


def logic_and(p, q):
    return p and q


def logic_nor(p, q):
    return not(p or q)


def logic_or(p, q):
    return p or q


def logic_nand(p, q):
    return not(p and q)


def string_to_function(function_as_string):
    if function_as_string == 'xor':
        return logic_xor
    if function_as_string == 'and':
        return logic_and
    if function_as_string == 'nor':
        return logic_nor
    if function_as_string == 'or':
        return logic_or
    if function_as_string == 'nand':
        return logic_nand
    else:
        raise WrongLogicOperatorString("Attempted to convert an invalid "
                                       "string to a Boolean operator function")


class Logic_Function:
    def __init__(self, operation, input_indexes):
        self.operation = operation
        self.input_indexes = input_indexes

    def calculate(self, inputs):
        for index in self.input_indexes:
            pass
