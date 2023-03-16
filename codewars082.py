# Exes and Ohs
# Parameters or Edge Cases:
    # inputs will be strings
    # ignore case sensitivity
    # string can contain any char
    # can the string be empty
# Return:
    # case sensitive boolean return true if there are same amount of x's and o's in the input string else false
    # if no x or o are present return true
# Examples:
    #  "ooxx" => true
    #  "xooxx" => false
    #  "ooxXm" => true
    #  "zpzpzpp" => true // when no 'x' and 'o' is present should return true
    #  "zzoo" => false
# Pseudo Code:
    # lowercase the input
    # count the number of x's and o's in the input string
    # check if the counts are equal for an implicit boolean return 
    # this will take care of empty strings too since 0 = 0 return True

# my answer, best practices and most clever
def xo(s):
    return s.lower().count('x') == s.lower().count('o')

# my answer refactored implicit return lambda
xo = lambda s: s.lower().count('x') == s.lower().count('o')

print(xo("ooxx")) # True
print(xo("xooxx")) # False
print(xo("ooxXm")) # True
print(xo("zpzpzpp")) # True
print(xo("zzoo")) # False
print(xo("")) # True

# brute force for loop 
# declaring variables to count x's and o's
def xo(s):

  exes = 0
  ohs = 0

  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1

  return exes == ohs

# importing Counter() 
from collections import Counter

def xo(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0)

# same as my unrefactored answer but not using True False instead of implicit boolean return with == 
def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False

# importing Counter() in line
def xo(s):
  c = __import__('collections').Counter(s.lower())
  return c['x'] == c['o']


# using regex
import re

# Using regex, the number of x's and o's are extracted from the test string
# and returned as a tuple.
def get_amounts(test):
    return(len(re.findall("[Xx]", test)), len(re.findall("[Oo]", test)))

# The results passed to this function will evaluate to True if they are equal
# and False if they are not.
def eval_results(results):
    if results[0] == results[1]:

        return True
    else:

        return False

# Call the get_amounts( ... ) and eval_results( ... ) functions and return the
# result.
def xo(test):
    result = get_amounts(test)
    return eval_results(result)

# clever using if element in 'caps or lowers input string' then add 1 to the count
def xo(s):
    count = 0
    for i in s:
        if i in 'Xx':
            count += 1
        elif i in 'Oo':
            count -= 1
    return count == 0

# instead of changing the input to either all lowercase or uppercase, they are using or statements in their conditionals with | instead of or
def xo(s):
    countX = 0
    countO = 0
    for i in s:
        if (i == 'X') | (i == 'x'):
            countX = countX + 1
        elif (i == 'O') | (i == 'o'):
            countO = countO + 1
    if countX == countO:     
        return True
    else:
        return False
    
    # using sum() on a new list of conditionals for elements in string
    def xo(s):
        return sum([-1 if c=='o' else (1 if c=='x' else 0) for c in s.lower()])==0
    
    # using .translate()
    def xo(s):
        return len(s.translate(None, 'Xx')) == len(s.translate(None, 'Oo'))