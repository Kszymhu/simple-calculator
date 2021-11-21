from operations import Operations, IDENTIFIERS_VS_OPERATORS

"""
class Operations:
    
    @staticmethod
    def power(stack: list):
        b = stack.pop()
        a = stack.pop()
        stack.append(a ** b)

    @staticmethod
    def multiply(stack: list):
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)

    @staticmethod
    def divide(stack: list):
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)

    @staticmethod
    def add(stack: list):
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)

    @staticmethod
    def subtract(stack: list):
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

    @staticmethod
    def identity(stack: list, number):
        stack.append(number)

OPERATIONS = {
    "^": Operations.power,
    "*": Operations.multiply,
    "/": Operations.divide,
    "+": Operations.add,
    "-": Operations.subtract
}
"""

def calculate(tokens):
    stack = []
    for token in tokens:
        if token in IDENTIFIERS_VS_OPERATORS.keys():
            #OPERATIONS[token](stack)
            operator = IDENTIFIERS_VS_OPERATORS[token]
            operator.operation()(stack)
        else:
            #Operations.identity(stack, token)
            stack.append(token)
    
    return stack[0]