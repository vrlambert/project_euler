
def factorial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

# reduce makes this nice and clean
print reduce(lambda x, y: int(x) + int(y), list(str(factorial(100))))
