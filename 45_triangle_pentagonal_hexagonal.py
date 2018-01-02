# Find the next number after 40755 that is triangular, hexagonal, and pentagonal

# Turns out all hexagonal numbers are triangular, so just check those

def main():
    n_hex = 144 # 144
    n_pent = 165 # 165
    pentag = 1
    while n_hex < 100000:
        hexag = n_hex * (2 * n_hex - 1)

        while pentag < hexag:

            pentag = n_pent * (3 * n_pent - 1) / 2
            n_pent += 1
        if pentag == hexag:
            print hexag, pentag
        n_hex += 1


main()
