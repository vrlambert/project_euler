from datetime import datetime

num = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime(year, month, 1).weekday() == 6:
            num += 1

print num
