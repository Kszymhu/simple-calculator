"""Contains the `Operations` class.
"""

from math_operator import MathOperator as operator

class Operations:
    """Contains methods for performing all of the calculations the calculator is capable of.
    """
    @staticmethod
    def addition(stack: list) -> None:
        """Pops two elements of the stack, adds them, and pushes the result.
        Elements don't need to fit any additional requirements.
        """
        num_b = stack.pop()
        num_a = stack.pop()
        stack.append(num_a + num_b)

    @staticmethod
    def subtraction(stack: list) -> None:
        """Pops two elements of the stack, subtracts the first one from the second one,
        then pushes the result.
        Elements don't need to fit any additional requirements.
        """
        num_b = stack.pop()
        num_a = stack.pop()
        stack.append(num_a - num_b)

    @staticmethod
    def multiplication(stack: list) -> None:
        """Pops two elements of the stack, multiplies them, then pushes the result.
        Elements don't need to fit any additional requirements.
        """
        num_b = stack.pop()
        num_a = stack.pop()
        stack.append(num_a * num_b)

    @staticmethod
    def division(stack: list) -> None:
        """Pops two elements of the stack,
        divides the second one by the first one, then pushes the result.
        Raises ValueError if the first popped element is 0.
        """
        num_b = stack.pop()
        num_a = stack.pop()
        if num_b == 0:
            raise ValueError

        stack.append(num_a / num_b)

    @staticmethod
    def exponentiation(stack: list) -> None:
        """Pops two elements of the stack,
        raises the second one to the power of the first one, then pushes the result.
        Elements don't need to fit any additional requirements.
        """
        num_b = stack.pop()
        num_a = stack.pop()
        stack.append(num_a ** num_b)

    @staticmethod
    def root(stack: list) -> None:
        """Pops two elements of the stack,
        calculates the `second popped element`th root of the first one, then pushes the result.
        Raises ValueError if the first popped element is negative, or when the second element is 0.
        """
        num_b = stack.pop()
        num_a = stack.pop()
        if num_b < 0 or num_a == 0:
            raise ValueError

        stack.append(num_a ** (1 / num_b))

    @staticmethod
    def modulo(stack: list) -> None:
        """Pops two elements of the stack,
        divides the second one by the first one, then pushes the remainder.
        Raises ValueError if the first popped element is 0.
        """
        num_b = stack.pop()
        num_a = stack.pop()

        if num_b == 0:
            raise ValueError

        stack.append(num_a % num_b)

IDENTIFIERS_VS_OPERATORS = {
        "+": operator(Operations.addition, 1, operator.Associativity.LEFT),
        "-": operator(Operations.subtraction, 1, operator.Associativity.LEFT),
        "*": operator(Operations.multiplication, 2, operator.Associativity.LEFT),
        "/": operator(Operations.division, 2, operator.Associativity.LEFT),
        "%": operator(Operations.modulo, 2, operator.Associativity.LEFT),
        "^": operator(Operations.exponentiation, 3, operator.Associativity.RIGHT),
        "root": operator(Operations.root, 3, operator.Associativity.RIGHT)
    }
