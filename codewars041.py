"""
Beginner-Reduce but Grow
Parameters or Edge Cases:
    input will be an array of integers
    intput array will never be null or empty
Return:
    the product of the integers
Examples:
    [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
    [6 , [1, 2, 3]],
    [16, [4, 1, 1, 1, 4]],
    [64, [2, 2, 2, 2, 2, 2]],
Psuedo Code:
    loop through the array and multiply the element integers together
    return the product
"""
# my answer and best practices
def grow(arr):
    prod = 1
    for e in arr:
        prod *=e
    return prod

# my answer refactored importing reduce one line lambda implicit return
from functools import reduce 
grow = lambda arr: reduce(lambda acc, c: acc * c, arr)

print(grow([1, 2, 3, 4])) # 24
print(grow([1, 2, 3])) # 6
print(grow([4, 1, 1, 1, 4])) # 16
print(grow([2, 2, 2, 2, 2, 2])) # 64

# most clever importing reduce() method for array math
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# one liner
from math import prod as grow

# how to add import into a lambda one liner
grow = lambda a: __import__("functools").reduce(lambda x,y: x*y, a)

# importing math for product method prod()
import math
def grow(arr):
    return math.prod(arr)

# importing reduce() and mul
from functools import reduce
from operator import mul

def grow(arr):
    return reduce(mul, arr, 1)

# importing only mul
from operator import mul

def grow(arr):
    return reduce(mul, arr)

# using eval() to evaluate the math expression
def grow(arr):
    return eval('*'.join([str(i) for i in arr]))

# lambda eval()
grow=lambda arr: eval("*".join(map(str,arr)))