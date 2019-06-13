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


x = 600851475143  # number to find prime factors
prime = 2

while prime < x/2:  # cancels out half the number which are indivisible
    if is_prime(prime) and x % prime == 0:  # checks that prime is prime and that it is a divider
        print(prime)
    prime = prime + 1
