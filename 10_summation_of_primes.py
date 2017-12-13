# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# algorithm and improvements came from the page above
from math import sqrt, floor
limit = 2000000

def eratosthenes_old(limit):
    """Returns a set of all primes below the given limit"""
    to_check = [2] + [n for n in range(3, limit+1, 2)]
    p = 2
    p_index = 0
    flagged = set()
    while p ** 2 < limit:
        for check in range(p ** 2, limit + 1, 2 * p):
            flagged.add(check)

        for i, value in enumerate(to_check[p_index + 1:], start = p_index + 1):
            if value not in flagged:
                p = value
                p_index = i
                break
        else:
            break

    return set(to_check) - flagged

def eratosthenes(limit):
    sieve = [None, None] + [False] * (limit - 1)
    crosslimit = int(floor(sqrt(limit)))
    for n in range(4, limit + 1, 2):
        sieve[n] = True
    for n in range(3, crosslimit):
        if not sieve[n]:
            for m in range(n*n, limit, 2*n):
                sieve[m] = True
    return [i for i, x in enumerate(sieve) if x is False]
# print eratosthenes_old(int(limit))
# print sum(eratosthenes_old(int(limit)))
# 142913828922
# runs in 4.4s

# new method using the structure provided in the
print sum(eratosthenes(limit))
# runs in < 1s
