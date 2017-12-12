# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# algorithm and improvements came from the page above
def eratosthenes(limit):
    to_check = [2] + [n for n in range(3, limit+1, 2)]
    p = 2
    p_index = 0
    flagged = set()
    while p ** 2 < limit:
        for check in range(p ** 2, limit + 1, p):
            flagged.add(check)

        for i, value in enumerate(to_check[p_index + 1:], start = p_index + 1):
            if value not in flagged:
                p = value
                p_index = i
                break
        else:
            break

    return set(to_check) - flagged

limit = 2000000
# print eratosthenes(int(limit))
print sum(eratosthenes(int(limit)))
# 142913828922
# runs in 4.4s
