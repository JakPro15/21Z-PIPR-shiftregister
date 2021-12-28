class WrongOperatorStringError(Exception):
    pass


class InvalidStateError(Exception):
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


def bool_operation_str_to_function(function_as_str):
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
    else:
        raise WrongOperatorStringError("Attempted to convert an invalid "
                                       "string to a Boolean operator function")


class Logic_Function:
    def __init__(self, operation: str, input_indexes: "list[int]"):
        self.set_operation(operation)
        self.input_indexes = input_indexes

    def operation(self):
        return self._operation

    def set_operation(self, new_operation_as_str: str):
        self._operation = bool_operation_str_to_function(new_operation_as_str)

    def calculate(self, inputs: "list[bool]"):
        result = inputs[self.input_indexes[0]]
        first = True
        for index in self.input_indexes:
            if first:
                first = False
            else:
                result = self._operation(result, inputs[index])
        return result


class Register:
    def __init__(self, flip_flop_functions: "list[Logic_Function]",
                 starting_state: "list[bool]"):
        pass

    def flip_flop_functions(self) -> "list[Logic_Function]":
        return self._flip_flop_functions

    def set_flip_flop_functions(self,
                                flip_flop_functions: "list[Logic_Function]"):
        self._flip_flop_functions = flip_flop_functions
        self.set_state([False for function in flip_flop_functions])

    def state(self) -> "list[bool]":
        return self._state

    def set_state(self, new_state: "list[bool]") -> None:
        if len(new_state) != len(self._flip_flop_functions):
            raise InvalidStateError("Attempted to set the state of a register "
                                    "to a list of a different length than the "
                                    "flip-flop functions list of the register")
        self._state = new_state

    def advance(self):
        self.set_state([flip_flop_function.calculate(self._state)
                        for flip_flop_function
                        in self._flip_flop_functions])
