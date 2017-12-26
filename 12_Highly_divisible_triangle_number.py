# Triangle numbers can be generated with n(n+1) / 2
from PE_useful import eratosthenes
from math import sqrt, floor

factors = 500

def main(n_factors):
    n = 1
    triangle = 0
    factors = 0
    prime_limit = 1000
    primes = update_primes(prime_limit)
    while factors < n_factors:
        triangle = n * (n + 1) / 2
        if triangle > prime_limit:
            prime_limit *= 2
            primes = update_primes(prime_limit)
        factors = get_number_factors(triangle, primes = primes)
        n += 1

    return triangle, factors

def update_primes(limit):
    return eratosthenes(int(floor(sqrt(limit))))

def get_factors(n):
    pass

def get_number_factors(n, primes = None):
    if n < 2:
        return 0
    _ , factors = zip(*get_prime_factors(n, primes))
    return reduce(lambda x, y: x * (y + 1), factors, 1)

def get_prime_factors(n, primes = None):
    if n < 2:
        return 0
    if primes is None:
        primes = update_primes(n)
    factors = [0 for _ in primes]
    for i, prime in enumerate(primes):
        if prime > n:
            break
        while n % prime == 0:
            n /= prime
            factors[i] += 1
    result = [(i, j) for i, j in zip(primes, factors) if j > 0]
    if n > 1:
        result.append((n, 1))
    return result

if __name__ == '__main__':
    print main(factors)
