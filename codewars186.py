# Anagram Detection
"""
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
"""
# Parameters or Edge Cases
"""
inputs will be a word consisting only of letters
letters can be uppercase or lowercase
inputs will not be empty or null
"""
# Return:
"""
boolean true if both inputs contain the same letters and are the same length
"""
# Examples:
"""
    "foefet", "toffee" => True
    "Buckethead", "DeathCubeK" => True
    "Twoo", "WooT" => True
    "dumble", "bumble" => False
    "ound", "round" => False
    "apple", "pale" => False
"""
# Pseudocode:
"""
    # convert both inputs into lowercase
    # if the inputs are not equal in length return false
    # iterate through the first input elements and if they do not exist in the second input return false 
    # outside the for loop return true

    # or sort both inputs and if they are not equal return False else return True
"""

# my answer using a for loop
def is_anagram(test, original):
    # convert both inputs into lowercase
    a,b = test.lower(),original.lower()
    # if the inputs are not equal in length return false
    if len(a) != len(b):
        return False
    # iterate through the first input elements and if they do not exist in the second input return false
    for e in a:
        if e not in b:
            return False
    # outside the for loop return true
    return True

# my answer using sorted() instead of a for loop
def is_anagram(test, original):
    # convert both inputs into lowercase
    a,b = test.lower(),original.lower()
    # if both sorted inputs are not equal
    if sorted(a) != sorted(b):
        return False
    # outside the for loop return true
    return True

# my answer refactored
def is_anagram(a, b):
    if sorted(a.lower()) != sorted(b.lower()):
        return False
    return True

# my answer refactored for Codewars only
def is_anagram(a, b):
    return False if sorted(a.lower()) != sorted(b.lower()) else True

# lambda implicit return
is_anagram = lambda a,b: False if sorted(a.lower()) != sorted(b.lower()) else True

print(is_anagram("foefet", "toffee")) # True
print(is_anagram("Buckethead", "DeathCubeK")) # True
print(is_anagram("Twoo", "WooT")) # True
print(is_anagram("dumble", "bumble")) # False
print(is_anagram("ound", "round")) # False
print(is_anagram("apple", "pale")) # False

# In this case Counter creates a dict that has each letter as keys and the occurrences of each letter as value.
from collections import Counter
# write the function is_anagram
def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())

# creating a dictionaries or in JavaScript objects
def is_anagram(test, original):
    test_dict, original_dict = {}, {}
    for i in test.lower():
        test_dict[i] = test_dict.get(i, 0) + 1
    for i in original.lower():
        original_dict[i] = original_dict.get(i, 0) + 1
        
    return test_dict == original_dict

# using ord() for ascii integer values of each letter
def is_anagram(test, original):
    if len(test) != len(original):
        return False
    
    alphabet = [0] * 26
    
    for i in range(len(test)):
        alphabet[(ord(test[i]) & 31) - 1] += 1
        alphabet[(ord(original[i]) & 31) - 1] -= 1

    return not any(alphabet)

# creating an array and using not any() for boolean implicit return
def is_anagram(test, original):
    if len(test) != len(original):
        return False
    
    count = [0] * 26
    
    for i in range(len(test)):
        count[(ord(test[i]) & 31) - 1] += 1
        count[(ord(original[i]) & 31) - 1] -= 1

    return not any(count)