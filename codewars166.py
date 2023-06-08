# Which are in?
"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.
""" 
# Parameters or Edge Cases:
"""
    inputs will be 2 arrays of strings of words of lowercase letters
"""
# Return:
"""
    an array of strings that elements in array1 exist in some part of a word in array2
"""
# Examples:
"""
    ["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"] => ['arp', 'live', 'strong']
    ["arp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"] => ['arp']
"""
# Pseudocode:
"""
    # declare an empty array result
    # iterate through array1 
    # iterate through array2
    # if the current element of arr1 is in the current element of arr2 and not in result append the current element of arr1 to result
    # sort result 
    # return result
"""

# my answer
def in_array(arr1, arr2):
    # declare an empty array result
    result = []
    # iterate through arr1 
    for e in arr1:
        # iterate through arr2
        for v in arr2:
            # if the current element of arr1 is in the current element of arr2 and not in result append the current element of arr1 to result
            if e in v and e not in result:
                result.append(e)
    # sort result
    result.sort()
    # return result
    return result

# my refactored answer returning result.sort() in the same line
def in_array(arr1, arr2):
    result = []
    for e in arr1:
        for v in arr2:
            if e in v and e not in result:
                result.append(e)
    return sorted(result)

print(in_array(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"])) # ['arp', 'live', 'strong']
print(in_array(["arp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"])) # ['arp']


# best practices are very similar to mine except for the conditional statement is a better refactored version
def in_array(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res

# most clever
# using set notation {} inside of sorted() with any() in the conditional
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

# similar to most clever but using set()
def in_array(a1, a2):
    return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))

# similar to best practices but using set() instead of eliminating duplicates in the conditional statement
def in_array(array1, array2):
    result = set()
    for a in array1:
        for b in array2:
            if a in b:
                result.add(a)
                break
    return sorted(result)

# one liner of above answer
def in_array(array1, array2):
    # your code
    return sorted(set([word for word in array1 for word_2 in array2 if word in word_2]))