# Find the smallest number divisible by numbers 1 thru 20

primes = [2, 3, 5, 7, 11, 13, 17, 19]

def check_divisible(high, number):
    if number == 0:
        return False
    for num in range(2,high):
        if number % num != 0:
            return False
    return True

def main(high_num):
    res = 0
    factor = 1
    for prime in primes:
        if prime > high_num:
            break
        factor *= prime
    while True:
        if check_divisible(high_num, res):
            return res
        else:
            res += factor

print main(20)
