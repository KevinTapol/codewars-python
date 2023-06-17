# Testing 1-2-3
"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""
# Parameters or Edge Cases:
"""
    inputs will a list of strings of letters
    input lists can be empty or null
"""
# Return:
"""
    return a list with each element of the input list concatenated with their index +1 : and white space
"""
# Examples:
"""
[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""
# Pseudocode:
"""
    # declare an empty list named result
    # enumerate through the input array using index and element
    # using string interpolation concat the string current index + 1: to the current element
    # return the new list
"""

# my answer
def number(lines):
    # declare an empty list named result
    result = []
    # enumerate through the input array using index and element
    for i,e in enumerate(lines):
    # using string interpolation concat the string current index + 1: to the current element
        result.append(f"{i+1}: {e}")
    # return result
    return result

# my answer refactored for codewars 
def number(lines):
    return [f"{i+1}: {e}" for i,e in enumerate(lines)]

# my answer refactored lambda for codewars only
number = lambda a: [f"{i+1}: {e}" for i,e in enumerate(a)]

print(number([])) # []
print(number(["a", "b", "c"])) # ["1: a", "2: b", "3: c"]

# best practices and most clever
# using enumerate starting at index 1 instead of adding 1 to the index
# enumerate(iterable, start) returns a list of tuples of index and element
# here they are using %d for index and %s for element
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

# similar to my answer but they are starting at 1 for enumerate
def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

# using .format(index, element) with enumerate(input, start)
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]

# using basic string concatenation
def number(lines):
    #your code here
    a=[]
    for i,c in enumerate(lines,1):
        str_var = str(i) + ': ' + str(c) #make sure to add another space
        a.append(str_var)
    return a

# importing starmap() instead of using .format() with arguments
from itertools import starmap

def number(lines):
    return list(starmap("{}: {}".format, enumerate(lines,1)))