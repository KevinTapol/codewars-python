"""
Grasshopper Summation
Parameters or Edge Cases:
    input will be an integer
Return:
    return the sum of the input integer's number from 0 to the integer stepping by 1
    the input will always be an integer greater than 0
Examples:
    (summation(1), 1)
    (summation(8), 36)
    (summation(22), 253)
    (summation(100), 5050)
    (summation(213), 22791)
Psuedo Code:
    declare a variable for total
    loop through starting at 0 to the input number and add it to the total
    return the total
"""

# my answer
def summation(num):
    # declare a variable for total
    total = 0
    # loop through starting at 0 to the input number and add it to the total
    for i in range(num + 1):
        total += i
    # return the total    
    return total

"""
# best practices 
# DEPRECATED! xrange() is only used in Python 2 but range() is used in Python 3
# xrange() evaluates the generator object only when required and not when the generator function is created. Therefore it is faster in implementation than range().

def summation(num):
    return sum(xrange(num + 1))

use range() instead
def summation(num):
    return sum(range(num + 1))
"""
# most clever
# used Triangular Number (n + 1) * n / 2
def summation(num):
    return (1+num) * num / 2

# lambda Triangular Number 
summation=lambda n:n*-~n>>1

# for loop in one line
def summation(num):
    return sum([x for x in range(num+1)])

# using range() with 2 parameters
def summation(num):
    return sum(range(1,num+1))

# using range() with 1 parameter
def summation(num):
    return sum(range(num + 1))

# for loop with range() using 2 parameters
def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total

# using a while loop
def summation(num):
    fac = 0 
    i = 0 
    while i < num:
        i += 1
        fac = fac + i
    return fac

# calling the function on itself
def summation(num):
    if num > 1:
       return num + summation(num - 1)
    return 1