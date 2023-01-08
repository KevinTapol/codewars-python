"""
You only need one-Beginner
Parameters or Edge Cases:
    inputs will be an array of numbers or strings and a value that can be either a number or a string
    Capitilization matters and are not equal ex 'The' != 'the'
Return:
    boolean true if given array contains given value else boolean false
Examples:
            (True, ([66, 101], 66)),
            (False, ([78, 117, 110, 99, 104, 117, 107, 115], 8)),
            (True, ([101, 45, 75, 105, 99, 107], 107)),
            (True, ([80, 117, 115, 104, 45, 85, 112, 115], 45)),
            (True, (['t', 'e', 's', 't'], 'e')),
            (False, (["what", "a", "great", "kata"], "kat")),
            (True, ([66, "codewars", 11, "alex loves pushups"], "alex loves pushups")),
            (False, (["come", "on", 110, "2500", 10, '!', 7, 15], "Come")),
            (True, (["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")),
            (False, ([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)),
            (True, (["anyone", "want", "to", "hire", "me?"], "me?")),
        ]
Psuedo Code:
    loop through the array and check if each value is equal to the given input
    return true if exists else false
"""
# my answer
def check(seq, elem):
    for i in range(len(seq)):
        if seq[i] == elem:
            return True
    return False

# my answer refactored one line lambda implicit return
check = lambda l, e: True if e in l else False

print(check([66, 101], 66)) # True
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8)) # False
print(check([101, 45, 75, 105, 99, 107], 107)) # True
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45)) # True
print(check(['t', 'e', 's', 't'], 'e')) # True
print(check(["what", "a", "great", "kata"], "kat")) # False
print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups")) # True
print(check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come")) # False
print(check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")) # True
print(check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)) # False
print(check(["anyone", "want", "to", "hire", "me?"], "me?")) # True


# best practices and most clever
# implicitly returns boolean
def check(seq, elem):
    return elem in seq

# "from operator import contains" -> the function 'contains' is imported from the builtin module 'operator'
# "... as check" -> an alias, namely 'check', is given to the function 'contains' in this context.
# This works because the function required in this kata fulfills the same purpose as the one living in the operator module.
from operator import contains as check

# while loop
def check(list, x):
    while True:
        if x in list:
            return True
        else:
            return False
    pass

# cleaner one liner than mine
check=lambda arr,e: e in arr

# The index() method returns the position at the first occurrence of the specified value. So if the index is greater or equal to 0 return true and at any other value return false
def check(seq, elem):
    try:
        seq.index(elem) >= 0
    except ValueError: 
        return False
    return True

# The count() method returns the number of elements with the specified value. So if it does exist it will be greater than 0 returning an implicit boolean true
def check(seq, elem):
    return list(seq).count(elem) > 0

# The any() function returns True if any item in an iterable are true, otherwise it returns False. If the iterable object is empty, the any() function will return False.
def check(seq, elem):
    return any(x == elem for x in seq)