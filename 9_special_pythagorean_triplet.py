# generating pythagorean triples from eulers method
# https://en.wikipedia.org/wiki/Pythagorean_triple

def euler_method(m, n):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return a, b, c

def main():
    m, n = 2, 1
    while True:
        a, b, c = 1, 1, 1
        while a + b + c < 1001:
            a, b, c = euler_method(m, n)
            if a + b + c == 1000:
                return a, b, c
            m += 1
        n += 1
        m = n + 1

a, b, c = main()

print a, b, c
print a*b*c
