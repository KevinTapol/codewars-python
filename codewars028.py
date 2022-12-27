"""
MakeUpperCase
Parameters or Edge Cases:
    input will be a string
Return:
    return the string in uppercase
Examples:
Psuedo Code:
    use the method .upper()
    or loop through each character and use .capitalize()
    or create a ditionary key value pair for each lowercase character to their respective uppercase character
    or use ord() for UNICODE
"""

# my answer and best practices
def make_upper_case(s):
    return s.upper()

print(make_upper_case("hello")) # "HELLO"

# my answer lambda one liner
make_upper_case = lambda s: s.upper()

# voted most clever NOT USING .upper()
# they created a dictionary or object for JS for every alphabet character
def make_upper_case(s):
    upperCase = ""
    Uppercasedict = {
    "a" : "A",
    "b" : "B",
    "c" : "C",
    "d" : "D",
    "e" : "E",
    "f" : "F",
    "g" : "G",
    "h" : "H",
    "i" : "I",
    "j" : "J",
    "h" : "H",
    "i" : "I",
    "j" : "J",
    "k" : "K",
    "l" : "L",
    "m" : "M",
    "n" : "N",
    "o" : "O",
    "p" : "P",
    "q" : "Q",
    "r" : "R",
    "s" : "S",
    "t" : "T",
    "u" : "U",
    "v" : "V",
    "w" : "W",
    "x" : "X",
    "y" : "Y",
    "z" : "Z",
    " " : " ",
    "A" : "A",
    "B" : "B",
    "C" : "C",
    "D" : "D",
    "E" : "E",
    "F" : "F",
    "G" : "G",
    "H" : "H",
    "I" : "I",
    "J" : "J",
    "K" : "K",
    "L" : "L",
    "M" : "M",
    "N" : "N",
    "O" : "O",
    "P" : "P",
    "Q" : "Q",
    "R" : "R",
    "S" : "S",
    "T" : "T",
    "U" : "U",
    "V" : "V",
    "W" : "W",
    "X" : "X",
    "Y" : "Y",
    "Z" : "Z",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "0" : "0",
    "!" : "!",
    "," : ",",
    "." : ".",
    }
    list(s)
    for i in (s):
        upperCase = upperCase + Uppercasedict[i]
    return upperCase

# using .capitalize() for each element
def make_upper_case(s):
    return "".join(i.capitalize() for i in s)

# checking if input is a string
def make_upper_case(s):
    if isinstance(s,str):
        return s.upper()
    else:
        return

# using ord() for UNICODE 
# ord() Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

# chr() Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord(). The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.
def make_upper_case(s):
    return ''.join(chr(ord(ch) - 32) if ord(ch) in range(97, 123) else ch for ch in s)

# using ord() and functions
def inrange(a,b,x):
    if x>=a and x<=b:
        return True
    else:
        return False
def make_upper_case(s):
    ans=""
    for x in s:
        if inrange(ord('a'),ord('z'),ord(x)):
            x=chr(ord('A')+(ord(x)-ord('a')))
        ans=ans+x
    return ans

# using a string as representation then converting to a list
# zip(*iterables, strict=False) Iterate over several iterables in parallel, producing tuples with an item from each one.
# dict() Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.
def make_upper_case(s):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowers_list = [l for l in lowers]
    uppers_list = [l for l in uppers]
    dictio = dict(zip(lowers_list, uppers_list))
    output = ''
    for letter in s:
        if letter not in lowers:
            output += letter
        else:
            output += dictio[letter]
    return output

# ascii lower to upper
from string import ascii_lowercase, ascii_uppercase

def make_upper_case(s):
    return s.translate(str.maketrans(ascii_lowercase, ascii_uppercase))