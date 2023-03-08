# Disemvowel Trolls
# Parameters or Edge Cases:
    # inputs will be strings
    # do I need to account for empty strings, numbers or special characters?
# Return:
    # the input string removing vowels "aeiou"
# Examples:
    # "This website is for losers LOL!" => "Ths wbst s fr lsrs LL!"
# Pseudo Code:
    # iterate through the string and when I find strings "aeiou" in the input, replace with "" for empty string

# my answer
# def disemvowel(s):
#     x = ""
#     for i in s:
#         if i not in "aeiouAEIOU":
#             x += i  
#     return x

# my answer refactored implicit return lambda
disemvowel = lambda s: "".join(i for i in s if i not in "aeiouAEIOU")

print(disemvowel("This website is for losers LOL!")) # "Ths wbst s fr lsrs LL!"

# best practices and most clever similar to my refactored but not using implicit return and using .lower() on the input
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

# mutating the input and replacing elements instead of creating a shallow copy
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

# using regex
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

# another regex but including capital vowels in the first argument and omitting the last argument to ignore case
import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

# another regex but using (?i) to handle case sensitivity
import re
def disemvowel(string):
    return re.sub(r'(?i)[aeiou]','',string)

# regex using find all and declaring the input as a list
# then using for elements in list/array
# finish with "".join() to return the solution to a string
import re

def disemvowel(string):
    wordList = re.findall('([^aeiouAEIOU]+)*',string)
    return  "".join([word for word in wordList ])

# while loop declare new string and concat elements that are not vowels in declared array
# here they are using the length of the input array as the stop point to iterate through the entire array
def disemvowel(str2handle):
    vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    str2return = ""
    i = 0
    n = len(str2handle)
    while i < n:
        if not str2handle[i] in vowel_character:
            str2return += str2handle[i]
        i += 1
    return str2return

# same idea as the while loop above but as a for loop
# declaring a list of all values intending to remove
# declare an empty string
# loop through the input string and if the element is not in the declared list of values then concat to the empty string
def disemvowel(string):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    answer = ""
    for letter in string:
        if not letter in vowels:
            answer += letter
    return answer

# here they are forcing all vowel characters to lowercase which makes sense because you are omitting them anyways
def disemvowel(string):
        
    s = ""
    for c in string:
        if c.lower() not in "aeiou":
            s += c
    return s

# deprecated for python3 you must use the following answer
def disemvowel(string):
    return string.translate(None, 'aAeEuUoOiI')

# using .translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# ord() function returns the number representing the unicode code of a specified character.
def disemvowel(string):
    return string.translate({ord(i):None for i in 'aeiouAEIOU'})

# creating a function to call another function to iterate through and replace given the arguments
def removeAll(string, letters):
    for l in letters:
        string = string.replace(l, "")
    return string

def disemvowel(string):
    return removeAll(string, "aeiouAIEOU")

# brute force replace chain for each string
def disemvowel(string):
    return string.replace('e', "").replace('E', '').replace('a', '').replace('A', '').replace('o', '').replace('O', '').replace('i', '').replace('I', '').replace('u', '').replace('U', '')