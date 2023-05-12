# Valid Braces
"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""
# Parameters or Edge Cases:
"""
    all inputs will be strings of only parentheses (), brackets [] or curly braces {}
    inputs will not be empty or null
"""
# Return:
"""
    boolean true if all braces are matched with the correct brace else false
"""
# Examples
"""
    "(){}[]"   =>  True
    "([{}])"   =>  True
    "(}"       =>  False
    "[(])"     =>  False
    "[({})](]" =>  False
"""
# Pseudocode
"""
    # declare an object of key value pairs of braces () [] and {} where the opening braces are keys and the closing braces are values
    # declare an empty array result
    # iterate through the input string
    # if the element is a key in the object braces 
    # append the element to result
    # else
    # if the length of result equals 0 or the last element in result passed in the object braces does not equal the current element
    # return false
    # outside of the for loop if the length of result equal 0 return true else false

"""
# my answer
def valid_braces(string):
    # declare an object of key value pairs of braces () [] and {} where the opening braces are keys and the closing braces are values
    braces = { '(':')', '[':']', '{':'}'}
    # declare an empty array result
    result = []
    # iterate through the input string
    for e in string:
        # if the element is a key in the object braces 
        if e in braces.keys():
            # append the element to result
            result.append(e)
        # else
        else:
            # if the length of result equals 0 or the last element in result passed in the object braces does not equal the current element
            if len(result) == 0 or braces[result.pop()] != e:
                # return false
                return False
    # outside of the for loop if the length of result equal 0 return true else false
    if len(result) == 0:
        return True
    else:
        return False
    
print(valid_braces("(){}[]")) # True
print(valid_braces("([{}])")) # True
print(valid_braces("(}")) # False
print(valid_braces("[(])")) # False
print(valid_braces("[({})](]")) # False

# best practices
# same idea as my answer but refactored with boolean comparison return
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  

# most clever
# wow so this will iterate through repeatedly and find the pairs next to each other and replace them with an empty space. This means that if there is a nested brace, that brace will be removed and the parent braces will then be next to each other to be removed in the next loop until there are no pairs left. This means that if the final result has anything left then there irregular pairs. So if the final answer is empty then return true else false.
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

# same idea as most clever but declaring the empty string as an argument
def validBraces(s, previous = ''):
  while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s

# a while loop that is declaring an array of pairs to compare to the input
def validBraces(s):
    pairs = ['{}', '()', '[]']
    while any(pair in s for pair in pairs):
        for pair in pairs: 
            s = s.replace(pair, "")
    return s == ""

# same as best practices but using elif instead of else if
BRACES = {"(":")", "{":"}","[":"]"}

def validBraces(string):
  waiting = []
  for l in string:
    if l in BRACES.keys():
      waiting.append(BRACES[l])
    elif not waiting or waiting.pop() != l:
      return False
  return not waiting

# importing regex and creating a class
# they used list(zip(key,value)) to create a nested array of pairs
import re

class Stack(object):
    def __init__(self): self._vals = []
    def push(self, i): self._vals.append(i)
    def peek(self): return self._vals[-1] if not self.is_empty() else None
    def pop(self): self._vals.pop()
    def is_empty(self): return len(self._vals) == 0

def validBraces(string):
    openers, closers = map(list, ('({[', ')}]'))
    pairs = list(zip(openers, closers))

    s = Stack()
    for char in list(string):
        if char in openers:
            s.push(char)
        elif (char in closers and (s.peek(), char) in pairs):
            s.pop()
    return s.is_empty()

# regex and while loop
import re

def validBraces(stg):
    while any(pair in stg for pair in ("{}", "[]", "()")):
        stg = re.sub(r"{}|\[]|\(\)", "", stg)
    return not stg