# Isograms  is a word that has no repeating letters, consecutive or non-consecutive.
# Parameters or Edge Cases:
    # ignore letter case
    # inputs will be a single word string
    # empty string will be considered an isogram
# Return:
    # true if input is an isogram else false
# Examples:
    # "Dermatoglyphics" = true
    # "moose" = false
    # "aba" = false
# Pseudo Code:
    # convert the string to lower case
    # use the count method on the input to see if there are more than 1 and return false else true

# my answer
def is_isogram(string):
    a = string.lower()
    for e in a:
        if a.count(e) > 1:
            return False
    return True

# my answer refactored implicit return using all for boolean return
is_isogram = lambda s: all(False for e in s.lower() if s.lower().count(e) > 1 )

print(is_isogram("Dermatoglyphics")) # True
print(is_isogram("moose")) # False
print(is_isogram("aba")) # False
print(is_isogram("")) # True

# best practices and most clever
# creating a new instance of the string taking each character only once and comparing to the input for a boolean truthy falsy return
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# similar to my refactored answer but they reversed the greater to less than or equal to so that you don't have to use False as a return inside of all()
def is_isogram(string):
    return all(string.lower().count(i) <= 1 for i in string)

# nice commenting
def is_isogram(string):
    #your code here
    char_dict = {}
    string = string.lower()
    
    for char in string:
        if char in char_dict:
            # increment count of this character
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    
    # loop over the characters in dictionary, if any have
    # more than 1 found, this string is not an isogram, so break
    # the loop and function and return False.
    for key in char_dict:
        if char_dict[key] > 1:
            return False
            
    # If no duplicates were found in the loop directly above,
    # this must be an isogram, so return true!
    return True

# importing to use Counter()
from collections import Counter

def is_isogram(string):
    for x in Counter(string.lower()).values():
        if x > 1:
            return False
    return True

# nested for loop
def is_isogram(string):
    s=string.lower() #to ignore cases
    for i in range(0,len(s)): #iterate over all chars in string
        for x in range(i+1,len(s)): #iterate over following chars
            if s[i]==s[x]: #return false on first reoccurance
                return False
    return True #otherwise it's an isogram

# using enumerate()
def is_isogram(string):
    '''
    Isograms are words that have no repeating letters.
    '''
    # 1) Sort the string
    # 2) Loop through each char
    #       If the current char != previous char, continue
    #       Else, return False as we found a repeating char
    string = sorted(string.lower())
    for i, value in enumerate(string):
        if i > 0:
            if value == string[i - 1]:
                return False
    return True