# Volume of a Cuboid
# Parameters or Edge Cases:
    # given 3 input numbers greater than 0
    # inputs can be floats
# Return:
    # the product of the inputs can be a float
# Examples:
    # get_volume_of_cuboid(1, 2, 2) # 4
    # get_volume_of_cuboid(6.3, 2, 5) # 63
# Psuedo Code:
    # return the product of the inputs

# my answer best practices and most clever
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# my answer refactored implicit return one liner lambda
get_volume_of_cuboid = lambda l, w, h: l * w * h

print(get_volume_of_cuboid(1, 2, 2)) # 4
print(get_volume_of_cuboid(6.3, 2, 5)) # 63

# using reduce and *args to multiply all the inputs together then return the product as an int()
from functools import reduce

def get_volume_of_cuboid(*args):
    return int(reduce(lambda x,y: x*y, args))

# importing math for .prod() and using *args to multiply all the inputs together
import math

def get_volume_of_cuboid(*vol):
    return  math.prod(vol)

# import for loop and *args
from math import prod
def get_volume_of_cuboid(*args):
    return prod([i for i in args])