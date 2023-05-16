# Parse nice int from char problem
"""
You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.
"""
# Parameters or Edge Cases:
"""
    input will be a string 
"""
# Return:
"""
    the first character in the string as an integer
"""
# Examples:
"""
    # "2 years old" => 2
    # "4 years old" => 4
    # "5 years old" => 5
    # "7 years old" => 7
"""
# Pseudocode:
"""
    return index 0 of the input as an integer
"""

# my answer best practices and most clever
def get_age(age):
    return int(age[0])

# my answer refactored implicit return
get_age = lambda age: int(age[0])

# checking if the first index is an integer in string format then return it as a integer
def get_age(age):
    for x in age:
    	if x.isdigit():
        	return int(x) 
        
# using regex
import re

def get_age(age):
    return int(re.search(r"\d+", age).group())

# lol using split on the first index and convert it into an integer
def get_age(age):
    return int(age.split()[0])

# filtering through the input where there is an integer in string format and return it as an integer
def get_age(age):
    return int(''.join(filter(str.isdigit, age)))

# regex but based on format of the input
import re

def get_age(age):
    return int(re.match(pattern=r'(?P<age_char>^\d.)', string=age).group("age_char"))

# regex but returning based on 0-9
import re
def get_age(age):
    return int(re.sub('[^0-9]','',age))