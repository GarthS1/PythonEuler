a = 1
b = 1
total = 0


while a < 1000:
    while b < 1000:
        x = a*b
        k = x
        f = x
        c = 0
        n = 1
        z = 0
        while x != 0:
            x = int(x/10)
            c = c + 1
        while k != 0:
            y = k % 10
            k = k - y
            z = z + (y * (10 ** (c-n)))
            k = round(k/10)
            n = n + 1
        if z == f:
            if z > total:
                total = z
        b = b + 1
    b = 1
    a = a + 1
print(total)



