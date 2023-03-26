# Is this a triangle?
# Parameters or Edge Cases:
    # inputs will be positive integers
# Return:
    # true if a triangle can be built with the integers representing the side lengths of a triangle else false
# Examples:
    # (1, 2, 2) => True
    # (7, 2, 2) => False
    # (1, 2, 3) => False
    # (1, 3, 2) => False
    # (3, 1, 2) => False
# Pseudo Code:
    # Google the formula for given 3 lengths is it a triangle
    # Triangle Inequality Theorem - the sum of lengths of two sides is always greater than the third side.

    # This means that I can pick the sum of any 2 inputs and it should be more than the remaining value.
    # true statements would be a + b > c, a + c > b and b + c > a

    # use and 

# my answer and best practices
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# my answer refactored implicit return lambda
is_triangle = lambda a,b,c: a + b > c and a + c > b and b + c > a

print(is_triangle(1, 2, 2)) # True
print(is_triangle(7, 2, 2)) # False
print(is_triangle(1, 2, 3)) # False
print(is_triangle(1, 3, 2)) # False
print(is_triangle(3, 1, 2)) # False

# most clever
# sort the inputs in value and reassign the inputs in ascending order
# this way, take the sum of the lowest 2 values and check if they are greater than the larges input integer
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

# take the highest value from the inputs and multiply by 2 and check to see if it is less than the sum of all the inputs
def is_triangle(a, b, c):
    return 2 * max(a, b, c) < a + b + c

# all values will be positive so |a-b| < c is equal to -c < a-b < c
def is_triangle(a, b, c):
  return abs(a-b) < c < a+b

# using all() return true if all items in an iterable are true else false
def is_triangle(a, b, c):
    return all([a+b>c, a+c>b, b+c>a])