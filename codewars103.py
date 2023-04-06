# Multiples of 3 or 5
# Parameters or Edge Cases:
    # inputs will be integers and can be negative
# Return:
    # the sum of all the multiples of 3 or 5 below and not including the input integer
# Examples:
# 4 => 3
# 6 => 8
# 15 => 45

# Pseudocode:
    # declare an empty array
    # create an array from range starting at 0 stopping at input integer and stepping by 1
    # check if each integer is divisible by 3 and not 5, 5 and not 3, or 15
    # if yes then push that iteration to the empty array
    # sum the new array
    # return the sum

# my answer
def solution(number):
    total = []
    for i in range(0, number, 1):
        if (i % 3 == 0 and i % 5 != 0) or (i % 5 == 0 and i % 3 != 0) or (i % 15 == 0):
            total.append(i)
    return sum(total)

# my answer refactored implicit return
solution = lambda n: sum([i for i in range(0, n) if (i % 3 == 0 and i % 5 != 0) or (i % 5 == 0 and i % 3 != 0) or (i % 15 == 0)])

print(solution(4)) # 3
print(solution(6)) # 8
print(solution(15)) # 45

# best practices and most clever
# no need for start or step in range but range will not include stop in the new list
# Here they use no remainder for 3 or no remainder for 5 meaning when both cases are met, the element is only counted once.
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# 2nd most clever
# I recognize the Gauss Theorem
# checking how many divisors of 3s, 5s and 15s exist and using them in Gauss Theorem
def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result

# highly rated
# Also using Gauss Theorem but with documentation
import math
def solution(number):
#     Uses identity sum of all numbers up to n = n*(n+1)/2
#     Uses identity sum of all numbers divisible by d less then k = d * sum of all numbers up to k/d
#     O(3) complexity
    number = number - 1
    three = 3 * math.floor(number / 3) * (math.floor(number / 3) + 1) / 2
    five = 5 * math.floor(number / 5) * (math.floor(number / 5) + 1) / 2
    fifteen = 15 * math.floor(number / 15) * (math.floor(number / 15) + 1) / 2
    return int(three + five - fifteen)

# using itertools.chain() to iterate by 3s 5s
def solution(number):
  import itertools
  return sum(set(itertools.chain(range(0, number, 3), range(0, number, 5))))


# using | instead of or
def solution(number):
  return sum(set(range(0,number,3)) | set(range(0,number,5)))

# using a separate function for Gauss Theorem
from math import floor

def sum_to_n(n):
    return n * (n + 1) / 2

def sum_of_multiples(k, n):
    return k * sum_to_n(floor(n / k))

def solution(number):
    number = number - 1
    return (sum_of_multiples(3, number) + 
        sum_of_multiples(5, number) - 
        sum_of_multiples(3 * 5, number))

# creating a class
# class object is used for grabbing the input number -1 for the endpoint number to be divided by the sum() function which returns the divisors
# The final line of solution() returns those divisors added by base of 3 or 5 but minus the base of 15 eliminating duplicates.
class Multiples:
    def __init__(self, maximum):
        self.maximum = maximum

    def sum(self, base):
        count = self.maximum // base + 1
        last = base * (count - 1)
        return count * last // 2

def solution(number):
    multiples = Multiples(number - 1)
    return multiples.sum(3) + multiples.sum(5) - multiples.sum(15)