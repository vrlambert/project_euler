# Triangle numbers can be generated with n(n+1) / 2
from PE_useful import eratosthenes
from math import sqrt, floor

factors = 500

def main(n_factors):
    n = 1
    triangle = 0
    factors = 0
    while factors < n_factors:
        triangle = n * (n + 1) / 2
        factors = get_number_factors(triangle)
        n += 1

    return triangle, factors



def get_factors(n):
    pass

def get_number_factors(n):
    if n < 2:
        return 0
    _ , factors = zip(*get_prime_factors(n))
    return reduce(lambda x, y: x * (y + 1), factors, 1)

def get_prime_factors(n):
    if n < 2:
        return 0
    prime_limit = int(floor(sqrt(n)))
    primes = eratosthenes(prime_limit)
    factors = [0 for _ in primes]
    for i, prime in enumerate(primes):
        while n % prime == 0:
            n /= prime
            factors[i] += 1
    result = [(i, j) for i, j in zip(primes, factors) if j > 0]
    if n > 1:
        result.append((n, 1))
    return result

if __name__ == '__main__':
    print main(factors)
