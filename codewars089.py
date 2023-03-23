# String ends with?
# Parameters or Edge Cases:
    # will both inputs always be a string?
    # will they always be letters or can they be numbers or special characters?
    # can they be empty?
    # do I need to worry about case sensitivity for comparison? I'll just lowercase everything before comparing
# Return:
    # boolean true if both inputs are strings and end with the same string value else false
# Examples:
    # ('abc', 'bc') => true
    # ('abc', 'd') => false
# Pseudo Code:
    # use the python method endswith() on each value and compare if they are equal
    # this will result in an implicit boolean return

    # if I didn't know the endswith() method, I would take the length second input and create a shallow copy of the first input going backwards the length of the second input
    # then compare them in value for an implicit boolean return


# my answer, best practices and most clever
def solution(text, ending):
    return text.endswith(ending)

# my answer refactored implicit return
solution = lambda a, b : a.endswith(b)

# my answer not using endswith()
# get the length difference of the strings to get the start point comparison 
# create a new string starting at that length comparison
# compare the new string to the 2nd input to implicitly return boolean
def solution(a, b):
    len_dif_start_index = len(a) - len(b)
    a_string_start_len_dif = a[len_dif_start_index:]
    return a_string_start_len_dif == b

# my answer not using endswith() refactored
solution = lambda a,b : a[(len(a) - len(b)):] == b

print(solution('abc', 'bc')) # true
print(solution('abc', 'd')) # true

# shortest answer
solution = str.endswith

# clever example not using endswith()
# same as my 2nd answer but using for element in string of start backwards from the first input at the length of the second input
def solution(string, ending):
    return ending in string[-len(ending):]

# using regex
from re import search, escape

def solution(string, ending):
    return bool(search(escape(ending)+'\Z',string))