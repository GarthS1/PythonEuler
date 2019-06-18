# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

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


sum_primes = 17  # start from sum of primes under 10

for i in range(11, 2000000, 2):  # start from 11 and increment by 2 as any even number isn't prime
    if is_prime(i):
        sum_primes += i

print(sum_primes)
