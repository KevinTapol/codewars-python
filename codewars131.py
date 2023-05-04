# Break camelCase
"""
  Complete the solution so that the function will break up camel casing, using a space between words.
"""
# Parameters or Edge Cases:
"""
  inputs will be a string word in camelCase
  inputs can be empty
"""
# Return:
"""
  a copy of the string with a white space preceding each capital letter of the camel case word
"""
# Examples:
"""
  "camelCasing"  =>  "camel Casing"
  "identifier"   =>  "identifier"
  ""             =>  ""
"""
# Pseudocode:
"""
  declare an empty string named result
  declare a string with the alphabet to uppercase named cap
  iterate through the input and if the current character is not in cap then concat the element to result
    if the current character is in cap then concat a white space then the element
  return the result

"""

# my answer
def solution(s):
    # declare an empty string named result
    result = ""
    # declare a string with the alphabet to uppercase named cap
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # iterate through the input and if the current character is not in cap then concat the element to result
    for i,e in enumerate(s):
      if e not in cap:
         result += e
      # if the current character is in cap then concat a white space then the element   
      else:
         result = result + " " + e
    # return the result     
    return result

# my answer refactored
def solution(s):
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join([e if e not in cap else " " + e for e in s])

# my answer refactored implicit return declaring cap in the argument
solution = lambda s, cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "".join([e if e not in cap else " " + e for e in s])

print(solution("camelCasing")) # "camel Casing"
print(solution("identifier")) # "identifier"
print(solution("")) # ""

# best practices and most clever
# The isupper() method returns True if all the characters are in upper case, otherwise False.
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

# using regex
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

# using .islower() instead of .isupper()
def solution(s):
    return ''.join(map(lambda x: x if x.islower() else " "+ x, s))

# regex with .findall()
import re
def solution(s):
    return ' '.join([x for x in re.findall('.[^A-Z]*', s)])