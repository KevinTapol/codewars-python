# Count the divisors of a number
"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to see which numbers are counted in each case.
"""
# Parameters or Edge Cases:
"""
    inputs will be positive integers greater than 0 up to 500,000
    inputs will not be empty or null
"""
# Return:
"""
    the total count of divisors of the input integer
"""
# Examples:
"""
    1 => 1
    4 => 3
    5 => 2
    12 => 6
    30 => 8
    4096 => 13
"""
# Pseudocode:
"""
    # declare an empty array named result to append the divisors 
    # iterate from 1 to the input integer inclusively by adding 1 to the input integer in the for loop stop
    # if the current index divided by the input integer has no remainder
    # append the current index to result
    # return the length of the array result
"""

# my answer
def divisors(n):
    # declare an empty array named result to append the divisors 
    result = []
    # iterate from 1 to the input integer inclusively by adding 1 to the input integer in the for loop stop
    for i in range(1,n +1):
    # if the current index divided by the input integer has no remainder
        if n % i == 0:
    # append the current index to result
            result.append(i)
    # return the length of the array result
    return len(result)

# my answer using sum() with 1's for each divisor instead of len() with the divisors
# Also included in most clever
def divisors(n):
    return sum([1 for i in range(1,n +1) if n % i == 0])

# lambda version
# Also included in Most Clever
divisors = lambda n: sum([1 for i in range(1,n +1) if n % i == 0])

# my answer refactored for Codewwars
# Also Best Practices
def divisors(n):
    return len([n//i for i in range(1,n +1) if n % i == 0])

# lambda version
divisors = lambda n: len([n//i for i in range(1,n +1) if n % i == 0])

print(divisors(1)) # 1
print(divisors(4)) # 3 
print(divisors(5)) # 2
print(divisors(12)) # 6 
print(divisors(30)) # 8
print(divisors(4096)) # 13

# Most Clever is stating computation times
# For Beginners.

# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])