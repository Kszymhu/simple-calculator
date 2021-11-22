"""Contains the `Operations` class.
"""

from math_operator import Operation, Associativity

def addition(stack: list) -> None:
    """Pops two elements of the stack, adds them, and pushes the result.
    Elements don't need to fit any additional requirements.
    """
    num_b = stack.pop()
    num_a = stack.pop()
    stack.append(num_a + num_b)

def subtraction(stack: list) -> None:
    """Pops two elements of the stack, subtracts the first one from the second one,
    then pushes the result.
    Elements don't need to fit any additional requirements.
    """
    num_b = stack.pop()
    num_a = stack.pop()
    stack.append(num_a - num_b)

def multiplication(stack: list) -> None:
    """Pops two elements of the stack, multiplies them, then pushes the result.
    Elements don't need to fit any additional requirements.
    """
    num_b = stack.pop()
    num_a = stack.pop()
    stack.append(num_a * num_b)

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

def exponentiation(stack: list) -> None:
    """Pops two elements of the stack,
    raises the second one to the power of the first one, then pushes the result.
    Elements don't need to fit any additional requirements.
    """
    num_b = stack.pop()
    num_a = stack.pop()
    stack.append(num_a ** num_b)

def root(stack: list) -> None:
    """Pops two elements of the stack,
    calculates the `second popped element`th root of the first one, then pushes the result.
    Raises ValueError if the first popped element is negative, or when the second element is 0.
    """
    num_b = stack.pop()
    num_a = stack.pop()
    if num_b < 0 or num_a == 0:
        raise ValueError

    stack.append(num_b ** (1 / num_a))

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
        "+": Operation(addition, 1, Associativity.LEFT),
        "-": Operation(subtraction, 1, Associativity.LEFT),
        "*": Operation(multiplication, 2, Associativity.LEFT),
        "/": Operation(division, 2, Associativity.LEFT),
        "%": Operation(modulo, 2, Associativity.LEFT),
        "^": Operation(exponentiation, 3, Associativity.RIGHT),
        "root": Operation(root, 3, Associativity.RIGHT)
    }
