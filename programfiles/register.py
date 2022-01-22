from .exceptions import (
    EmptyRegisterError,
    WrongRegisterStateError,
    WrongFlipFlopStateError
)
from copy import deepcopy


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
    :param _past_states: List of lists of Boolean values representing the
                         previous states of the register's flip-flops.
    :type _past_states: list[list[bool]]
    :param _state: List of Boolean values representing states of the
                   register's flip-flops.
    :type _state: list[bool]
    """
    def __init__(self, flip_flop_functions, starting_state=None):
        """
        Creates an object of type Register.
        """
        if flip_flop_functions == []:
            raise EmptyRegisterError
        if starting_state is None:
            self.set_flip_flop_functions(flip_flop_functions)
        else:
            self._flip_flop_functions = flip_flop_functions.copy()
            self.set_past_states([])
            self.set_state(starting_state)

    def flip_flop_functions(self):
        """
        Returns a copy of the list of the register's flip-flop functions.
        """
        return self._flip_flop_functions.copy()

    def set_flip_flop_functions(self, flip_flop_functions):
        """
        Sets the flip-flop functions list of the register to a copy of the
        given list and sets the state of all flip-flops to False. Also sets
        past states list to an empty list.
        """
        self._flip_flop_functions = flip_flop_functions.copy()
        self.set_state([False for function in flip_flop_functions])
        self.set_past_states([])

    @staticmethod
    def _check_state_elements(state):
        """
        Checks whether the given list contains only elements that represent
        a valid flip-flop state: Boolean values and integers 0 and 1.
        """
        for element in state:
            if not (isinstance(element, bool) or isinstance(element, int)):
                return False
            if element not in {0, 1}:
                return False
        return True

    def past_states(self):
        """
        Returns a copy of the past states list of the register.
        """
        return deepcopy(self._past_states)

    def set_past_states(self, new_past_states):
        """
        Sets the past states of the register to the given list.
        """
        self._past_states = new_past_states.copy()

    def state(self):
        """
        Returns the state of the register, with the values converted to type
        int.
        """
        return convert_to_int(self._state)

    def set_state(self, new_state):
        """
        Sets the current state of the register to a copy of the given list.
        """
        if len(new_state) != len(self._flip_flop_functions):
            raise WrongRegisterStateError
        if not self._check_state_elements(new_state):
            raise WrongFlipFlopStateError
        self._state = new_state.copy()

    def advance(self):
        """
        Advances the state of the register by one step. Also adds the previous
        state of the register to the register's list of past states.
        """
        self._past_states.append(self._state)
        self.set_state([flip_flop_function.calculate(self._state)
                        for flip_flop_function
                        in self._flip_flop_functions])

    def looped(self):
        """
        Returns True if the current state of the register is in the register's
        list of past states (indicating that the register has looped).
        Otherwise returns False.
        """
        return self._state in self._past_states

    def add_new_state(self, list):
        """
        Advances the register by one step and appends the resulting state of
        the register to the given list.
        """
        self.advance()
        list.append(self.state())
