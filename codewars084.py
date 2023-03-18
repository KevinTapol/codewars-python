# Shortest Word
# Parameters or Edge Cases:
    # inputs will be a string of words
    # String will never be empty and you do not need to account for different data types.
# Return:
    # the length of the shortest word
# Examples:
    # "bitcoin take over the world maybe who knows perhaps" => 3
    # "turns out random test cases are easier than writing out basic ones" => 3
    # "lets talk about javascript the best language" => 3
    # "i want to travel the world writing code one day" => 1
    # "Lets all go on holiday somewhere very cold" => 2   
    # "Let's travel abroad shall we" => 2
# Pseudo Code:
    # split the string into an array of elements on white space using 
    # create a shallow copy array of each word taking in the length of each element 
    # use min() on the new array and return the result

# my answer
def find_short(s):
    return min(list(map(lambda e: len(e), s.split())))

# my answer refactored implicit return
find_short = lambda s: min(list(map(lambda e: len(e), s.split())))
    
print(find_short("bitcoin take over the world maybe who knows perhaps")) # 3
print(find_short("turns out random test cases are easier than writing out basic ones")) # 3
print(find_short("lets talk about javascript the best language")) # 3
print(find_short("i want to travel the world writing code one day")) # 1
print(find_short("Lets all go on holiday somewhere very cold")) # 2
print(find_short("Let's travel abroad shall we")) # 2

# best practices and most clever
# using minimum length element for elements in array
def find_short(s):
    return min(len(x) for x in s.split())

# passing int a 2nd argument for min() of key = length
def find_short(s):
    return len(min(s.split(' '), key=len))

#same as above but broken down into clean documentation
def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length

# a much shorter and cleaner version of my code
# you can remove the white space quotes in split
def find_short(s):
    return min(map(len, s.split(' ')))

# iterating through with for element in string with conditionals
def find_short(s):
    sList = s.split()
    shortestLength = len(sList[0])
    for item in sList:
        if len(item) < shortestLength:
            shortestLength = len(item)
    return shortestLength

# sort by length and return the length of the first element
def find_short(s):
    return len(sorted(s.split(), key=len)[0])

# using reduce() 
# this answer didn't import reduce and will not work without it. I added it below
from functools import reduce

def find_short(s):
    return len(reduce((lambda x, y: x if len(x) < len(y) else y), s.split())) # l: shortest word length