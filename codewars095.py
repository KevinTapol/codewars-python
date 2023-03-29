# Two to One
# Parameters or Edge Cases:
    # inputs will be strings including only letters
    # will the inputs be case sensitive
    # will the inputs be null or empty
# Return:
    # a new sorted string concatenating both inputs and containing each character only once
# Examples:
    # "aretheyhere", "yestheyarehere" => "aehrsty"
    # "loopingisfunbutdangerous", "lessdangerousthancoding" => "abcdefghilnoprstu"
    # "inmanylanguages", "theresapairoffunctions" => "acefghilmnoprstuy"
# Pseudo Code:
    # concat the inputs
    # use set() to create an instance of each character only once in curly bracket notation
    # sort the set() using sorted() which converts the set into a list
    # then convert the list into a string with "".join()
    # return the new string



# my answer, best practices and most clever
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# my answer refactored implicit return
longest = lambda a,b: "".join(sorted(set(a+b)))

print(longest("aretheyhere", "yestheyarehere")) # "aehrsty"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding")) # "abcdefghilnoprstu"
print(longest("inmanylanguages", "theresapairoffunctions")) # "acefghilmnoprstuy"

# clever use of one liner for element in alphabet if x in concatenated inputs to pull each character only once
def longest(s1, s2):
    return "".join([x for x in "abcdefghijklmnopqrstuvwxyz" if x in s1+s2])

# wow adding each time to an empty string that the element is not in the concatenated inputs
def longest(s1, s2):   
    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Concatenating the Two Given Strings
    s = s1 + s2
    # Declaring the Output Variable
    y = ""
    # Comparing whether a letter is in the string
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x
    # returning the final output    
    return y

# using pipe character for union or or instead of concatenating
def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))

# same idea as | but using .union()
def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))

# for element in concatenated inputs and not in x meaning only include each character once
def longest(s1, s2):
    x=''
    y=sorted(s1+s2)
    for i in y:
      if i not in x:
        x += i
    return x 

# importing numpy to use .unique()
import numpy
def longest(a1, a2):
    # numpy.unique returns an ordered list of all unique elements of an array
    return "".join(numpy.unique(list(a1 + a2)))