

filename = '22_names.txt'

with open(filename, 'r') as f:
    strings = f.read()

words = sorted(strings.replace('"','').split(','))

def convert(s):
    return sum(map(lambda s: ord(s) - 64, list(s)))

total = 0
for i, word in enumerate(words, 1):
    total += i * convert(word)

print total
