# start with a basic brute force approach


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]

high_res = -1

for i in range(100, 1000):
    for j in range(100, 1000):
        if i*j > high_res:
            if is_palindrome(i*j):
                high_res = i*j

print high_res
# answer is 906609
