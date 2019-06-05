a = 9
b = 9

while a < 10:
    while b < 10:
        x = a*b
        k = x
        z = 0
        n = 0
        while x != 0:
            y = x % (pow(10, (n+1)))
            x = x - y
            z = z + y * pow(10, (2-n))
            n = n + 1
        if z == k:
            print(z)
        else:
            print(z, "a")
        b = b + 1
    b = 1
    a = a+1
