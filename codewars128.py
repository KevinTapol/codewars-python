# Is a number prime?
"""

Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""
# Parameters or Edge Cases:
"""
    inputs will be integers and can be negative or positive
    inputs can be large enough to time out if using brute force solutions or recursion
"""
# Return:
"""
    boolean true if the input is a prime number else false
"""
# Examples:
"""
    0 =>  False, "0  
    1 =>  False, "1  
    2 =>  True, "2  
    73 => True, "73 
    75 => False, "75 
    -1 => False, "-1 
"""
# Pseudocode:
"""
    after reading the discussion, you can brute force the solution ending at the square root of the input which is the same as input**.5 so I will use a brute force while loop

    if the input integer is less than 2 return False
    declare a variable count set it equal to 2 
    while the declared variable count is less than the square root of the input or the input to the power of 1/2 
        if the input divided by the current iterator returns no remainder return False
        add 1 to the current count
    outside of the while loop return True
"""

# my answer
def is_prime(num):
    # if the input integer is less than 2 return False
    if num < 2:
        return False
    # declare a variable count set it equal to 2
    count = 2
    # while the declared variable count is less than the square root of the input or the input to the power of 1/2
    while count <= num**.5:   
        # if the input divided by the current iterator returns no remainder return False 
        if num%count == 0:
            return False
        # add 1 to the current count
        count += 1
    # outside of the while loop return True 
    return True 

print(is_prime(0)) # False
print(is_prime(1)) # False
print(is_prime(2)) # True
print(is_prime(73)) # True
print(is_prime(75)) # False
print(is_prime(-1)) # False

# best practices and most clever
#  x >>= y works the same as x = x >> y
# This is the Miller-Rabin test for primes, which works for super large n
# As appanoid pointed out: this solution is incorrect because it will occasionally return True for very large numbers that aren't prime.

import random

def even_odd(n):
    s, d = 0, n
    while d % 2 == 0:
          s += 1
          d >>= 1
    return s, d

def Miller_Rabin(a, p):
    s, d = even_odd(p-1)
    a = pow(a, d, p)
    if a == 1: return True
    for i in range(s):
        if a == p-1: return True
        a = pow(a, 2, p)
    return False

def is_prime(p):
    if p == 2: return True
    if p <= 1 or p % 2 == 0: return False
    return all(Miller_Rabin(random.randint(2,p-1),p) for _ in range(40))

# WHAT!!! THERE'S A METHOD TO TEST FOR PRIME!!!
# The Python way? Import a c-based module and let it do the heavy lifting?
import gmpy2

def is_prime(num):
  return gmpy2.is_prime(num) if num > 0 else False

# same answer further refactored for codewars only
from gmpy2 import is_prime

# besides the import answer above, this is one of the few answers that does not use square root or to the power of 1/2
# here they use the input divided by the current iterator as the stop
def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i <= num / i:
        if num % i == 0:
            return False
        i += 1
    return True

# using recursion and setting recursion limit
# clever but only for codewars
import sys

sys.setrecursionlimit(100000)

def is_prime(num, divisor=2):
    if num < 2:
        return False
    
    if divisor ** 2 > num:
        return True
    
    if num % divisor == 0:
        return False
    
    return is_prime(num, divisor + 1)

# implicit return one line lambda
is_prime = lambda n: n > 2 and n % 2 and not any(n % x == 0 for x in range(3, int(n ** .5) + 1, 2)) or n == 2

# while loop importing math for sqrt() instead of **.5
from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 

# brute force for loop
def is_prime(num):
  if num==2 or num==3: return True
  if num<2 or num%2==0 or num%3==0: return False
  for i in range(5,int(num**.5)+2,2):
      if num%(i-1)==0: return False
      if num%(i+1)==0: return False
  return True
  #second more efficient version, as I remembered that every prime >3
  #is derived from 6k+/1 with k positive integer.


# clever to use truthy falsy for modulus comparison
def is_prime(num):
    if num <= 1:
        return  False 
    elif num ==  2:
        return True
    elif num % 2 == 0:
        return  False 
    return sum([i for i in range(1, int(num  ** 0.5 + 1), 2) if num % i == 0]) == 1