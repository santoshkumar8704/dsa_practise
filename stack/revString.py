def reverseString(S):
    stack = []
    rev = ""
    for s in S:
        stack.append(s)
    while stack:
        rev += stack.pop()
    return rev
S= input()
print(reverseString(S))