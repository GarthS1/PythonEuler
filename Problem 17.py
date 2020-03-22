ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
tens = ["", "","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numToWord(n):
  one = n % 10
  n = n  / 10 
  ten = n % 10
  n = n / 10
  hundred = n % 10
  word = ones[hundred] + tens[ten] + ones[one] 
  return word


print(numToWord(120))