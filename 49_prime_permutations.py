from PE_useful import eratosthenes

primes_1 = eratosthenes(10000)
primes = primes_1[168:] # 168 is the index of the first prime over 1000, 1009


def is_permutation(n1, n2, n3):
    s1 = set(str(n1))
    s2 = set(str(n2))
    s3 = set(str(n3))
    return s1 == s2 & s2 == s3 & s1 == s3


def main():
    for p1 in primes:
        for p2 in primes[primes.index(p1) + 1:]:
            diff = p2 - p1
            p3 = p2 + diff
            if p3 in primes and is_permutation(p1, p2, p3):
                print p1, p2, p3, diff


main()
