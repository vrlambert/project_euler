# It's prime sieve time!
from math import sqrt, floor

# the first one is something I wrote without doing research
def first_primes(limit):
    """generates primes up to the given limit"""
    yield 2
    for test_prime in range(3, limit + 1, 2):
        if is_prime(test_prime):
            yield test_prime

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

# this works fairly quickly to get the right answer,
# but is definitely not optimized
print list(first_primes(1000000))[10000]

# note this method would work better with a sieve of eratosthnes or counting
# the primes on the way up
