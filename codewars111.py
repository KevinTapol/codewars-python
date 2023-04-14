# Counting Duplicates
# Parameters or Edge Cases:
    # input will be a string of letters and positive integers
    # consider uppercase and lowercase characters as equal
# Return:
    # return the number of characters that have duplicates
# Examples:
    # "abcde" -> 0 # no characters repeats more than once
    # "aabbcde" -> 2 # 'a' and 'b'
    # "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
    # "indivisibility" -> 1 # 'i' occurs six times
    # "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    # "aA11" -> 2 # 'a' and '1'
    # "ABBA" -> 2 # 'A' and 'B' each occur twice
# Pseudocode:
    # declare an empty array to append the elements that occur more than once
    # take in the input string and convert it to lower case
    # iterate through the string and for each element that occurs more than once append said element to the empty array
    # eliminate duplicates from the declared array using set()
    # convert the set into a list
    # return the length of the list

# my answer
def duplicate_count(text):
    result = []
    n = text.lower()
    for e in n:
        if n.count(e) > 1:
            result.append(e)
    return len(list(set(result)))

# my answer refactored 
def duplicate_count(t):
    return len(list(set([e for e in t.lower() if t.lower().count(e) > 1 ])))

# my answer refactored implicit return 
duplicate_count = lambda t: len(list(set([e for e in t.lower() if t.lower().count(e) > 1 ])))

print(duplicate_count("abcde")) # 0
print(duplicate_count("aabbcde")) # 2
print(duplicate_count("indivisibility")) # 1
print(duplicate_count("Indivisibilities")) # 2
print(duplicate_count("aA11")) # 2
print(duplicate_count("ABBA")) # 2

# best practices and most clever
# here they used set() to eliminate all duplicates then grabbed from that set and grabbed the elements from that set() if they occur more than once in the original input to lowercase
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# importing Counter() and also using .iteritems()
# This is a Python 2 solution - for Python 3 use items().
from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)

# using Counter() with .keys() and .values() instead of set()
from collections import Counter

def duplicate_count(text):
    counter = Counter(text.lower())
    return len([counter.keys() for i in counter.values() if i>1])

# an answer without an if statement
# same idea but grabbing elements from the set(input) then sum() the created array
def duplicate_count(text):
    text = text.lower()
    return(sum([text.count(c) > 1 for c in set(text)]))

# using regex
from re import findall

def duplicate_count(text):
    return (len(findall("(\w)\\1+", "".join(sorted(text.upper())))))

# importing Counter() inline
def duplicate_count(text):
    return sum( 1 for v in __import__("collections").Counter(text.lower()).itervalues() if v>1)

# using filter()
def duplicate_count(text):
    """ This is supposed to be a memory efficient solution as it only retain the char->count map in memory. BUT, I'm not
    sure about what python actually does under the hood for those iterators."""
    lc = dict()
    for c in text.lower():
        lc[c] = lc.get(c, 0) + 1
    return sum(1 for _ in filter(lambda ct: ct[1] > 1, lc.items()))