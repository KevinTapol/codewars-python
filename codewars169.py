# Find the divisors!
"""
Instructions
Output
Past Solutions
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 1
    inputs will never be null or empty
"""
# Return:
"""
    an array of integers representing the divisors for the input number
    if no divisors exists return the string 'input is a prime' where input is the integer
"""
# Examples:
"""
    15 => [3,5] 
    253 => [11,23]          
    24 => [2,3,4,6,8,12]                     
    25 => [5]
    13 => "13 is prime"
    3 => "3 is prime"
    29 => "29 is prime"
"""
# Psuedocode:
"""
    # declare an empty array result
    # iterate from 2 to the input number
    # if the input number divided by the current index has no remainder then append it to result
    # outside of the for loop if the length of result is 0 return 'input is a prime' where input is the input integer
    # else return result
"""

# my answer
def divisors(n):
    # declare an empty array result
    result = []
    # iterate from 2 to the input number
    for i in range(2,n):
    # if the input number divided by the current index has no remainder then append it to result
        if n % i == 0:
            result.append(i)
    # outside of the for loop if the length of result is 0 return 'input is a prime' where input is the input integer
    if len(result) == 0:
        return f"{n} is prime"
    # else return result
    return result

# my answer refactored
def divisors(n):
    result = [i for i in range(2,n) if n%i ==0]
    return f"{n} is prime" if len(result) == 0 else result

print(divisors(15)) # [3,5]
print(divisors(253)) # [11,23]
print(divisors(24)) # [2,3,4,6,8,12]
print(divisors(25)) # [5]
print(divisors(13)) # "13 is prime"
print(divisors(3)) # "3 is prime"
print(divisors(29)) # "29 is prime"


# best practices 
# same as my answer but using concatenation instead of f string
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

# most clever
# using or statement with %d instead of f string
def divisors(n):
    return [i for i in range(2, n) if not n % i] or '%d is prime' % n

# using .format
def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

# using math instead of modulus
import math
def divisors(n):
  o = [i for i in range(2, int(math.ceil(n/2)+1)) if n%i==0]
  return o if len(o) > 0 else "%d is prime" % n