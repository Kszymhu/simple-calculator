import rpn_solver_test
from operations import IDENTIFIERS_VS_OPERATORS
from math_operator import Associativity

def check_if_valid_float(candidate: str) -> bool:
    """Checks if `candidate` represents a valid float.
    """
    try:
        float(candidate)
        return True
    except ValueError:
        return False

def main():
    tokens = input().split(" ")

    output = []
    operators = []

    for token in tokens:

        if check_if_valid_float(token):
            output.append(float(token))

        elif token in {"abs", "ln", "sqrt"}:
            operators.append(token)

        elif token in IDENTIFIERS_VS_OPERATORS.keys():

            if len(operators) > 0:
                while (
                    len(operators) > 0
                    and operators[-1] != "("
                    and IDENTIFIERS_VS_OPERATORS[operators[-1]].precedence() >= IDENTIFIERS_VS_OPERATORS[token].precedence()
                    and IDENTIFIERS_VS_OPERATORS[token].associativity ==  Associativity.LEFT
                ):
                    output.append(operators.pop())

            operators.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":

            while (
                len(operators) > 0
                and operators[-1] != "("
            ):
                output.append(operators.pop())
            operators.pop()

            if(len(operators) > 0 and operators[-1] in {"abs", "ln", "sqrt"}):
                output.append(operators.pop())

    while len(operators) > 0:
        output.append(operators.pop())

    print(output)

    print(f"Result: {rpn_solver_test.calculate(output)}")

if __name__ == "__main__":
    main()
