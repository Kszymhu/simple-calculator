"""
Boy don't try to front, I-I
Know just, just, what you are, are-are
Boy don't try to front, I-I
Know just, just, what you are, are-are
You say I'm crazy
(You!) I got your crazy
(You!) You're nothing but a
(You!) Tokenizer
"""

from math import pi, e
from typing import Union
from logic.operations import IDENTIFIERS_VS_OPERATIONS

IDENTIFIERS_VS_CONSTANTS = {
    "pi": pi,
    "e": e
}

Token = Union[str, float]

def is_valid_float(candidate: str) -> bool:
    """Checks if `candidate` represents a valid float."""
    try:
        float(candidate)
        return True
    except ValueError:
        return False

def tokenize(raw_tokens: list[str]) -> list[Token]:
    tokens = []

    for raw_token in raw_tokens:
        if is_valid_float(raw_token):
            tokens.append(float(raw_token))

        elif raw_token in IDENTIFIERS_VS_CONSTANTS.keys():
            tokens.append(IDENTIFIERS_VS_CONSTANTS[raw_token])

        elif raw_token in IDENTIFIERS_VS_OPERATIONS.keys() or raw_token in {"(", ")"}:
            tokens.append(raw_token)

        else:
            raise ValueError()

    return tokens
