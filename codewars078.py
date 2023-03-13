# Get the Middle Character
# Parameters or Edge Cases:
    # inputs will be a string can be capitalized but will be letters
    # test cases will be small so you don't need to worry about time outs 
# Return:
    # a string of the middle character. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
# Examples:
    # "test" => "es"
    # "testing" => "t"
    # "middle" => "dd"
    # "A" => "A"
# Pseudo Code:
    # if the length of the string is odd return the character at index of (length -1) / 2 since indexes start at 0 and not 1
    # if the length of the string is even return the characters at index of (length /2) -1 and length/2

# my answer
def get_middle(s):
    if len(s) % 2 -1 != 0:
        return s[len(s)//2 -1] + s[len(s)//2]
    else:
        return s[len(s)//2]
    
# my answer refactored implicit return conditionals
get_middle = lambda s: s[len(s)//2 -1] + s[len(s)//2] if len(s) % 2 -1 != 0 else s[len(s)//2]
    
print(get_middle("test")) # "es"
print(get_middle("testing")) # "t"
print(get_middle("middle")) # "dd"
print(get_middle("A")) #"A"

# best practices
# interesting use of variable declaration with divmod() function returns a tuple containing the quotient and the remainder when argument1 (dividend) is divided by argument2 (divisor).
# if odd means if odd == 1
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

# most clever
# using list start stop
# If the string has an even length say 4, then i = 1. So s[1:-1] will be the equivalent to s[1:3] which will give you the two middle letters.
# If the string has an odd length say 5, then i = 2. So s[2:-2] will be the equivalent to s[2:3] which will give you the single middle letter.
# But if the string is too short (length in the interval [0-2]) this will make i = 0, then the slice will capture no letters and return an empty string: "".
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s

# declaring variables for len() and take the int() from x/2 instead of //
import math
def get_middle(s):
    #your code here
    x = len(s)
    y = int(x/2)
    if x%2==0:
        return s[y-1:y+1]
    else:
        return s[y:y+1]
    
# while condition
def get_middle(s):
    while len(s) > 2:
        s = s[1:-1]
    return s

# cleaner version of my answer except using start stop list
def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]

# another divmod but using if not
def get_middle(s):
    q, r = divmod(len(s), 2)
    return s[q - (1 if not r else 0):q + 1]

# declaring empty list and string then using .pop() to remove and + to concat
def get_middle(input):
    letter_list = []
    letters_together = ''
    for letters in input:
        letter_list += letters
    while len(letter_list) > 2:
        letter_list.pop(0)
        letter_list.pop(-1)
    for letters_individual in letter_list:
        letters_together += letters_individual
    return letters_together