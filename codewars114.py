# Replace With Alphabet Position
# Parameters or Edge Cases:
    # input will be a string containing letters and characters
# Return:
    # only the letters in their location order with their position in the alphabet as a string
# Examples:
    # "The sunset sets at twelve o' clock." => "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    # "The narwhal bacons at midnight." => "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
# Pseudocode:
    # declare a string of lowercase character of every character in the alphabet
    # declare an empty array result
    # declare an object with lowercase letters as the key and their position as a value
    # iterate through the input string in lowercase and for each character that is in the alphabet string concat the object value of that key to the empty array result
    # join the array elements on a whitespace and return the new string

# my answer
def alphabet_position(test):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for e in test.lower():
        if e in alphabet:
            result.append(str(alphabet.index(e) + 1)) 
    return " ".join(result)

# my answer refactored
def alphabet_position(test):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alphabet.index(e) + 1) for e in test.lower() if e in alphabet])

# my answer refactored implicit return 
alphabet_position = lambda test: " ".join([str("abcdefghijklmnopqrstuvwxyz".index(e) + 1) for e in test.lower() if e in "abcdefghijklmnopqrstuvwxyz"])

print(alphabet_position("The sunset sets at twelve o' clock.")) # "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
print(alphabet_position("The narwhal bacons at midnight.")) # "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"

# string.isdigit() and string.isnumeric() returns true if they are digits/numeric(0-9) 
# similar to isinstance("a", str) returns true that "a" is a string
# isinstance(1, int) returns true that 1 is an integer
# type() function returns the type of the specified object
# type(('apple', 'banana', 'cherry')) returns <class 'tuple'> meaning the input is a tuple
# type("Hello World") returns <class 'str'> meaning the input is a string
# type(33) returns <class 'int'> meaning the input is an integer

# best practices and most clever
# ord() returns the integer representation of a character
# in this case "a" returns the integer 97
# isalpha() method returns True if all the string characters are alphabet letters (a-z)
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# same idea as above but using the ord("a") = to 97 + 1 instead of - 96
def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

# similar to my unrefactored answer but adding whitespace to a string instead of an array per iteration then using .lstrip(" ") to remove leading whitespace
# also declaring the string globally instead of locally to the function
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ') 
    
# concatenating white space but using [:-1] to exclude the final white space instead of using .lstrip()
def alphabet_position(text):
    answer = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z']
    for char in text.lower():
        if char in alphabet:
            answer += (str(alphabet.index(char) + 1) + " ")
    return answer[:-1]    
    
# importing ascii_lowercase for lowercase letters a-z
from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())

# create an object key value pair
def alphabet_position(text):
    alphabet = {  'a' : 1,
                  'b' : 2,
                  'c' : 3,
                  'd' : 4,
                  'e' : 5,
                  'f' : 6,
                  'g' : 7,
                  'h' : 8,
                  'i' : 9,
                  'j' : 10,
                  'k' : 11,
                  'l' : 12,
                  'm' : 13,
                  'n' : 14,
                  'o' : 15,
                  'p' : 16,
                  'q' : 17,
                  'r' : 18,
                  's' : 19,
                  't' : 20,
                  'u' : 21,
                  'v' : 22,
                  'w' : 23,
                  'x' : 24,
                  'y' : 25,
                  'z' : 26, }
    inds = []
    for x in text.lower():
        if x in alphabet:
            inds.append(alphabet[x])
    return ' '.join(([str(x) for x in inds]))

# creating a dictionary in steps but same as above
#import string so we can generate the alphabets using string.ascii
import string
def alphabet_position(text):
    lower_case_text = text.lower() #convert the given text into all lowercase letters
    alphabet = string.ascii_lowercase # generate lowercase letters from the string module
    number = list(range(1, 27)) #generate numbers from 1-26
    dict_alphabet_number = dict(zip(alphabet, number)) # combine the aphabets in a dictionary using dict and zip
    collector = [] # create a container to old the numbers generated from the loop
    
    for element in lower_case_text: 
        if element in alphabet:
            collector.append(str(dict_alphabet_number[element])) 
    return ' '.join(collector)

# using filter()
def alphabet_position(text):
  al = 'abcdefghijklmnopqrstuvwxyz'
  return " ".join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))

# regex using .findall()
import re

def alphabet_position(text):
    return " ".join([str(ord(i) - 96) for i in re.findall('[a-z]', text.lower())])

# regex using .sub() with search parameters
import re
def alphabet_position(text):
    return ' '.join(map(lambda x: str(ord(x) - 96), re.sub('(?i)[^a-z]', '', text.lower())))