"""Contains the `generate_rpn` function."""


from typing import Union
from operations import IDENTIFIERS_VS_OPERATORS as OPERATIONS
from math_operator import Associativity

Token = Union[str, float]

def generate_rpn(tokens: list[Token]) -> list[Token]:
    """Rearranges `tokens` into the reverse polish notation."""
    output = []
    op_stack = []

    for token in tokens:

        if isinstance(token, float):
            output.append(token)

        elif token in {"abs", "ln", "sqrt"}:
            op_stack.append(token)

        elif token in OPERATIONS.keys():

            while (
                len(op_stack) > 0
                and op_stack[-1] != "("
                and OPERATIONS[op_stack[-1]].precedence() >= OPERATIONS[token].precedence()
                and OPERATIONS[token].associativity ==  Associativity.LEFT
            ):
                output.append(op_stack.pop())

            op_stack.append(token)

        elif token == "(":
            op_stack.append(token)

        elif token == ")":
            while (
                len(op_stack) > 0
                and op_stack[-1] != "("
            ):
                output.append(op_stack.pop())
            op_stack.pop()

            if(len(op_stack) > 0 and op_stack[-1] in {"abs", "ln", "sqrt"}):
                output.append(op_stack.pop())

    while len(op_stack) > 0:
        output.append(op_stack.pop())

    return output
