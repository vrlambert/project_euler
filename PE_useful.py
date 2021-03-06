# collection of useful functions I wrote along the way
from math import floor, sqrt

def is_prime(number):
    """Checks if a number is prime"""
    if number <= 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        for test_num in range(5, int(floor(sqrt(number))) + 1, 6):
            if number % test_num == 0:
                return False
            if number % (test_num + 2) == 0:
                return False
    # return true if we didn't find any divisors
    return True

def eratosthenes(limit):
    sievebound = (limit - 1) / 2
    sieve = [None,] + [False] * sievebound
    crosslimit = int(floor(sqrt(limit) - 1) / 2)
    # for n in range(4, limit + 1, 2):
    #     sieve[n] = True
    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sievebound + 1, 2 * i + 1):
                sieve[j] = True
    return [2] + [2 * i + 1 for i, x in enumerate(sieve) if x is False]

def get_prime_factors(n, primes = None):
    if n < 2:
        return [0]
    if primes is None:
        limit = n
        primes = eratosthenes(int(floor(sqrt(limit))))
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

def get_number_factors(n, primes = None):
    if n < 2:
        return 0
    _ , factors = zip(*get_prime_factors(n, primes))
    return reduce(lambda x, y: x * (y + 1), factors, 1)

def get_factors(n):
    p_factors = get_prime_factors(n)
    if len(p_factors) == 1:
        return [1, n]
    prime_divisors, multiplicity = zip(*p_factors)

    factors = []
    def find_factors(prime_divisors, multiplicity, current_divisor = 0, current_result = 1):
        if current_divisor == len(prime_divisors):
            factors.append(current_result)
            return

        for i in range(multiplicity[current_divisor] + 1):
            find_factors(prime_divisors, multiplicity, current_divisor + 1, current_result)
            current_result *= prime_divisors[current_divisor]

    find_factors(prime_divisors, multiplicity)
    return sorted(factors)

def word_value(s):
    """Returns the word value, where the value is the sum of the letters
    position in the alphabet. Takes in the word as a string"""
    s = s.upper()
    return sum(map(lambda s: ord(s) - 64, list(s)))
