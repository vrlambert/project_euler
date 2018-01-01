from PE_useful import eratosthenes

# Upper limit of primes to check, problem needs 1000000
limit = 1000000

primes = eratosthenes(limit)
print 'primes done'

def consec_prime_sum(p):
    """
    Takes in a prime number, p, and returns the consecutive primes that sum to
    the value, if possible. Otherwise returns None
    """

    # End one before the prime, the prior prime can't start the sequence
    end = primes.index(p) - 1
    # Iterate through all the primes up to the target prime as starting points
    for start in range(end):
        sequence = []
        i = 1
        while sum(sequence) < p:
            sequence = primes[start:start + i]
            i += 1
        if sum(sequence) == p:
            # The first one found is always the longest (it has smaller numbers)
            return sequence

    return []


def main1(limit):
    """
    initial semi brute force solution
    """
    max_length = 0
    max_p = 1

    for p in primes:
        if p > limit:
            break
        seq = consec_prime_sum(p)
        if len(seq) > max_length:
            max_length = len(seq)
            max_p = p

    print max_p, max_length

def main2(limit):
    max_len = 1

    # iterate through all primes
    for p1 in primes:

        # break if the prime can't be a part of the max length
        if p1 > limit / max_len:
            break

        # initialize lengths
        length = 0
        total = 0

        # iterate through all following primes
        for p2 in primes[primes.index(p1):]:
            # add to the total
            total += p2

            # if the total is higher than the limit, break
            if total > limit:
                break

            # one longer streak
            length += 1

            # If it's the longest, keep track of it
            if total in primes and length > max_len:
                start = p1
                max_len = length
                high = total

    print high, start, max_len

main2(limit)
