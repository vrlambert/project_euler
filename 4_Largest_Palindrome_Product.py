# start with a basic brute force approach
import time

def is_palindrome(string):
    string = str(string)
    return string == string[::-1]

def try_one():
    high_res = -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            if i*j > high_res:
                if is_palindrome(i*j):
                    high_res = i*j

    return high_res
# answer is 906609

# Faster brute force solution, with hints from the PE pdf
def try_two():
    high_res = -1

    for i in reversed(range(100, 1000)):
        for j in reversed(range(i, 1000)):
            if i*j > high_res:
                if is_palindrome(i*j):
                    high_res = i*j
    return high_res

t1 = time.time()
print try_one(), time.time()-t1

# This one is three times faster!
t2 = time.time()
print try_two(), time.time()-t2
