def evaluatePrefix(exp):
    stack = []
    operators = {'+' : lambda x,y : x+y,
                 '-' : lambda x,y : y-x,
                 '*' : lambda x,y : x * y,
                 '/' : lambda x,y : y // x}
    for x in reversed(exp.split()):
        if x.isdigit():
            stack.append(x)
        elif x in operators:
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            res = operators[x](val1,val2)
            stack.append(res)
        else :
            raise ValueError('invalid token')
    if len(stack) != 1:
        raise ValueError('invalid expression')
    return stack[0]
prefix_expr = "+ * 3 4 2"
result = evaluatePrefix(prefix_expr)
print("Result of evaluating prefix expression:", result)