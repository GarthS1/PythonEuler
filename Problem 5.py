# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 2520  # can start here because any number smaller than this won't meet half the requirements

while x % 20 or x % 19 or x % 18 or x % 17 or x % 16 or x % 15 or x % 14 or x % 13 or x % 12 or x % 11:
    # covers all possible divisors
    x = x + 20  # increment by 20 as it has to be divisible by 20

print(x)
