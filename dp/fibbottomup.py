def fib(n):
    if n <=1 :
        return n
    res = [0]* (n+1)
    res[1] = 1
    for i in range(2,n+1):
        res[i] = res[i-1] + res[i-2]
    return res[n]
n = 3
print(fib(n))