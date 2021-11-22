"""Contains the `Operator` class.
"""

from typing import Callable
from enum import Enum

class MathOperator:
    """Holds data about a specific mathematical operator.
    """

    class Associativity(Enum):
        """Enum containing flags describing the operator associativity
        (which operation is executed first in case of equal precedence level).
        """
        LEFT = 0
        RIGHT = 1

    def __init__(
        self,
        operation: Callable,
        precedence_level: int,
        associativity: Associativity
    ) -> None:
        self._operation = operation
        self._precedence_level = precedence_level
        self._associativity = associativity

    def operation(self) -> Callable:
        """Returns the operation
        (function which performs the mathematical operation).
        """
        return self._operation

    def precedence_level(self) -> int:
        """Returns the precedence level
        (number describing the priority with which the operators are executed).
        """
        return self._precedence_level

    def associativity(self) -> Associativity:
        """Returns a flag describing operator associativity
        (which operation is executed first in case of equal precedence level).
        """
        return self._associativity
