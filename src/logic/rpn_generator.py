"""Contains the `generate_rpn` function."""

from tokenizer import Token
from operations import IDENTIFIERS_VS_OPERATIONS as OPERATIONS
from operation import Associativity

def generate_rpn(tokens: list[Token]) -> list[Token]:
    """Rearranges `tokens` into the reverse polish notation, using the shunting yard algorithm.
    This code is *definitely not* a butchered version of pseudocode from https://en.wikipedia.org/wiki/Shunting-yard_algorithm.
    """
    output = []
    op_stack = []

    for token in tokens:

        if isinstance(token, float):
            output.append(token)

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

    while len(op_stack) > 0:
        output.append(op_stack.pop())

    return output
