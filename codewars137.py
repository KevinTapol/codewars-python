# Count characters in your string
"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""
# Parameters or Edge Cases:
"""
    inputs will be strings of characters
    the input can be empty
"""
# Return:
"""
    a dictionary where the keys are each individual character in the input and the value is the count of occurrences of the characters in the input
"""
# Examples:
"""
    'aba' => {'a': 2, 'b': 1}
    '' => {}
    'aa' => {'a' : 2}
    'aabb' => {'b' : 2, 'a' : 2}
"""
# Pseudocode:
"""
    # if the input string length is 0 then return {}
    # declare an empty list as value
    # declare a list of each individual string character of the input as input
    # declare a list of a set of the input to obtain an array of each character only once as key
    # iterate through key and for each element count the number of times it occurs in input
    # append that count to value
    # create a dictionary from the lists key and value
    # return the dictionary
"""

# my answer
def count(s):
    # if the input string length is 0 then return {}
    if len(s) == 0:
        return {}
    # declare an empty list as value
    value = []
    # declare a list of each individual string character of the input as input
    input = [e for e in s]
    # declare a list of a set of the input to obtain an array of each character only once as key
    key = list(set(input))
    # iterate through key and for each element count the number of times it occurs in input append that count to value
    for e in key:
        value.append(input.count(e))
    # create a dictionary from the lists key and value
    result = dict(zip(key, value))
    # return the dictionary
    return result

# my answer refactored
def count(s):
    input = [e for e in s]
    key = list(set(input))
    value = [input.count(e) for e in key]
    return dict(zip(key, value))


print(count('aba')) # {'a': 2, 'b': 1}
print(count('')) # {}
print(count('aa')) # {'a' : 2}
print(count('aabb')) # {'b' : 2, 'a' : 2}

# best practices
# Counter() returns a dictionary of the input where each character is the key and the value is the count of each character occurrence. Keys cannot have duplicates. So, duplicates will be removed instead of error out.
from collections import Counter

def count(string):
    return Counter(string)

# most clever
# I completely forgot that a dictionary will eliminate duplicates for keys. So, this means you do not need to make a list set for each element only occurring once because converting it to a dictionary does it implicitly.
def count(string):
    return {i: string.count(i) for i in string}

# same idea as most clever but broken up into easier to read code
def count(string):
    letters = {}
    for c in string:
        letters[c] = string.count(c)
    return letters

# same idea as most clever but you don't need set() because using dictionary notation in the return will eliminate duplicate keys
def count(s):
    return {x:s.count(x) for x in set(s)}

# same idea as most clever but using .get()
def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter

# one liner of best practices
from collections import Counter as count

# maintaining as a string and concatenating the key to an empty object if it exists add 1 to the value else for first occurrence set value to 1
def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r