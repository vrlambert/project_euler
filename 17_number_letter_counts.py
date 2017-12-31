# add the number of letters for numbers 1 - 1000 (no spaces or hyphens)

# First define some numbers
base_numbers = ['one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine']
teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
base_tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
             'seventy', 'eighty','ninety']
h = 'hundredand'
t = 'onethousand'

# initialize total letters
total_letters = 0

# Calculate the base sums for each group and print them (for curiousity)
base_sum = sum([len(s) for s in base_numbers])
print 'base sum', base_sum

teen_sum = sum([len(s) for s in teen])
print 'teen sum', teen_sum

ten_sum = sum([len(s) for s in base_tens])
print 'ten sum', ten_sum

# total letters from the hundreds place minus three for no first 'and'
hundred_sum = len(h) * 100 - 3

#######################################################

# Now we move on to how many times each should be counted

# Ones place
# Base sum shows up 9 times per 100 * ten times under 1000
total_letters += base_sum * 9 * 10

# Tens place
# 10-19 added once for each hundred (ten times)
total_letters += teen_sum * 10

# Add each ten place one hundred times (ten times for each hundred)
total_letters += ten_sum * 10 * 10

# Add the hundred sum nine times
total_letters += hundred_sum * 9

# base number also occurs before 100 from 100 - 999, adds it another 100 times
total_letters += base_sum * 100

# Now add one thousand
total_letters += len(t)

print 'total', total_letters
