# Jaden Casing Strings
# Parameters or Edge Cases:
# Return:
    # the input string with each word's first letter to uppercase
# Examples:
    # "How can mirrors be real if our eyes aren't real" => "How Can Mirrors Be Real If Our Eyes Aren't Real"
# Pseudo Code:
    # split each word on empty space into a list
    # create a shallow copy array using map with the .capitalize() to upper the first character of each element
    # return the new array as a string making sure to join on an empty space

# my answer
def to_jaden_case(string):
    return " ".join(map(lambda x: x.capitalize(), string.split()))

# my answer refactored implicit return
to_jaden_case = lambda s: " ".join(map(lambda x: x.capitalize(), s.split()))

# I refactored the best practices and most clever code as how I would agree it being best practices.
import string
def to_jaden_case(s):
    return string.capwords(s)

# I further refactored the code to an implicit return with import.
to_jaden_case = lambda s: __import__('string').capwords(s)

print(to_jaden_case("How can mirrors be real if our eyes aren't real")) # "How can mirrors be real if our eyes aren't real"

# best practices and most clever
# I strongly disagree for this being best practices.
# This is the most clever in is it the least code used.
import string
to_jaden_case = string.capwords

# using for element in string instead of map(function, list)
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# declare an empty string and concat to it
def to_jaden_case(string):
    words = string.split(" ")
    output = ""
    for word in words:
        corrected = word.capitalize()
        output += corrected + " "
        
    return output[0:-1]
# [0:-1] to take from begining to last one excluding the last one " "
# word.capitalize = to capitalize the first letter of an string

# concatenation with rstrip() to remove white spaces at the end of the string
def to_jaden_case(string):
    return ''.join(w.capitalize()+' ' for w in string.split()).rstrip()

# using array methods with [start:stop:step]
def to_jaden_case(string):
    res = []
    for w in string.split():
        res.append(w.upper()[:1] + w[1:].lower())
    return " ".join(res)

# regex
import re
def to_jaden_case(string):
    return re.sub(r"\S+", lambda x: x.group().capitalize(), string)

# pure array methods
def to_jaden_case(s):
    return ' '.join(map(lambda e:e[0].upper()+e[1:].lower(),s.split()))