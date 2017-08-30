"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
high = 1000

def easy_solution(high):
    result = 0
    for i in range(high):
        if i%3==0 or i%5==0:
            result += i
    return result

print(easy_solution(high))


# The solution given py project euler
def sum_divible_by(n):
    p = (high-1) // n
    return n * p * (p + 1) // 2

print(sum_divible_by(3) + sum_divible_by(5) - sum_divible_by(15))
