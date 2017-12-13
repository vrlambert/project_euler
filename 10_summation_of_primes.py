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

# print eratosthenes_old(int(limit))
# print sum(eratosthenes_old(int(limit)))
# 142913828922
# runs in 4.4s

# version written using project euler provided tips
def eratosthenes(limit):
    sievebound = (limit - 1) / 2
    print sievebound
    sieve = [None,] + [False] * sievebound
    crosslimit = int(floor(sqrt(limit)) - 1) / 2
    # for n in range(4, limit + 1, 2):
    #     sieve[n] = True
    for i in range(1, crosslimit):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sievebound + 1, 2 * i + 1):
                sieve[j] = True
    return [2] + [2 * i + 1 for i, x in enumerate(sieve) if x is False]

# new method using the structure provided in the
res = eratosthenes(limit)
print sum(res)
# runs in 0.317s
