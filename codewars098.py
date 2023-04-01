# Find the next perfect square!
# Parameters or Edge Cases:
    # inputs will be integers greater than 0
# Return:
    # if the input is a perfect square return the next perfect square from the input integer 
    # else return -1
# Examples:
    # 121 --> 144
    # 625 --> 676
    # 114 --> -1 since 114 is not a perfect square
# Pseudo Code:
    # take the square root of the input number
    # if it does not return an integer return -1 
    # else return the integer + 1

# my answer
import math
def find_next_square(sq):
    if math.sqrt(sq)//1 == math.sqrt(sq)/1:
        return int((math.sqrt(sq)//1 + 1)**2)
    else:
        return -1
    
# my answer refactored implicit return 
# far from dry but it is technically an implicit return one liner
find_next_square = lambda sq: int((__import__("math").sqrt(sq)//1 + 1)**2) if __import__("math").sqrt(sq)//1 == __import__("math").sqrt(sq)/1 else -1
    
print(find_next_square(121)) # 144
print(find_next_square(625)) # 676
print(find_next_square(114)) # -1

# best practices
# instead of importing math to use sqrt take the input to the power of 0.5 input**0.5 and using .is_integer() for boolean return if the float is an integer
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

# most clever
# same using input to the power of 0.5 instead of import math for square root .sqrt() but with a one liner if else
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2

# similar to my answer but using .is_integer()
import math

def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1

# importing only the square root function from math
from math import sqrt
def find_next_square(sq):
    return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1

# checking for a remainder with modulus %
def find_next_square(sq):
    sqrt=sq**(0.5)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    return -1

# importing both square root and power for math
import math


def find_next_square(sq):
    """Return the next square if sq is a square, -1 otherwise"""
    square = math.sqrt(float(sq))
    return -1 if not square.is_integer() else math.pow(square + 1, 2)

# importing numpy to use .square() and .sqrt()
import numpy
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if(sq % numpy.sqrt(sq)==0):
        return numpy.square(numpy.sqrt(sq)+1)
    else:
        return -1
    
# using math.floor() instead of checking for remainder, int() or is_integer()
import math
def find_next_square(sq):
    if math.sqrt(sq).is_integer():
        return(int(((math.floor(math.sqrt(sq)))+1)**2))
    else:
        return -1