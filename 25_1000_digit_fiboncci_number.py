
start = [1,1]
n = 2
while True:
    next_fib = start[n - 2] + start[n - 1]
    if len(str(next_fib)) == 1000:
        print n+1 #off by one error
        break
    start.append(next_fib)
    n += 1
