# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?


sumx = 0
x = pow(2, 1000)

while x > 0:
    sumx = sumx + x % 10
    x = int(x - (x % 10))
    x = int(x / 10)

print(sumx)
print(x)
