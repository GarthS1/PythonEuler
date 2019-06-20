# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

a = 1
b = 1
c = 1

while a < 1000:  # has to be less than 1000
    b = a + 1  # since b has to be bigger than a start from a + 1
    while b < 1000-a:  # has to be less than 1000-a
        c = 1000-b-a
        if a ** 2 + b ** 2 == c ** 2:  # checks if Pythagorean Triplet
            print(a*b*c)
        b += 1
    b = 1  # resets b back to 1
    a += 1


