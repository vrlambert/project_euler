# Find the largest sum path through the triange, trivial with this solution
with open('67_triangle.txt', 'r') as f:
    triangle = ''
    for line in f.readlines():
        triangle += line

def split_int(s):
    l = s.split()
    return [int(s) for s in l]
t1 = triangle.split('\n')[:-1]
t = map(split_int,t1)

for i, row in enumerate(reversed(t[:-1])):
    for j, _ in enumerate(row):
        lower = t[len(t) - i - 1][j:j+2]
        row[j] += max(lower)

print t[0][0]
