"""
Sum Arrays
Parameters or Edge Cases:
    input will be an array of numbers
    array can be emtpy
    numbers can be non-integer and negative
Return:
    the sum of the numbers in the array
Examples:
    (sum_array([]), 0)
    (sum_array([1, 2, 3]), 6)
    (sum_array([1.1, 2.2, 3.3]), 6.6)
    (sum_array([4, 5, 6]), 15)
    (sum_array(range(101)), 5050)
Psuedo Code:
    if the array is empty or null return 0
    else return the sum of the elements of the array
"""

# my answer
def sum_array(a):
    # if the array is empty or null return 0
    if not a:
        return 0
    # else return the sum of the elements of the array
    else:
        return sum(a)

print(sum_array([])) # 0
print(sum_array([1, 2, 3])) # 6
print(sum_array([1.1, 2.2, 3.3])) # 6.6
print(sum_array([4, 5, 6])) # 15
# print(sum_array(range(101)) # 5050

# my answer refactored lambda
sum_array = lambda a: 0 if not a else sum(a)

# best practices
# sum() of an empty or null array automagically returns 0
def sum_array(a):
  return sum(a)

# voted most clever several lines adding each individual element of the array given the condition of the length of the array
# ex the first few lines it goes up to a length of 199
"""
def sum_array(a):
    if len(a) == 0:
	    return 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return a[0] + a[1]
    if len(a) == 3:
        return a[0] + a[1] + a[2]
    if len(a) == 4:
        return a[0] + a[1] + a[2] + a[3]
"""

# voted 2nd most clever
sum_array = sum

# brute force for loop adding each element to a declared variable
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

# while loop same as for loop but break when reaching the length of the input array
def sum_array(a):
    total = 0
    i = 0
    while i < len(a):
        total += a[i]
        i += 1
    return total

# importing functools for reduce
# here they are using reduce similar to JS reduce accumulator current value start value = 0
from functools import reduce
def sum_array(a):
    return reduce(lambda a,c: a + c, a, 0)

# another way of dealing with null or empty arrays
def sum_array(a=0):
    return sum(a) if a !=0 else 0

# testing length of the array for null or empty
def sum_array(a):
    if len(a)>0:
        return sum(a)
    return 0  

# using sum on an array but with a for loop for each element in the input array
def sum_array(a):
    return sum([i for i in a])

# importing functools and using .reduce() with a lambda
import functools as ft
def sum_array(a):
    if a == []: 
        results = 0 
    else: 
        results = ft.reduce(lambda a,b: a+b,a)
    return results

# importing from math to use .fsum()
import math

def sum_array(a):
    score=0    
    if a is None:
        return 0
    else:
        return math.fsum(a)

# using != for input array not equal array
def sum_array(a):
    if a!=[]:
        sum_array = sum(a)
    elif a==[]:
        sum_array =0
    return sum_array