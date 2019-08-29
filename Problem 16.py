# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?


sumx = 0  # stores sum
x = str(2**1000)

for n in x:  # calculates sum of all digits
	sumx += int(n)

print(sumx)
