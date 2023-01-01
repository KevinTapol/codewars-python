"""
Invert Values
Parameters or Edge Cases:
    inputs will be an array of integers that can be negative or positive
Return:
    an array of the additive inverse of each integer input meaning the value that when added results in 0
Examples:
        invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        invert([]), [])
Psuedo Code:
    take in the input array and create a shallow copy and multiply each element by -1
    return the new array
"""

# my answer 2nd best practices and most clever
def invert(a):
    return list(map(lambda x: x * -1, a))

print(invert([1,2,3,4,5])) # [-1,-2,-3,-4,-5]
print(invert([1,-2,3,-4,5])) # [-1,2,-3,4,-5]
print(invert([])) # []

# my answer refactored to lambda one liner
invert = lambda a: list(map(lambda x: x * -1, a))

# best practices and most clever
# brute force for loop 
def invert(lst):
    return [-x for x in lst]

# for loop but multiplying by -1 instead of adding a negative sign to the x
# I prefer this because of the clear multiply by -1 for psuedo code
def invert(lst):
   return [i*-1 for i in lst]

# while loop
def invert(lst):
    i = 0
    inv = []
    while i < len(lst):
        inv.append(lst[i] * -1)
        i += 1
    return inv

# for loop but declaring an empty array and adding the inverses to it
def invert(lst):
    lst2=[]
    for num in lst:
        lst2.append(num*-1)
    return lst2

# using __neg__ to get the inverse value of each element
def invert(lst):
    return list(map(int.__neg__, lst))

# importing operator to use .neg 
import operator

def invert(lst):
    return list(map(operator.neg, lst))

# importing numpy instead of using map()
"""
import numpy
def invert(lst):
    return list(numpy.array(lst) * -1)
"""