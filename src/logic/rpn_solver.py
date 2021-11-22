from logic.operations import IDENTIFIERS_VS_OPERATIONS

def calculate(tokens):
    stack = []
    for token in tokens:
        if token in IDENTIFIERS_VS_OPERATIONS.keys():
            operator = IDENTIFIERS_VS_OPERATIONS[token]
            num_b = stack.pop()
            num_a = stack.pop()
            stack.append(operator.function()(num_a, num_b))
        else:
            stack.append(token)
    
    return stack[0]
