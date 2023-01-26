# Get the mean of an array
# Parameters or Edge Cases:
    # input will be an array of integers
    # array will never be empty
# Return:
    # the mean or average of the input array
# Examples:
    # get_average([2, 2, 2, 2]) # 2
    # get_average([1, 5, 87, 45, 8, 8]) # 25
    # get_average([2,5,13,20,16,16,10]) # 11
    # get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]) # 11
# Psuedo Code:
    # return the sum of the array divided by the length of the array
    # use // to divide and only return the integer do not round up or down

# my answer and best practices and most clever
def get_average(marks):
    # return the sum of the array divided by the length of the array
    # use // to divide and only return the integer do not round up but could round down
    return sum(marks)//len(marks)

# my answer refactored implicit lambda one liner
get_average = lambda n: sum(n)//len(n)

print(get_average([2, 2, 2, 2])) # 2
print(get_average([1, 5, 87, 45, 8, 8])) # 25
print(get_average([2,5,13,20,16,16,10])) # 11
print(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7])) # 11

# importing numpy for .mean()
import numpy

def get_average(marks):
    return int(numpy.mean(marks))

# same as above but implicit one line function return
get_average = lambda m: int(__import__("numpy").mean(m))

# import both numpy and math
import math
import numpy
def get_average(marks):
    number =  numpy.average(marks)
    return math.floor(number)

# for loop
def get_average(marks):
    sum = 0
    for x in marks:
        sum = sum + x
    num = len(marks)
    ans = sum/num
    return int(ans)

# another for loop
import math
def get_average(marks):
    sum = 0
    for num in marks:
        sum += num
    total = sum / len(marks)
    return math.floor(total)

# one line for loop
def get_average(marks):
    return sum(n for n in marks) // len(marks)

def get_average(marks):
    sum = 0
    for num in marks:
        sum += num
    total = sum / len(marks)
    return math.floor(total)

# importing from statistics
from statistics import mean
def get_average(array):
    return int(mean(array))

# importing statistics in line
def get_average(marks):
    return int(__import__("statistics").mean(marks))

# using trunc()
from math import trunc
def get_average(marks):
    return trunc(sum(marks)/len(marks))