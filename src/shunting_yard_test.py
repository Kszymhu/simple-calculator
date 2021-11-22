import rpn_solver_test
import operations
import math_operator

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
    print(f"Tokens: {tokens}")

    output = []
    operators = []

    for token in tokens:
        print(f"Processing token: {token}.")

        if check_if_valid_float(token):
            print("Token is a number, pushing into output.")
            output.append(float(token))

        elif token in {"abs", "ln", "sqrt"}:
            print("Token is a function, pushing into operator stack.")
            operators.append(token)

        elif token in operations.IDENTIFIERS_VS_OPERATORS.keys():
            print("Token is an operator")

            if len(operators) > 0:
                while (
                    len(operators) > 0
                    and operators[-1] != "("
                    and operations.IDENTIFIERS_VS_OPERATORS[operators[-1]].precedence_level() >= operations.IDENTIFIERS_VS_OPERATORS[token].precedence_level()
                    and operations.IDENTIFIERS_VS_OPERATORS[token].associativity == math_operator.MathOperator.Associativity.LEFT
                ):
                    print(f"Operator {operators[-1]} has higher or equal precedence as {token},\
transferring it to output.")
                    output.append(operators.pop())

            print("Pushing token into operator stack.")
            operators.append(token)

        elif token == "(":
            print("Token is a left parenthesis. pushing into the operator stack.")
            operators.append(token)

        elif token == ")":
            print("Token is a right parenthesis.")

            while (
                len(operators) > 0
                and operators[-1] != "("
            ):
                print(f"Transferring token {operators[-1]} into the output stack.")
                output.append(operators.pop())
            operators.pop() #hopefully a left parenthesis

            if(len(operators) > 0 and operators[-1] in {"abs", "ln", "sqrt"}):
                print(f"Transferring function token {operators[-1]} to the output stack.")
                output.append(operators.pop())

    while len(operators) > 0:
        print(f"Transferring token {operators[-1]} to the output stack.")
        output.append(operators.pop())

    print(output)

    print(f"Result: {rpn_solver_test.calculate(output)}")

if __name__ == "__main__":
    main()
