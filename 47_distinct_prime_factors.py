from PE_useful import get_prime_factors, eratosthenes
primes = eratosthenes(10000)

# Initialize a dict of prime factors to avoid recalculation
factors = {}
factors[2] = set([(2, 1)])
factors[3] = set(get_prime_factors(3))
factors[4] = set(get_prime_factors(4))

def distinct_factors(ns):
    """
    Takes in a set of integers and returns True if they have distinct prime
    factors. Otherwise returns false.
    """
    # Pull factors from the factors dict
    factors_list = [factors[n] for n in ns]
    all_set = set([])

    # Keep track of all independent factors so far and return false if there
    # is a match
    for factor in factors_list:
        if len(all_set & factor) > 0:
            return False
        all_set |= factor
    else:
        return True

def main(number):
    # start at 5
    n = 5
    while True:
        # calculate the factors for n
        factors[n] = set(get_prime_factors(n, primes = primes))
        # Get the numbers n thru n-i where i is the number of numbers desired
        numbers = [n - i for i in range(number)]

        # If the factors are distinct and have the right amount
        if distinct_factors(numbers) and \
            all([len(factors[i]) == number for i in numbers]):

            # We found the answer, print it and break
            for num in numbers:
                print num, list(sorted(factors[num]))
            break
        n += 1

main(4)
