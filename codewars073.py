# Vowel Count
# Parameters or Edge Cases:
    # We will consider a, e, i, o, u as vowels for this Kata (but not y).
    # The input string will only consist of lower case letters and/or spaces.
# Return:
    # Return the number (count) of vowels in the given string.
# Examples:
    # "aeiou" => 5 
    # "y" => 0
# Pseudo Code:
    # declare an integer count = 0 to account for empty or null strings
    # iterate through the input and if the string includes the characters aeiou add 1 for each element in the string
    # return the new count
# my answer
def get_count(sentence):
    count = 0
    for i in sentence[:]:
        # here I used multiple conditions instead of if i in "aeiou"
        if i == "a" or i =="e" or i =="i" or i =="o" or i =="u":
            count += 1
    return count

# my answer refactored implicit return lambda
# instead of declaring an empty variable here I am adding summing 1 each time the string contains any of the vowels aeiou
get_count = lambda s: sum(1 for i in s if i in "aeiou")

print(get_count("aeiou")) # 5
print(get_count("y")) # 0
print(get_count("")) # 0
print(get_count("abracadabra")) # 5

# best practices and most clever
# here they are accounting for uppercase which the Kata parameters stated only lowercase will be involved
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# summing truthy falsy
# c represent boolean true
# here they are summing how many boolean true results of 'aeiou' existing in the input
def getCount(s):
    return sum(c in 'aeiou' for c in s)

# importing re to use .findall() and re.IGNORECASE 
# then returning the length of the new string with len()
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

# same idea as above but using for each element in input
# returning the length of the new list for each element that is aeiou
def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeoiu'])

# using .count() in a list
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])

# implicit lambda using .count()
getCount = lambda s: sum(s.count(i) for i in 'aeiou')

# counting instances of boolean True but outside the list 
def getCount(inputStr):
    return [letter in "aeiou" for letter in inputStr].count(True)