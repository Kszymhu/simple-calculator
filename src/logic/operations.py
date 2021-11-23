"""Contains the `Operations` class.
"""
from math import log
from logic.operation import Operation, Associativity

def addition(num_a: float, num_b: float) -> float:
    """Adds `num_a` to `num_b`.
    Neither `num_a` nor `num_b` need to fit any additional requirements.
    """
    return num_a + num_b

def subtraction(num_a: float, num_b: float) -> float:
    """Subtracts `num_b` from `num_a`.
    Neither `num_a` nor `num_b` need to fit any additional requirements.
    """
    return num_a - num_b

def multiplication(num_a: float, num_b: float) -> float:
    """Multiplies `num_a` and `num_b`.
    Neither `num_a` nor `num_b` need to fit any additional requirements.
    """
    return num_a * num_b

def division(num_a: float, num_b: float) -> float:
    """Divides `num_a` by `num_b`.
    Raises ValueError if `num_b` == 0.
    """
    if num_b == 0:
        raise ValueError

    return num_a / num_b

def modulo(num_a: float, num_b: float) -> float:
    """Calculates the remainder of division of `num_a` by `num_b`
    Raises ValueError if `num_b` == 0.
    """
    if num_b == 0:
        raise ValueError

    return num_a % num_b

def exponentiation(num_a: float, num_b: float) -> float:
    """Raises `num_a` to the power of `num_b`.
    Raises ValueError if both `num_a` and `num_b` are 0.
    """

    if num_a == 0 and num_b == 0:
        raise ValueError

    return num_a ** num_b

def root(num_a: float, num_b: float) -> float:
    """Calculates the `num_a`-degree root of `num_b`.
    Raises ValueError if:
    1. `num_a` < 0
    2. `num_b` == 0.
    """

    if num_a < 0 or num_b == 0:
        raise ValueError

    return num_b ** (1 / num_a)

def logarithm(num_a: float, num_b: float) -> float:
    """Calculates the base-`num_a` logarithm of `num_b`.
    Raises ValueError if:
    1. `num_b` is 0 and `num_a` is non-zero
    2. `num_a` is 0 and `num_b` is non-zero
    3. `num_b` is 1
    4. `num_a` <= 0
    5. `num_b` < 0
    """
    value_error_conds = [
        num_b == 0 and num_a != 0,
        num_a == 0 and num_b != 0,
        num_b == 1,
        num_a <= 0,
        num_b < 0
    ]

    if True in value_error_conds:
        raise ValueError

    return log(num_b, num_a)


IDENTIFIERS_VS_OPERATIONS = {
        "+": Operation(addition, 1, Associativity.LEFT),
        "-": Operation(subtraction, 1, Associativity.LEFT),
        "*": Operation(multiplication, 2, Associativity.LEFT),
        "/": Operation(division, 2, Associativity.LEFT),
        "%": Operation(modulo, 2, Associativity.LEFT),
        "^": Operation(exponentiation, 3, Associativity.RIGHT),
        "root": Operation(root, 3, Associativity.RIGHT),
        "log": Operation(logarithm, 3, Associativity.RIGHT)
    }
