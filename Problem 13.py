# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

k = open("sum.txt", 'r')  # open the file needed
theInts = []  # creates an empty list for storage
for val in k.read().split():  # creates a list for the ints
    theInts.append(int(val))
k.close()

print(sum(theInts))  # prints the sum of the list
