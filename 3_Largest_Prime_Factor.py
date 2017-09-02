"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import floor, sqrt

number = 13195
number_high = 600851475143

############## Initial Solution #####################

def get_factors(n):
    # Returns all the factors of n
    top = floor(sqrt(n))
    return [x for x in range(2, top + 1) if n % x==0]

def is_prime(n):
    if len(get_factors(n)) == 0:
        return True
    else:
        return False

def get_prime_factors(n):
    result = []
    for factor in get_factors(n):
        if is_prime(factor):
            result.append(factor)
    return result

def largest_prime_factor(n):
    return max(get_prime_factors(n))

############# After reading PE solution ################
def reduce_factor(n, factor):
    # simple function to divide out all instances of a factor
    while n % factor == 0:
        n /= factor
    return n

def largest_prime_factor_2(n):
    # function returns the largest prime factor by
    # dividing out all smaller factors completely first

    # First check if two is a factor and then divide out all twos
    if n % 2 == 0:
        lastfactor = 2
        n = reduce_factor(n, 2)
    else:
        lastfactor = 1

    # Next check from 3 and count upward by two
    factor = 3
    maxfactor = sqrt(n) # factor can't be higher than the sqrt
    while n > 1 and factor <= maxfactor:
        if n % factor == 0:
            n /= factor
            lastfactor = factor
            n = reduce_factor(n, factor)
            maxfactor = sqrt(n)
        factor += 2

    if n == 1:
        return lastfactor
    else:
        return n

if __name__ == '__main__':
    print(largest_prime_factor_2(number_high))
