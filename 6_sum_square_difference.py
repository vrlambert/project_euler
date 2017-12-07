def sum_of_square(high):
    return sum(x**2 for x in range(high+1))

def square_of_sum(high):
    return sum(range(high+1))**2

def main1(high):
    return square_of_sum(high) - sum_of_square(high)

print main1(10)
print main1(100)
