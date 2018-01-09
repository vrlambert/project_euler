from PE_useful import eratosthenes

def is_pandigital(n):
    s = str(n)
    for digit in range(1, len(s) + 1):
        if str(digit) not in s:
            return False
    else:
        return True

limit = 10000000
primes = eratosthenes(limit)
for p in primes:
    if is_pandigital(p):
        print p

# luckily the answer is < 10,000,000
