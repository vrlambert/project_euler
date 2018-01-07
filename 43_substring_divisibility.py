from itertools import permutations
from PE_useful import eratosthenes

test = 1406357289

def divisible(n):
    primes = eratosthenes(18)
    s = str(n)
    for i, p in enumerate(primes,1):
        if int(s[i:i + 3]) % p != 0:
            return False
    else:
        return True

total = 0
for s in permutations(str(test)):
    n = int(''.join(s))
    if divisible(n):
        print n
        total += n

print 'total:', total
