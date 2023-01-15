"""
How good are you really?
Parameters or Edge Cases:
    inputs will be an array of integers and an integer
    array will not be empty
Return:
    boolean true if sum of array is less than the integer else false
Examples:
    (better_than_average([2, 3], 5), True)
    (better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75), True)
    (better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69), True)
    (better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50), False)
    (better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21), False)
Psuedo Code:
    Use the math comparison for implicit return of boolean true false for a math statement
    if the sum of the input array divided by array length is less than the input integer return true else false
"""
# my answer similar to best practices and most clever but reverse statement
def better_than_average(class_points, your_points):
    # Use the math comparison for implicit return of boolean true false for a math statement
    # if the sum of the input array is less than the input integer return true else false but implicitly with a math statement
    return sum(class_points) / len(class_points) < your_points

# my answer one line lambda implicit return
better_than_average = lambda c, y: sum(c) / len(c) < y

print(better_than_average([2, 3], 5)) # True
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)) # True
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)) # True
print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)) # False
print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21)) # False

# best practices and most clever 
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# importing statistics to use .mean()
import statistics
def better_than_average(class_points, your_points):
    return your_points > statistics.mean(class_points)

# same as above but not using dot notation .mean() instead mean()
from statistics import mean

def better_than_average(class_points, your_points):
    return your_points > mean(class_points)

# using *args for the inputs
def better_than_average(*args):
    return args[1] > sum(*args) / (len(args[0]) + 1.0)

# using a while loop
def better_than_average(class_points, your_points):
    i = 0
    totalP = 0
    while i < len(class_points):
        totalP += class_points[i]
        i += 1
    totalP = totalP / len(class_points)
    if totalP > your_points:
        return False
    else:
        return True

# one line lambda with the import in the lambda 
better_than_average = lambda c,y: __import__("numpy").mean(c)<y