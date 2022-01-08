from .exceptions import InvalidStateError


def convert_to_int(list):
    """
    Converts each of the given list's contents to type int.
    """
    return [int(value) for value in list]


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
        """
        Returns the state of the register, with the values converted to type
        int.
        """
        return convert_to_int(self._state)

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
        list.append(self.state())
