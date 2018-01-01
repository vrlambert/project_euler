from PE_useful import eratosthenes

limit = 10000

primes = eratosthenes(limit)

odd_composites = set([])

for p in primes:
    num = 1
    while p + 2 * num ** 2 < limit:
        to_add = p + 2 * num ** 2
        if to_add % 2 == 1:
            odd_composites.add(to_add)
        num += 1

for n in range(3,limit,2):
    if n in primes:
        continue
    if n not in odd_composites:
        print n
