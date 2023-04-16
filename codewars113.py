# Duplicate Encoder
# Parameters or Edge Cases:
    # inputs will be a string of characters that can be letters and special character
    # ignore capitalization meaning bring all characters to uppercase or lowercase
# Return:
    # a string replacing each character with ( if the character occurs more than once else )
# Examples:
    # "din"      =>  "((("
    # "recede"   =>  "()()()"
    # "Success"  =>  ")())())"
    # "(( @"     =>  "))((" 
# Pseudocode:
    # declare an empty string
    # iterate through the input string and if the element in the string occurs more than once add ( to the declared string else add )
    # return the new string

# my answer
def duplicate_encode(word):
    result = ""
    for e in word.lower():
        if word.lower().count(e) > 1:
            result += ")"
        else:
            result += "("
    return result

# my answer refactored
def duplicate_encode(w):
    return "".join([")" if w.lower().count(e) > 1 else "(" for e in w.lower()])

# my answer further refactored lambda implicit return
duplicate_encode = lambda w: "".join([")" if w.lower().count(e) > 1 else "(" for e in w.lower()])

print(duplicate_encode("din")) # "((("
print(duplicate_encode("recede")) # "()()()"
print(duplicate_encode("Success")) # ")())())"
print(duplicate_encode("(( @")) # "))(("

# best practices and most clever same as my refactored answer but if else conditions switched
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# imported Counter() instead of using .count()
# This is more efficient than the top solution because the character counts are only computed once.
from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)

# clean documentation
#This solution is O(n) instead of O(n^2) like the methods that use .count()
#because .count() is O(n) and it's being used within an O(n) method.
#The space complexity is increased with this method.
import collections
def duplicate_encode(word):
    new_string = ''
    word = word.lower()
    #more info on defaultdict and when to use it here:
    #http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string

# here they are creating a dictionary or object key value pair and return the value
def duplicate_encode(word):
    word = word.lower()
    dict = {}
    for char in word:
        dict[char] = ')' if char in dict else '('
    
    return ''.join( dict[char] for char in word )