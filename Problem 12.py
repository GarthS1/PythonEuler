# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

import math


def is_prime(n):  # function for finding a prime number (not written by me)
    if n == 1:
        return False
    elif n < 4:  # 2 and 3 are prime
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:  # anything under 9 not divisible by 2 is prime
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.sqrt(n)  # n rounded to the greatest integer r so that r*r<=n
        f = 5
        while f <= r:
            if n % f == 0:
                return False  # (and step out of the function)
            if n % (f + 2) == 0:
                return False  # (and step out of the function)
            f = f + 6
        return True  # (in all other cases)


triangle_number = 0
counter = 1
divisors = 0

while divisors <= 500:  # max amount of divisors is 499 before the loop ends
    divisors = 0
    triangle_number += counter  # finds next triangle number
    counter += 1
    if not is_prime(triangle_number):  # checks if prime to save time
        i = 1
        temp = math.sqrt(triangle_number)
        # unique divisors only go up to the square and has a corresponding divisor on the other side
        while i <= temp:
            if triangle_number % i == 0:
                divisors += 2  # add two for both corresponding divisors
            i += 1

print(triangle_number)
