import math

x = 13195
prime = 1

while prime < x/2:
    t = isPrime(prime)
    if t and x % prime == 0:
        print(x)
    prime = prime + 1


def isPrime(n):
    if n == 1:
        return False
    elif n < 4:  # 2 and 4 are prime
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:  # anything under 9 not divisible by 2 is prime
        return True
    elif n % 3:
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

