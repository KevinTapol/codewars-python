# Detect Pangram
"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""
# Parameters or Edge Cases:
    # inputs will be a string of words with punctuation and/or special characters
    # ignore case sensitivity meaning uppercase letters and lowercase letters are equal in this case
# Return:
    # boolean true if the input is a pangram else false
# Examples:
    # "The quick, brown fox jumps over the lazy dog!" => # True
    # "Should return false for not a pangram" => # False
# Pseudocode:
    # declare a string with every letter in the alphabet to lower case
    # take the input string and convert it to lowercase
    # iterate through the alphabet string and if the element in the array is not in the input string return False else True

# my answer and best practices
def is_pangram(s):
    # declare a string of every letter in the alphabet to lowercase
    letters = 'abcdefghijklmnopqrstuvyz'
    # for every character in letter that is not in the input string to lowercase return false else true
    for e in letters:
        if e not in s.lower():
            return False
    return True

# my answer refactored using all() on the list to check if all values are true then return true else false
def is_pangram(s):
    a = 'abcdefghijklmnopqrstuvyz'
    return all([False if e not in s.lower() else True for e in a])

# my answer further refactored implicit return
is_pangram = lambda s: all([False if e not in s.lower() else True for e in 'abcdefghijklmnopqrstuvyz'])

print(is_pangram("The quick, brown fox jumps over the lazy dog!")) # True
print(is_pangram("Should return false for not a pangram")) # False

# most clever
# here they are importing ascii_lowercase to get every letter of the alphabet to lowercase instead of declaring a string of every letter in the alphabet to lowercase for comparison
# .issubset() is being used to check if all letters are in the argument passed which in this case is the input to lowercase
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())

# same as most clever but using an alphabet string instead of importing ascii_lowercase
def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False

# comparing lengths for boolean True False with set() taking each character only once
import string

def is_pangram(s):
    return set(s.lower()) >= set(string.ascii_lowercase)

# creating a tuple instead of list but same idea using ascii_lowercase to check for all() return true if all are true in the array
from string import ascii_lowercase

def is_pangram(s):
    return all(l in s.lower() for l in ascii_lowercase)