a = 1
b = 1

while a < 3:
    while b < 3:
        x = a*b
        k = x
        z = 0
        n = 0
        while x != 0:
            y = x % 10
            x = x - y
            z = z + (y * (pow(10, n)))
            n = n + 1
        if z == k:
            print(z)
        b = b + 1
    b = 1
    a = a+1
