def evaluatePostFix(exp):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: y - x,  # Corrected order of operands for subtraction
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: y // x}  # Corrected order of operands for division
    stack = []
    for val in exp.split():
        if val.isdigit():
            stack.append(int(val))
        elif val in operators:
            val1 = stack.pop()
            val2 = stack.pop()
            res = operators[val](val1, val2)  # Corrected order of operands
            stack.append(res)
        else:
            raise ValueError('Invalid token: ' + val)
    if len(stack) != 1:
        raise ValueError('Invalid expression')
    return stack[0]

postfix_expr = "3 4 + 2 *"
result = evaluatePostFix(postfix_expr)
print("Result of evaluating postfix expression:", result)
