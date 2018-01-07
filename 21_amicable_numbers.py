from PE_useful import get_prime_factors

limit = 10000

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

total = 0
for n in range(limit + 1):
    digit_sum = sum(get_factors(n)[:-1])
    if digit_sum == n:
        continue
    if sum(get_factors(digit_sum)[:-1]) == n:
        total += n

print total
