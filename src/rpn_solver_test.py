from operations import IDENTIFIERS_VS_OPERATORS

def calculate(tokens):
    stack = []
    for token in tokens:
        if token in IDENTIFIERS_VS_OPERATORS.keys():
            operator = IDENTIFIERS_VS_OPERATORS[token]
            operator.operation()(stack)
        else:
            stack.append(token)
    
    return stack[0]
