from math import sqrt
limit = 10000

def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()

def pent(n):
    return n * (3 * n - 1) / 2


n = 2
while n < limit:
    p1 = pent(n)
    for m in range(1,n):
        p2 = pent(m)
        if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
            print p1, p2, p2 - p1
            break
    n += 1
