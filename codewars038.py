"""
Find the Maximum and Minimum Values of a List
Parameters or Edge Cases:
    inputs will be an array with integers
    integers can be negative or positive

    TWO FUNCTIONS!!!! DO NOT COMBINE INTO ONE FUNCTION!!!
    one function will be the min and the other the max vaule of the input array
Return:
    the interger value of the min value of the array and the max value of the array respectively with the two functions
Examples:
    def fixed_min_cases():
        test.assert_equals(minimum([-52, 56, 30, 29, -54, 0, -110]), -110)
        test.assert_equals(minimum([42, 54, 65, 87, 0]), 0)
        test.assert_equals(minimum([1, 2, 3, 4, 5, 10]), 1)
        test.assert_equals(minimum([-1, -2, -3, -4, -5, -10]), -10)
        test.assert_equals(minimum([9]), 9)

    def fixed_min_cases():
        test.assert_equals(maximum([-52, 56, 30, 29, -54, 0, -110]), 56)
        test.assert_equals(maximum([4,6,2,1,9,63,-134,566]), 566)
        test.assert_equals(maximum([5]), 5)
        test.assert_equals(maximum([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
        test.assert_equals(maximum([9]), 9)

Psuedo Code:
    take in the array and use min() to find the min value and return it for minimum function
    take in the array and use max() to find the min value and return it for maximum function

"""
# my answer and best practices
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

print(minimum([-52, 56, 30, 29, -54, 0, -110])) # -110
print(minimum([42, 54, 65, 87, 0])) # 0
print(minimum([1, 2, 3, 4, 5, 10])) # 1
print(minimum([-1, -2, -3, -4, -5, -10])) # -10
print(minimum([9])) # 9

print(maximum([-52, 56, 30, 29, -54, 0, -110])) # 56
print(maximum([4,6,2,1,9,63,-134,566])) # 566
print(maximum([5])) # 5
print(maximum([534,43,2,1,3,4,5,5,443,443,555,555])) # 555
print(maximum([9])) # 9

# my answer refactored lambdas
minimum = lambda arr: min(arr)
maximum = lambda arr: max(arr)

# most clever
# sorted() returns a new sorted list and [0] takes the first index while [-1] takes the last index
def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]

# same idea but using index location based on length for max value
import math

def min(arr):
    return (sorted(arr))[0]

def max(arr):
    return (sorted(arr))[len(arr)-1]

# sorted(reverse=True) sorts the array in ascending then reverses it 
def min(arr):
    arr.sort()
    return arr[0]

def max(arr):
    arr.sort(reverse=True)
    return arr[0]

# brute force for loops
def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high

# least amount of code used
minimum = min
maximum = max

# using .reduce()
from functools import reduce # the answer did not have this listed but it NEEDS the import to work in production for VSCode IDE

def min(arr):
    return reduce(lambda x,y: x if x < y else y, arr)
def max(arr):
    return reduce(lambda x,y: x if x > y else y, arr)

# using builtins for function naming conflicts NOT CURRENLTY WORKING
import builtins

def min(arr):
    return builtins.min(arr)

def max(arr):
    return builtins.max(arr)

# nested for loops sort comparing each element value if previous element is greater then swap them
def bouble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def minimum(arr):
    return bouble_sort(arr)[0]

def maximum(arr):
    return bouble_sort(arr)[len(arr)-1]