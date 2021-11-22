"""Contains the `main` function. Run this file if you want to experience
the pure joy of having your calculations done for you.
"""

from logic.rpn_generator import generate_rpn
from logic.rpn_solver import calculate
from logic.tokenizer import tokenize

def main():
    """Calculator entry point."""

    tokens_raw = input().split(" ")
    tokens = tokenize(tokens_raw)
    rpn = generate_rpn(tokens)
    result = calculate(rpn)
    print(result)

if __name__ == "__main__":
    main()
