# Function 2 - squaring an argument
"""
Now you have to write a function that takes an argument and returns the square of it.
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
    inputs will never be emtpy
"""
# Return:
"""
    return the square of the input
"""
# Examples:
"""
    2 => 4
    50 => 2500
    1 => 1
"""
# Pseudocode:
"""
    square the input and return the result
"""

# my answer, best practices and most clever
def square(n):
    return n**2

# my answer refactored implicit return
square = lambda n: n**2

print(square(2)) # 4
print(square(50)) # 2500
print(square(1)) # 1

# using math pow()
def square(n):
    return pow(n, 2)

# multiplying by itself
def square(n):
    return n*n

# import numpy one liner for square
from numpy import square