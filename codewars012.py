"""
Parameters or Edge Cases:
    input will be
Return:
    an integer of the sum of each element squared 
Examples:
    [1, 2, 2] # 9 because 1^2 + 2^2 + 2^2 = 9
    (square_sum([1,2]), 5)
    (square_sum([0, 3, 4, 5]), 50)
    (square_sum([]), 0)
    (square_sum([-1,-2]), 5)
    (square_sum([-1,0,1]), 2)
Psuedo Code:
    declare a variable represting the total
    loop through each element in the array and multiply it by itself then add it to the declared variable
    return the variable
"""

# my answer
def square_sum(numbers):
    # declare a variable represting the total
    sum = 0
    # loop through each element in the array and multiply it by itself then add it to the declared variable
    for i in range(len(numbers)):
        numbers[i] *= numbers[i]
        sum += numbers[i]
    # return the variable    
    return sum

print(square_sum([1,2])) # 5
print(square_sum([0, 3, 4, 5])) # 50
print(square_sum([])) # 0
print(square_sum([-1,-2])) # 5
print(square_sum([1,2,2])) # 9
print(square_sum([-1,0,1])) # 2

# best practices and most clever
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

# one liner lambda sum the list of each element to the power of 2 for each element in the list
square_sum = lambda n: sum(e**2 for e in n)

# cleaner brute force for loop
"""
def square_sum(numbers):
	res = 0
	for num in numbers:
   		res = res + num*num
    return res
"""

# using sum() map() and lambda function
def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))    

# loop through the list with each element to the power of 2
def square_sum(numbers):
    return sum([x**2 for x in numbers])

# create a new list and add the squared values to the new list then sum the new list
def square_sum(numbers):
    result = []
    for sqr in numbers:
        result.append(sqr ** 2)
    return sum(result)

# importing numpy
"""
import numpy
def square_sum(numbers):
    return sum(numpy.array(numbers) ** 2)
"""

# importing functools to use reduce()
"""
import functools
def square_sum(numbers):
    return functools.reduce(lambda x, y: x + y**2, numbers, 0)
"""

# using sum() square()
"""
from numpy import square
def square_sum(numbers):
    return sum(square(numbers))
"""

# using repeat()
from itertools import repeat
def square_sum(numbers):
    return sum(map(pow, numbers, repeat(2)))

# descriptive comments
def square_sum(numbers):
    #your code here
    s = []                 #empty list to store the result from loop below
    for x in numbers:     #loop through argument value
        x = x**2         #square value and assign
        s.append(x)     #append new value to list s
    return sum(s)     #sum of list after loop finishes

# using sum() pow()
def square_sum(numbers):
    return sum(pow(i, 2) for i in numbers)

# using a while loop
def square_sum(numbers):
    lol = 0
    hassu = len(numbers)
    while hassu > 0:
        lol = numbers[hassu - 1] ** 2 + lol
        hassu = hassu - 1
    return lol