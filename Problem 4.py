# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 1
b = 1
total = 0  # stores the largest palindrome


while a < 1000:  # keeps first number in range of 1000
    while b < 1000:   # keeps second number in range of 1000
        x = a*b  # calculates product
        k = x  # stores x in k and f for future use
        f = x
        c = 0  # counter for how many digits a number has
        n = 1  # counter for how many times the palindrome loop has run
        z = 0  # stores the palindrome number
        while x != 0:  # calculates the amount of digits in x
            x = int(x/10)
            c = c + 1
        while k != 0:  # continues until k is zero
            y = k % 10  # y is the number for the last digit in x
            k = k - y  # removes the last digit to 0
            z = z + (y * (10 ** (c-n)))  # puts the number in the opposite digit slot
            k = round(k/10)  # reduces the digits by 1 for future use
            n = n + 1
        if z == f:  # checks if palindrome
            if z > total:  # checks if larger palindrome then previous one saved
                total = z
        b = b + 1  # increase by 1
    b = 1  # reset to 1
    a = a + 1
print(total)
