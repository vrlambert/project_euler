

coin_values2 = [1, 2, 5, 10, 20, 50, 100, 200]
coin_values = [200, 100, 50, 20, 10, 5, 2, 1]

def get_value(nums):
    result = 0
    for i, value in enumerate(coin_values):
        result += nums[i]*value
    return result

def brute_force():
# gets the right answer, 73682 in 30 seconds
# there has to be a better way
    results = []
    # start at 8 which are the 8 solutions of only one type of coin
    total = 8

    # skip coin one because there is only one permutation using that coin
    # iterate through all the possible values of each other coin
    for c2 in range(2):
        for c3 in range(4):
            for c4 in range(10):
                for c5 in range(20):
                    for c6 in range(40):
                        for c7 in range(100):
                            for c8 in range(200):
                                num = (0, c2, c3, c4, c5, c6, c7, c8)
                                value = get_value(num)
                                # skip all the values that are over the limit
                                if value > 200:
                                    break
                                # increment the total if it's the right amount
                                elif value == 200:
                                    # results.append(num)
                                    total += 1
                                    # print total, num, get_value(num)
    return total

amount = 200
def ways(target, avc):
    # base case, if we are at the smallest coin return 1 way
    if avc < 1: return 1
    # initialize a counter for the number of ways
    res = 0
    while target >= 0:
        res += ways(target, avc - 1)
        target -= coin_values2[avc]
    return res

print ways(amount, 7)
