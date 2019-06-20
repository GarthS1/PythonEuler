# The sum of the squares of the first ten natural numbers is,1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
square_of_sums = 0

for i in range(101):  # goes up to 100
    sum_of_squares += i ** 2  # adds powers to sum_of_squares

for i in range(101):  # goes up to 100
    square_of_sums += i  # adds numbers to square_of_sums

square_of_sums = square_of_sums ** 2  # squares
print(square_of_sums - sum_of_squares)
