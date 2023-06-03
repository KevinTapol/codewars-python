# Count the monkeys
"""
You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

For example(Input --> Output):

10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 1 --> [1]
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
"""
# Return:
"""
    create an array with elements from 1 to n inclusively
"""
# Psuedocode:
"""
    create an array starting at 1 stopping at n +1 stepping by 1
    return the array
"""

# my answer
def monkey_count(n):
    x = [i for i in range(1,n+1)]
    return x

# my answer refactored 
def monkey_count(n):
    return [i for i in range(1,n+1)]

# my answer refactored for Codewars only implicit return lambda 
monkey_count = lambda n: [i for i in range(1,n+1)]

print(monkey_count(1)) # [1]
print(monkey_count(10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# best practices and most clever
# ah right no need to a for loop if your not mutating each element
def monkey_count(n):
    return list(range(1, n+1))

# for loop similar to my answer but easier to read
def monkey_count(n):
    #your code here
    list = []
    for i in range(1,n+1):
        list.append(i)
    return list

# using extend() instead of append()
def monkey_count(n):
    #your code here
    L=[]
    L.extend(range(1,n+1))
    return(L)

# while loop with variable declarations for stop conditions
def monkey_count(n):
    a = []
    i = 1
    while i < n+1:
      a = a + [i]
      i += 1
    return a  