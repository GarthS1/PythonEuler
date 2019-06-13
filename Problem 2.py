f1 = 1  # first term in Fibonacci sequence
f2 = 2  # second term in Fibonacci sequence
total = 0

while f2 <= 4000000:  # stops from going over 4 million
    if f2 % 2 == 0:  # checks if even-valued
        total += f2
    temp = f2  # store the second term to a temporary term
    f2 += f1  # adds the second and first term together to get your new second term
    f1 = temp  # replaces the first term with second term

print(total)
