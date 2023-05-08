# Count the smiley faces!
"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of strings per each element containing special characters
    inputs can be empty
"""
# Return:
"""
    return an integer representing the count of smiley faces in the array
    smiley faces must start with : or ; 
    may or may not contain - or ~
    and end with ) or D 
"""
# Examples:
"""
    Valid smiley face examples: :) :D ;-D :~)
    Invalid smiley faces: ;( :> :} :]
"""
# Pseudocode:
"""
    # declare an empty count and set it to 0
    # iterate through each string element in the array
    # if the elements length is 2 and index 0 is ':' or ';' and index 1 is ')' or 'D' add 1 to count
    # if the elements length is 3 and index 0 is ':' or ';' and index 1 is '-' or '~' and index 2 is ')' or 'D' add 1 to the count
    # return the count

    or 
    # declare an array of accepted values for smiley faces
    # declare a count and set it to 0
    # iterate through the input array and if the element is in accepted values array add 1 to the count
    # return count

"""

# my answer using conditionals
def count_smileys(arr):
    # declare an empty count and set it to 0
    count = 0
    # iterate through each string element in the array
    for e in arr:
    # if the elements length is 2 and index 0 is ':' or ';' and index 1 is ')' or 'D' add 1 to count
        if len(e) == 2 and (e[0] == ':' or e[0] == ';') and (e[1] == ')' or e[1] == 'D'):
            count += 1
    # if the elements length is 3 and index 0 is ':' or ';' and index 1 is '-' or '~' and index 2 is ')' or 'D' add 1 to the count
        if len(e) == 3 and (e[0] == ':' or e[0] == ';') and (e[1] == '-' or e[1] == '~') and (e[2] == ')' or e[2] == 'D'):
            count += 1
    # return the count
    return count


# my answer comparing an array of accepted values to the input array
def count_smileys(arr):
    # declare a count and set it to 0
    count = 0
    # declare an array of accepted values for smiley faces
    accepted_values = [':)', ':D', ';)', ';D', ':~)', ':-)',':-D',':~D', ';-D', ';~D', ';-)', ';~)']
    # iterate through the input array 
    for e in arr:
        # if the element is in accepted values array 
        if e in accepted_values:
            # add 1 to the count
            count += 1
    # return the count        
    return count

# my answer refactored
def count_smileys(arr):
    accepted_values = [':)', ':D', ';)', ';D', ':~)', ':-)',':-D',':~D', ';-D', ';~D', ';-)', ';~)']
    return sum([1 for e in arr if e in accepted_values])

# my answer refactored to implicit return lambda ONLY FOR CODEWARS NOT PRODUCTION!!!
count_smileys = lambda arr, accepted_values = [':)', ':D', ';)', ';D', ':~)', ':-)',':-D',':~D', ';-D', ';~D', ';-)', ';~)']: sum([1 for e in arr if e in accepted_values])


print(count_smileys([':)', ';(', ';}', ':-D'])) # 2
print(count_smileys([';D', ':-(', ':-)', ';~)'])) # 3
print(count_smileys([';]', ':[', ';*', ':$', ';-D'])) # 1

# best practices and most clever
# using regex
# iterate through the input and find all instances of accepted parameters of the input array converted into a string and separated on whitespace
# push the instance to a list and return the length of that new list
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


# triple nested for loop simulating the regex answer
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

# another regex
import re

def count_smileys(arr):
    return sum(1 for s in arr if re.match(r'\A[:;][-~]?[)D]\Z',s))

# implicit return lambdas for CODEWARS ONLY!!! NEVER IN PRODUCTION!! But if this was layered out as a proper function, I would upvote to most clever.
# here they are checking if the first character referenced by index 0, the last character referenced by by index -1 and a copy of the array of index 1 contains success smiley faces in the input array
count_smileys=lambda a:sum(s and s[0]in':;'and s[-1]in')D'and s[1:-1]in('','-','~')for s in a)

# better alternative to the triple nested for loop
# declaring accepted values of individual parts and using conditionals to check for successes
def count_smileys(arr):
    total = 0
    eyes = ':;'
    nose = '-~'
    mouth = ')D'
    for char in arr:

        if len(char) == 3:
            if char[0] in eyes and char[1] in nose and char[2] in mouth:
                total += 1

        elif len(char) == 2:
            if char[0] in eyes and char[1] in mouth:
                total += 1
    return total

# clever answer
# creating a set of accepted combinations and return the length of count of accepted occurrences
def count_smileys(arr):
    smiles = set([a+b+c for a in ":;" for b in ['','-', '~'] for c in ")D"])
    return len([1 for s in arr if s in smiles])

# create a string of accept smileys and convert it into an array of elements
# return the sum of accepted smileys in the input array
valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()

def count_smileys(arr):
    return sum(face in valid for face in arr)