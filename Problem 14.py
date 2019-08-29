# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


x = 1  # keeps track of numbers
Lcounter = 0  # keeps track of Longest Counter
LongChain = 0  # Keep track of the current number which produces the largest chain


while x <= 1000000:  # runs all number under one million
    temp = x
    counter = 0  # resets counter
    while temp > 1:  # runs until reaches 1
        if temp % 2 == 0:  # runs even sequence
            temp = int(temp / 2)
        else:  # runs odd sequence
            temp = 3*temp + 1
        counter = counter + 1  # increments counter
    if counter > Lcounter:  # if produces a larger chain store new number and length of chain
        Lcounter = counter
        LongChain = x
    x = x+1

print(LongChain)  # prints number under one million that makes the longest chain
