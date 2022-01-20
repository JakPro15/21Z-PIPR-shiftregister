from .exceptions import WrongRegisterStateError, WrongFlipFlopStateError


def convert_to_int(iterable):
    """
    Converts each of the given iterable's contents to type int. Does not
    modify the iterable, returns the result as a list.
    """
    return [int(value) for value in iterable]


class Register:
    """
    Class Register. Represents a shift register where the input of each
    flip-flop is a single Boolean operation performed on the outputs of some
    of the other flip-flops. Attributes:
    :param _flip_flop_functions: List of logic functions being the inputs of
                                 the register's flip-flops.
    :type _flip_flop_functions: list[Logic_Function]
    :param _past_states: List of lists of Boolean values representing the
                         previous states of the register's flip-flops.
    :type _past_states: set[tuple[bool]]
    :param _state: List of Boolean values representing states of the
                   register's flip-flops.
    :type _state: tuple[bool]
    """
    def __init__(self, flip_flop_functions, starting_state=None):
        """
        Creates an object of type Register.
        """
        if starting_state is None:
            self.set_flip_flop_functions(flip_flop_functions)
        else:
            self._flip_flop_functions = flip_flop_functions.copy()
            self._past_states = set()
            self.set_state(starting_state)

    def flip_flop_functions(self):
        """
        Returns a copy of the _flip_flop_functions parameter.
        """
        return self._flip_flop_functions.copy()

    def set_flip_flop_functions(self, flip_flop_functions):
        """
        Sets the flip-flop functions list of the register to a copy of the
        given list and resets the state of all flip-flops to False.
        """
        self._flip_flop_functions = flip_flop_functions.copy()
        self.set_past_states(set())
        self.set_state([False for function in flip_flop_functions])

    @staticmethod
    def _check_state_elements(state):
        for element in state:
            if not (isinstance(element, bool) or isinstance(element, int)):
                return False
            if element not in {0, 1}:
                return False
        return True

    def past_states(self):
        """
        Sets the past states of the register to the given set.
        """
        return self._past_states.copy()

    def set_past_states(self, new_past_states):
        """
        Sets the past states of the register to the given set.
        """
        self._past_states = new_past_states.copy()

    def state(self):
        """
        Returns the state of the register as a list, with the values converted
        to type int.
        """
        return convert_to_int(self._state)

    def set_state(self, new_state):
        """
        Sets the current state of the register to the given list.
        """
        if len(new_state) != len(self._flip_flop_functions):
            raise WrongRegisterStateError
        if not self._check_state_elements(new_state):
            raise WrongFlipFlopStateError
        self._state = tuple(new_state)

    def advance(self):
        """
        Advances the state of the register by one step. The previous state of
        the register is added to _previous_states.
        """
        self._past_states.add(self._state)
        self.set_state([flip_flop_function.calculate(self._state)
                        for flip_flop_function
                        in self._flip_flop_functions])

    def looped(self):
        """
        Returns True if the current state of the register is the same as the
        starting state of the register. Otherwise, returns False.
        """
        return self._state in self._past_states

    def add_new_state(self, list):
        """
        Advances the register by one step and appends the resulting state of
        the register to the given list.
        """
        self.advance()
        list.append(self.state())
