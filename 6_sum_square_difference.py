# initial brute force solution
def sum_of_square(high):
    return sum(x**2 for x in range(high+1))

def square_of_sum(high):
    return sum(range(high+1))**2

def main1(high):
    return square_of_sum(high) - sum_of_square(high)

print main1(10)
print main1(100)

# now with some input from the project euler pdf
def main2(high):
    sum1 = high*(high+1) / 2
    sum_sq = (2*high + 1) * (high + 1) * high / 6
    return sum1 ** 2 - sum_sq

print main2(10)
print main2(100)
