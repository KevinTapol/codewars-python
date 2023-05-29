# Valid Phone Number
"""
Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)
"""
# Parameters or Edge Cases:
"""
    inputs will be a string
"""
# Return:
"""
    boolean true if the string is in the format of a phone number ie '(012) 345-6789' else false
"""
# Examples:
"""
    "(123) 456-7890"  => true
    "(1111)555 2345"  => false
    "(098) 123 4567"  => false
"""
# Pseudocode:
"""
    # declare a string with the numbers 0-9 in it named x
    # if the element at index 0 is not '(' return false
    # if the element at index 4 is not ')' return false
    # if the element at index 5 is not ' ' return false
    # if the element at index 9 is not '-' return false
    # if the reaming elements are not in x return false
    # outside of the conditionals return true
"""

# my answer
def valid_phone_number(phone_number):
    # declare a string with the numbers 0-9 in it named x
    x = '0123456789'
    # iterate through the input string
    if len(phone_number) != 14:
        return False
    # if the element at index 0 is not '(' return false
    if phone_number[0] != '(':
        return False
    # if the element at index 4 is not ')' return false
    if phone_number[4] != ')':
        return False
    # if the element at index 5 is not ' ' return false
    if phone_number[5] != ' ':
        return False
    # if the element at index 8 is not '-' return false
    if phone_number[9] != '-':
        return False
    # if the reaming elements are not in x return false
    if phone_number[1] not in x or phone_number[2] not in x or phone_number[3] not in x or phone_number[6] not in x or phone_number[7] not in x or phone_number[8] not in x or phone_number[10] not in x or phone_number[11] not in x or phone_number[12] not in x or phone_number[13] not in x:
        return False
    # outside of the for loop return true
    return True

print(valid_phone_number("(123) 456-7890")) # True
print(valid_phone_number("(1111)555 2345")) # False
print(valid_phone_number("(098) 123 4567")) # False

# best practices
# using regex
def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))

# most clever
# here they are declaring a comparison string
# iterate through the input string and if the current element is an integer concatenate 'x' else concatenate the character
# check if the resulting new concatenated string is equal to the desired template for a boolean true false implicit return.
def validPhoneNumber(phoneNumber):
    number = ''
    template = '(xxx) xxx-xxxx'
    for l in phoneNumber:
        if l.isdigit():
            number += 'x'
        else:
            number += l
    
    return number == template

# another regex but using .compile()
import re
prog = re.compile('^\(\d{3}\) \d{3}-\d{4}$')
def validPhoneNumber(phone_number):
    return prog.match(phone_number) is not None

# another regex but using only .match() inside of a bool() for return
validPhoneNumber = lambda x: bool(__import__('re').match('\(\d{3}\) \d{3}-\d{4}$', x))

# regex but specifying 0-9 instead of using d{}
import re

def validPhoneNumber(phoneNumber):
    return any(re.findall("^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$", phoneNumber))

# clever way of not using regex
# same idea of boolean return for conditional statements
# iterating through the input and returning the integer 1 each time the element is numeric and sum it 
# if there are not exactly 10 integers in the input return false
# also clever that they are concatenating the index location of every special character in order and comparing it to '() -' for boolean return
def valid_phone_number(p):
    return len(p)==(14) and sum(1 for i in p if i.isnumeric())==10 and p[0]+p[4]+p[5]+p[9]=='() -'

# interesting replacing special characters with an empty space
# then creating a 2 d array of only the integers where the first 3 integers are in the 2d index 0 next 3 are at index 1 and the final 4 are at index 2
def validPhoneNumber(s):
    if s.count(' ') == s.count('-') == 1 and len(s) == 14:
        a = s.replace('(','').replace(')','').replace('-',' ')
        b = a.split()
        return [len(x) for x in b] == [3,3,4]
    return False