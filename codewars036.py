"""
Calculate Average
Parameters or Edge Cases:
    inputs will be an array of integers greater than 0
    empty arrays should return 0
Return:
    the average as a float of the array of integers
Examples:
    (find_average([1, 2, 3]), 2)
Psuedo Code:
    if the array length is 0 return 0
    else sum the array and divide the sum by the length of the array
    return the float number
"""
# my answer
def find_average(numbers):
    # if the array length is 0 return 0
    if len(numbers) == 0:
        return 0
    # sum the array and divide the sum by the length of the array
    else:
        # return the float number
        return sum(numbers)/len(numbers)

print(find_average([1, 2, 3])) # 2
print(find_average([])) # 0

# my answer lambda one liner
find_average = lambda numbers: 0 if len(numbers) == 0 else sum(numbers)/len(numbers)

# best practices and most clever
# here they are using if array to check if the array is null or empty
def find_average(array):
    return sum(array) / len(array) if array else 0

# submitted as 2nd best practices but should NOT WORK YOU CAN'T DIVIDE BY 0!!!!! or can you?
def find_average(numbers):
   return sum(numbers)/len(numbers)

# try except block taking into account divide by zero
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

# brute force for loop
def find_average(numbers):
    result = 0
    for x in range(len(numbers)):
        result += numbers[x]
    return result/len(numbers)

# importing mean to find the average
from statistics import mean as find_average

# importing math
import math
def find_average(numbers):
    return math.fsum(numbers)/len(numbers)

# using numpy for mean
import numpy as np
def find_average(numbers):
    return np.mean(numbers)

# importing functools for reduce()
import functools

def find_average(numbers):
    a = functools.reduce(lambda x, y: x+y, numbers)
    b = len(numbers)
    return a / b

# I love the class builds
# here they are using the class build to take in acount if the array is not null or empty
def find_average(array):
    if not array:
        return 0

    class SafeFloat(object):
        def __init__(self, val):
            super(SafeFloat, self).__init__()
            self.val = val

        def __eq__(self, float_val):
            # let me fix your comparisons..
            def isclose(a, b):
                return abs(a - b) < 0.00000001
            return isclose(self.val, float_val)

        def __str__(self):
            return str(self.val)

    from numpy import mean
    return SafeFloat(mean(array))