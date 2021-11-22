"""Contains the `Associativity` and `Operation` class.
"""

from typing import Callable
from enum import Enum

class Associativity(Enum):
    """Enum containing flags describing the operator associativity
    (which operation is executed first in case of equal precedence level).
    """
    LEFT = 0
    RIGHT = 1


class Operation:
    """Holds data about a specific mathematical operation.
    """
    def __init__(
        self,
        function: Callable,
        precedence: int,
        associativity: Associativity
    ) -> None:
        self.__function = function
        self.__precedence = precedence
        self.__associativity = associativity

    def function(self) -> Callable:
        """Returns the operation
        (function which performs the mathematical operation).
        """
        return self.__function

    def precedence(self) -> int:
        """Returns the precedence level
        (number describing the priority with which the operators are executed).
        """
        return self.__precedence

    def associativity(self) -> Associativity:
        """Returns a flag describing operator associativity
        (which operation is executed first in case of equal precedence level).
        """
        return self.__associativity
