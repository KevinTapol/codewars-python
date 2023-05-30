# N-th Fibonacci
"""
I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that, when given a number n (n >= 1 ), returns the nth number in the Fibonacci Sequence.

For example:

   nth_fib(4) == 2
Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.


After some research I learned the Fibonacci Sequence is where each number is the sum of the two that precede it. Starting at 0,1,1,2,3,5,8,13,21,34,55,89,144, etc
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
"""
# Return:
"""
    the element at the input integer n position of the Fibonacci sequence
"""
# Examples:
"""
    1 => 0
    2 => 1
    3 => 1
    4 => 2
    5 => 3
    6 => 5
    7 => 8
"""
# Pseudocode:
"""
    # declare an array named fib of integers of the Fibonacci Sequence starting with 0 and 1
    # generate an array with the length of the input n 
    # iterate through the array and append the sum of the current index element with the next index element to the array
    # return the element at the index of n -1
    
"""

# my answer
# def nth_fib(n):
#     # declare an array named fib of integers of the Fibonacci Sequence starting with 0 and 1
#     fib = [0,1]
#     # generate an array with the length of the input n 
#     for i in range(n):
#         # iterate through the array and append the sum of the current index element with the next index element to the array
#         fib.append(fib[i] + fib[i+1])
#     # return the element at the index of n -1
#     return fib[n-1]

# print(nth_fib(1)) # 0
# print(nth_fib(2)) # 1
# print(nth_fib(3)) # 1
# print(nth_fib(4)) # 2
# print(nth_fib(5)) # 3
# print(nth_fib(6)) # 5
# print(nth_fib(7)) # 8

# best practices
# declaring variables representing the first and second values of the Fibonacci Sequence instead of declaring an array with the same values
# then they are generating an array with the length of n-1 with each iteration in the same line reassigning a as b and b as the sum of a and b
# this way the final result of a will be the element at n-1 of the Fibonacci Sequence without generating an array of more than 2 values.
def nth_fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

# using recursion for values at indexes greater that 1
# this is a lot of recursions for high numbers
def nth_fib(n):
  if n==1:
      return 0
  elif n==2:
      return 1
  else:
      return nth_fib(n-1)+nth_fib(n-2)
  
# same idea as above but using 1 statement for inputs of 0 and 1
def nth_fib(n):
    if n <= 2:
        return n-1
    return nth_fib(n-1) + nth_fib(n-2)

# one line version of both previous answers
def nth_fib(n):
  return 0 if n==1 else 1 if n in [2,3] else (nth_fib(n-2)+nth_fib(n-1))

# while loop version of my answer
def nth_fib(n):
    if n == 1:
        return 0
    fib = [0,1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return(fib[-1])

# importing math for sqrt() but doesn't work past values of 70
from math import sqrt
def nth_fib(n):
  n = n - 1
  Phi = (1 + sqrt(5))/2
  phi = (1 - sqrt(5))/2
  
  return int(((Phi**n)-(phi**n))/sqrt(5))

#Using Binet's Formula to speed things up
def nth_fib(n):
    Phi = (pow(5, 0.5) + 1)/2
    phi = Phi - 1
    n -= 1
    return round((pow(Phi, n) - pow(-phi, n))/pow(5, 0.5))