# Parameters or Edge Cases:
# Return: the product of the input variables
# Examples:
# Psuedo Code: multiply the variables and return the product

# my answer and best practices
def multiply(a, b):
    return a * b
print(multiply(3,9))  #27
print(multiply(0,4))  #0
print(multiply(-2,5))  #-10
print(multiply(10,9))  #90

# most clever
# isinstance() function checks whether the object or variable is an instance of the specified class type or data type.
def multiply(a, b):
    if isinstance(a, (int, float, complex)):
        if isinstance(b, (int, float, complex)):
            return a * b

# using lambda similar to arrow function in javascript
multiply = lambda x, y: x * y

# using if else 
def multiply(a, b):
  if a is not None and b is not None:
     return a * b
  else:
      return None

# using .mul to multiply
multiply = __import__('operator').mul

# using .mul
from operator import mul as multiply

# interesting using *= to return the first input as a total
def multiply(a, b):
  a *= b
  return a

# using try except
def multiply(a, b):
    try:        
      return a * b
    except Exception as e:
      return e
    
# using math. methods
import math
def multiply(a, b):
  return a and b and math.exp(math.log(a) + math.log(b))

# using prod()
def multiply(*args):
    from math import prod
    return prod(args)