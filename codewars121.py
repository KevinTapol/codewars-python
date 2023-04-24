# Does my number look big in this?
"""A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10)."""
# Parameters or Edge Cases:
    # Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
# Return:
    # true if the input integer individual digits to the power of the number of digits sum is equal to the input integer else false
# Examples:
    # 153 => 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 => True
    # 1652 => 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938 => False
# Pseudocode:
    # convert the input integer into a string and split up the string into an array with each string digit at an index converted back into an int
    # iterate through each digit taking it to the power of the length of the array 
    # sum the elements
    # if the sum is equal to the input return true else false

# my answer 
def narcissistic( value ):
    # convert the input integer into a string and split up the string into an array with each string digit at an index converted back into an int
    x = [int(e) for e in str(value)]
    # iterate through each digit taking it to the power of the length of the array
    y = list(map(lambda e: e**len(str(value)), x))
    return True if sum(y) == value else False

# my answer refactored truthy
def narcissistic( value ):
    return sum([int(e)**len(str(value)) for e in str(value)]) == value

# my answer refactored implicit return
narcissistic = lambda v: sum([int(e)**len(str(v)) for e in str(v)]) == v
    
print(narcissistic(153))

# best practices and most clever
# only difference from my answer is they used a tuple instead of a list for array format
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

# here they declared variables for reused code with a for element in input
def narcissistic( value ):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)

# brute force while loop
def narcissistic( value ):
    v = value
    l = len(str(value))
    s = 0
    while v > 0:
        s += (v % 10)**l
        v //= 10

    return s == value