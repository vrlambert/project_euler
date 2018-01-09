from math import sqrt
filename = '42_words.txt'


def is_triangular(x):
    n = (sqrt(8*x + 1) - 1) / 2.
    if n > int(n):
        return False
    else:
        return int(n)

def word_value(s):
    s = s.upper()
    return sum(map(lambda s: ord(s) - 64, list(s)))

with open(filename, 'r') as f:
    strings = f.read()

words = sorted(strings.replace('"','').split(','))

total = 0
for word in words:
    if is_triangular(word_value(word)):
        total += 1

print total
