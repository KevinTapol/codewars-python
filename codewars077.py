# You're a square!
# Parameters or Edge Cases:
    # inputs will be integers and can be negative
    # inputs will not be empty
    # will inputs be 
# Return:
    # boolean true if input is a perfect square else false meaning we can use truthy falsy
# Examples:
    # -1  =>  false
    #  0  =>  true
    #  3  =>  false
    #  4  =>  true
    # 25  =>  true
    # 26  =>  false
# Pseudo Code:
    # if the value is less than 0 return False because a perfect square root cannot be negative
    # if the value is 0 return true because dividing by 0 should cause a problem
    # iterate from 0 to input number n and if that iteration times itself is equal to n return true
    # outside of the for loop return false
    # This answer works but timed out due to large input numbers not previously stated for parameters or edge cases. So I decided to import math and use math.sqrt() as an alternative

    # alternate answer using math.sqrt()
    # import math for math.sqrt()
    # if the input value is greater or equal to 0 and the square root return of the input is an integer return true else false


# my answer brute force for loop 
# this times out due to test cases that are very large numbers
# so I decided to do an import math answer
def is_square(n):  
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        # for i in reversed(range(n//2)): I did this to start backwards and at half input value of integer in an attempt for timeout large integers but it still timed out
        for i in range(n):
            if i*i == n:
                return True
        return False

# my answer using math.sqrt()
import math as m
def is_square(n):
    if n >=0 and m.sqrt(n) % 1 == 0:
        return True
    else:
        return False
    
# my answer refactored implicit return lambda truthy in line import for math.sqrt()
is_square = lambda n: n >= 0 and __import__("math").sqrt(n) %1 == 0

print(is_square(-1)) # False
print(is_square(0)) # True
print(is_square(3)) # False
print(is_square(4)) # True

# best practices and most clever
# very similar to my refactored truthy answer but I don't understand the semicolon in Python instead of C# or JavaScript
# comment about ; u can do use it when u wanna put all statements in one line : if n > 0 : n+=1 ; k-=7 hope that helps
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

# very very clever using **0.5 as input to the power of 0.5 instead of using square root of 2
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

# same idea but using pow() instead of **
def is_square(n):    
    return n >= 0 and pow(n, 0.5) % 1 == 0

# using .is_integer() for boolean truthy return
import math

def is_square(n):    

    if n < 0:
        return False

    sqrt = math.sqrt(n)
    
    return sqrt.is_integer()

# try except block instead of greater than or equal to 0
import math
def is_square(n):    
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False
    
# interesting using int() instead of modulus % taking the integer value of n to the power of 0.5 to the power of 2 returns the value n
def is_square(n):    
    if n>=0:
        if int(n**.5)**2 == n:
            return True
    return False

# same as above but truthy using int() to check for remainder instead of modulus % 
import math
def is_square(n):
  return n >= 0 and int(math.sqrt(n)) ** 2 == n

# importing only sqrt from math
from math import sqrt

def is_square(n):    
    return n>=0 and sqrt(n).is_integer()

# interesting using int() to get the whole number and subtract it by same maths without int()
import math

def is_square(n):
    if n < 0:
        return False
    return (int(math.sqrt(n)) - math.sqrt(n)) == 0

# get the square root of the input
# round down then multiply the rounded down by itself to see if it equals input
# using truthy boolean as return
import math

def is_square(n):
    if n < 0:
        return False
    r = math.sqrt(n)
    r = math.floor(r)
    return r * r == n

# while loop
def is_square(n): 
    if n < 0:
        return False
    if n == 0:
        return True
    k = 1
    while True:
        k_square = k**2
        if k_square > n:
            return False
        if k_square == n:
            return True
        k = k + 1