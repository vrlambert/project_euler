upper = 1000000

# generator form
def collatz(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            yield n / 2
            n = n / 2
        else:
            yield 3 * n + 1
            n = 3 * n + 1

# simple recursive form, not fast enough
def collatz_rec(n, steps = []):
    steps.append(n)
    if n == 1:
        return steps
    elif n % 2 == 0:
        return collatz_rec(n / 2, steps)
    else:
        return collatz_rec(3 * n + 1, steps)


paths = {}
# recursive form memoized
# we could capture the count instead of the steps which would be faster
# but it could be nice to look at the steps one day
def collatz_rec_memo(n, steps = ()):
    # if n has already been seen
    if n in paths:
        # the rest of the path is added
        full = steps + paths[n]

        # only add save if there is more info to be captured for a new number
        if steps:
            paths[steps[0]] = full
        # return the full path
        return full

    # if we don't have a complete path, add the latest step to the path
    steps += (n,)

    # if n is one, we are done
    if n == 1:
        paths[steps[0]] = steps
        return steps

    # if it's even, divide by two and return
    elif n % 2 == 0:
        return collatz_rec_memo(n / 2, steps)

    # if it's odd, 3*n+1 is the next step
    else:
        return collatz_rec_memo(3 * n + 1, steps)

def main(limit):
    max_length = 0
    max_number = 0
    for integer in range(1, limit + 1):
        length = len(list(collatz_rec_memo(integer)))
        # print integer, length
        if length > max_length:
            max_length = length
            max_number = integer
    print max_number, max_length

if __name__ == '__main__':
    main(upper)
