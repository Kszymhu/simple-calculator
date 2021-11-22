from __future__ import annotations
from typing import Union

Token = Union[str, float]

def check_if_valid_float(candidate: str) -> bool:
    """Checks if `candidate` represents a valid float.
    """
    try:
        float(candidate)
        return True
    except ValueError:
        return False

def tokenize_expression(expression: str) -> list[Token]:
    """Splits `expression` into a list of tokens."""
    return [
        float(x) if check_if_valid_float(x)
        else x
        for x in expression.split(" ")
    ]

def main() -> None:
    expression = input()
    tokens = tokenize_expression(expression)

    print(tokens)

if __name__ == "__main__":
    main()
    