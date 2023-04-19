# Persistent Bugger
"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit."""

"""What they mean is separate the positive digit into individual digits and multiply them together. If the result is a single digit, return the number of times you had to repeat the process to get a single digit."""
# Parameters or Edge Cases:
    # inputs will be positive integers greater than 0
    # inputs will never be empty
# Return:
# Examples:
    # 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
    # 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
    # 4 --> 0 (because 4 is already a one-digit number)
# Pseudocode:
    # take the input integer and separate each digit in an array
    # multiply the elements of the array
    # if the product is a single digit return the digit
    # else repeat the process with the product as the new integer
    # repeat until the process is met

# my answer COUNT THE RECURSIONS
# I used recursion with 2 arguments passing in new arguments each recursion till a single digit of the first argument is reached. Then return the second argument as the count of recursions.
def persistence(n, t= 0):
    if len(str(n)) == 1:
        return t
    else:
        int_arr = list(map(int, [e for e in str(n)]))
        product = 1
        for i in range(len(int_arr)):
            product *= int_arr[i]
        tries = t + 1
        if len(str(product)) == 1:
            return tries
        else:
            return persistence(product, tries)

print(persistence(39)) # 3
print(persistence(999)) # 4
print(persistence(4)) # 0
print(persistence(25)) # 2

# best practices and most clever DEPRECATED!!!! Updated solution below
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

# best practices and most clever updated solution for Python3
import functools
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=functools.reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

# similar to my idea of recalling the function on itself instead of a while loop
# here they are using mul for the multiplication of the integer and reduce(product, 1)+1 to return the number of tries
from functools import reduce
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1

# using reduce for multiplication
from functools import reduce
def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(lambda a,b: a*b, [int(d) for d in str(n)])
        i += 1
    return i

# import math to achieve the same as best practices and most clever
import math

def persistence(n):
    counter = 0
    
    while n > 9:
        n = math.prod(int(x) for x in str(n))
        counter += 1
    
    return counter

# using eval instead of math.prod()
def persistence(n):
    c = 0
    while len(str(n)) >1:
        n = eval('*'.join(x for x in str(n)))
        c+=1

    return c

# very clean while loop
def persistence(n):
    y = 0
    while n > 9:
        x = 1
        for i in str(n):
            x *= int(i)
        n = x
        y += 1
    return y

# while loop based on length of the string version of the input
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

# DEPRECATED!!! I updated the answer and submitted it below
persistence = lambda n,c=0: persistence(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c

# My answer updated from the deprecated code above
persistence = lambda n,c=0: persistence(__import__('functools').reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c

# while loop DEPRECATED!!! Updated solution below
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

# UPDATED!!! from solution above
from functools import reduce
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

# using an external function to call inside the other function
def multiply_digits(n):
    product = 1
    while(n > 0):
        product *= n % 10
        n //= 10
        
    return product

def persistence(n):
    count = 0
    while(n > 9):
        n = multiply_digits(n)
        count += 1
        
    return count