"""Holds the Expression class.
"""

from __future__ import annotations
from typing import Callable, Union

class Expression:
    """Represents a specific mathematical expression.
    Examples: 3 + 4, or 4 * a, where a is another expression.
    """

    def __init__(
            self,
            operation: Callable[[list[float]], float],
            operands: list[Union[Expression, float]]
        ) -> None:

        self.__operation = operation
        self.__operands = operands

    def get_operation(self) -> Callable[[list[float]], float]:
        """Returns operation.
        """

        return self.__operation

    def get_operands(self) -> list[Union[Expression, float]]:
        """Returns list of operands.
        """

        return self.__operands

    def calculate(self) -> float:
        """Returns value of the expression.
        """

        calculated_operands = [
            x.calculate() if isinstance(x, Expression)
            else x
            for x in self.get_operands()
        ]

        return self.get_operation()(calculated_operands)
