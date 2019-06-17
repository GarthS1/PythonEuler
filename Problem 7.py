# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

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


counter = 6  # prime counter
n = 13  # number to start counting from

while counter < 10001:
    n += 2  # can increment by 2 as any even number (besides 2) isn't prime
    if is_prime(n):
        counter += 1
print(n)

