# Unique In Order
# Parameters or Edge Cases:
    # DO NOT CHANGE THE ORDER OF THE INPUTS!!! DELETE CHARACTERS NEXT TO EACH OTHER THAT ARE DUPLICATES
    # inputs can be a string of letters both capital and lowercase
    # inputs can also be an array of integers or an array of strings
    # capital letters are not considered equal to their lowercase equivalent ex "C" != "c" 
    # input strings can be empty
    # input arrays can be empty
    # integers can be negative or positive
    # Can arrays of strings be 2d arrays?
    # if the input contains only one type of character duplicated then return an array of that character used only once
# Return:

# Examples:
    # 'AAAABBBCCDAABBB' => ['A', 'B', 'C', 'D', 'A', 'B']
    # 'ABBCcAD'         => ['A', 'B', 'C', 'c', 'A', 'D']
    # [1, 2, 2, 3, 3]   => [1, 2, 3]
    # (1, 2, 2, 3, 3)   => [1, 2, 3]
    # "" => []
    # [] => []
    # () => []
    # "A" => ["A"]
    # ["A"] => ["A"])
    # ("A",) => ["A"]
# Pseudocode:
    # create a copy of the input as a list 
    # creating a copy of a string and converting it to a list creates a new list of each string element at it's own index
    # create an empty list
    # if the index is 0 or the element at the current index is not equal to the element at the next index then append the current index to the empty array
    # return the empty array


# my answer
def unique_in_order(s):
    copy = list(s[:])
    result = []
    for i in range(len(copy)):
        if i == 0 or copy[i] != copy[i-1]:
            result.append(copy[i])
    return result

# my answer refactored
def unique_in_order(s):
    copy = list(s[:])
    result = []
    return [copy[i] for i in range(len(copy)) if i == 0 or copy[i] != copy[i-1]]

print(unique_in_order("")) # []
print(unique_in_order(())) # []
print(unique_in_order([])) # []
print(unique_in_order("A")) # ["A"]
print(unique_in_order(("A"))) # ["A"]
print(unique_in_order(["A"])) # ["A"]
print(unique_in_order("AA")) # ["A"]
print(unique_in_order(("A","A"))) # ["A"]
print(unique_in_order(["A","A"])) # ["A"]
print(unique_in_order(["A","a"])) # ["A", "a"]
print(unique_in_order("AAAABBBCCDAABBB")) # ["A", "a"]

# best practices and most clever
# here they are declaring the element as prev to compare the next index to the element
# it's a bit messy imo
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

# similar to my answer but instead of declaring a copy globally they use element not equal to res[-1] condition to append
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

# Genius Solution!!
# importing groupby to compare and return an array of elements where the element is not equal to the next index element
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

# using enumerate for index and element array copy
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

# same as above but not implicit return lambda 
def unique_in_order(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]

# clean for loop
"""
it's an "abuse" of the boolean shortcut:

check if x in r[-1:], if so, the or condition is fulfilled so the second statement isn't executed
if x is not in the end part, the second statement is checked and x is appended to the r list.
Note that the or condition returns a boolean, but this one isn't used."""
def unique_in_order(iterable):
	r = []
	for x in iterable:
		x in r[-1:] or r.append(x)
	return r

# return an empty array concatenated with the conditional statement
def unique_in_order(it):
    return [it[0]] + [e for i, e in enumerate(it[1:]) if it[i] != e] if it else []