# CamelCase Method
"""
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""
# Parameters or Edge Cases:
"""
    inputs will be a string of lowercase words
    inputs can be empty
"""
# Return:
"""
   the input string without spaces an in Pascal case NOT camelCase
   camelCase is the first word is lowercase and every following is uppercase
   PascalCase is every word capitalized 
"""
# Examples:
"""
    "test case" => "TestCase"
    "camel case method" => "CamelCaseMethod"
    "say hello " => "SayHello"
    " camel case word" => "CamelCaseWord"
    "" => ""
"""
# Pseudocode:
"""
    # take in the input string and split it on white space with each element as a capitalized word
    # convert the array into a string with no spaces
    # return the string
"""

# my answer
def camel_case(s):
    # take in the input string and split it on white space with each element as a capitalized word
    x =[e.capitalize() for e in s.split()]
    # convert the array into a string with no spaces
    x = ''.join(x)
    # return the string
    return x

# my answer refactored for Codewars
def camel_case(s):
    return ''.join([e.capitalize() for e in s.split()])

# my answer implicit return lambda for Codewars only
camel_case = lambda s: ''.join([e.capitalize() for e in s.split()])

print(camel_case("test case")) # "TestCase"

# Best Practices and Most Clever
# I completely forgot about title() returns a string where the first character in every word is upper case
# Here they are just using .title() and replacing every whitespace with no space
def camel_case(string):
    return string.title().replace(" ", "")

# for loop using .upper()
def camel_case(string):
    if len(string) == 0: return ""
    str_list = list(string)
    space_ids = [index for index, char in enumerate(str_list) if char == " " and index < len(str_list) - 1 ]
    for index in space_ids:
        str_list[index + 1] = str_list[index + 1].upper()
    str_list[0] = str_list[0].upper()
    changed_str = "".join(str_list)
    changed_str = changed_str.replace(" ", "")
    return changed_str

# same idea as best practices but using .split() and ''.join() instead of .replace()
def camel_case(s):
    #your code here
    return ''.join(s.title().split())

# regex for replacing white spice
import re

def camel_case(string):
    return re.sub('\s+', '', string.title())

# regex for capitalizing every first word (^|\s)
import re

def camel_case(s):
    return re.sub(r'(^|\s)(\w)', lambda m: m.group(2).upper(), s.strip())