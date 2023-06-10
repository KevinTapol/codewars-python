# Reverse words
"""

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""
# Parameters or Edge Cases:
"""
    inputs will be a string sentence
"""
# Return:
"""
    return the sentence with each word in the same order but each word reversed
"""
# Examples:
"""
    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
"""
# Pseudocode:
"""
    # declare an empty array result
    # iterate through the input split on whitespace
    # append each element in reverse to result
    # convert result into a string joining on whitespace
"""

# my answer
def reverse_words(text):
    # declare an empty array result
    result = []
    # iterate through the input split on whitespace
    for e in text.split(' '):
    # append each element in reverse to result
        result.append(e[::-1])
    # convert result into a string joining on whitespace
    return ' '.join(result)

# my answer refactored best practices and most clever
def reverse_words(t):
    return ' '.join(e[::-1] for e in t.split(' '))

# my answer refactored for codewars lamba one liner
reverse_words = lambda t: ' '.join(e[::-1] for e in t.split(' '))

print(reverse_words("This is an example!")) # "sihT si na !elpmaxe"
print(reverse_words("double  spaces")) # "elbuod  secaps"

# regex
import re

def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)

# using map() with a function for its argument and string input split on whitespace as the second argument
def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))

# regex with join
import re

def reverse_words(str):
  return ''.join(word[::-1] for word in re.split(r'(\s+)', str))