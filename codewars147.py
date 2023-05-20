# Roman Numerals Decoder
"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
"""
# Parameters or Edge Cases:
"""
    inputs will be a Roman Numeral string with a combination of the following capital letters 'IVXLCDM'
    Symbol    Value
    I          1
    V          5
    X          10
    L          50
    C          100
    D          500
    M          1,000
"""
# Return:
"""
    the integer equivalent to the roman numeral string input
"""
# Examples:
"""
    'XXI' => 21
    'MCMXC' =>  1990
    'MMVIII' =>  2008
    'MDCLXVI' =>  1666
    'M' => 1000

"""
# Pseudocode:
"""
# create a dictionary/object for each roman numeral letter as the key and the year as the value named roman_year
# take in the input string, reverse it, convert the string into an array with each element as a string letter and declare it as a variable r_input
# declare an integer equal to 0 representing the current value of the element as a key from the dictionary/object roman_year
# declare an integer equal to 0 representing the current total for year
# iterate the the array r_input
# if last equals 0
# add the current elements value from the dictionary/object roman_year to year
# if last is greater than the value of the current element from the dictionary/object roman_year 
# subtract the value from year
# else
# add the current elements value from the dictionary/object roman_year to year
# reassign last equal to the value of the current element as a key from the dictionary/object roman_year
# return the total year
"""

# my answer
def solution(input):
    # create a dictionary/object for each roman numeral letter as the key and the year as the value named roman_year
    roman_year = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    # take in the input string, reverse it, convert the string into an array with each element as a string letter and declare it as a variable r_input
    r_input = list(input[::-1])
    # declare an integer equal to 0 representing the current value of the element as a key from the dictionary/object roman_year
    last = 0
    # declare an integer equal to 0 representing the current total for year
    year = 0
    # iterate the the array r_input
    for e in r_input:
        # if last equals 0
        if last == 0:
            # add the current elements value from the dictionary/object roman_year to year
            year += roman_year[e]
        # if last is greater than the value of the current element from the dictionary/object roman_year 
        elif last > roman_year[e]:
            # subtract the value from year
            year -= roman_year[e]
        # else
        else:
            # add the current elements value from the dictionary/object roman_year to year
            year += roman_year[e]
        # reassign last equal to the value of the current element as a key from the dictionary/object roman_year
        last = roman_year[e]
    # return the total year
    return year

# my answer refactored 
# declaring all my variables in one line
def solution(input):
    last, year, r_input, roman_year = 0, 0, list(input[::-1]), {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    for e in r_input:
        if last == 0:
            year += roman_year[e]
        elif last > roman_year[e]:
            year -= roman_year[e]
        else:
            year += roman_year[e]
        last = roman_year[e]
    return year

print(solution('MCMXC')) #  1990
print(solution('MMVIII')) #  2008
print(solution('MDCLXVI')) #  1666
print(solution('M')) # 1000

# best practices
# similar to my answer but cleaner to ready the variable declarations and not declaring a variable for the input reversed and converted to a list
def solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total

# voted most clever was an array of every single combination of roman numerals where the letters where the key and the integer year was the value
# funny but strongly disagree

# created a list of tuples instead of a dictionary
# iterating through the 2d array where s is the letters and v is the numbers
# take the input and return the current count of the current index multiplied by the current element
# sum the result
values = [('M', 1000), ('CM', -200), ('D', 500), ('CD', -200),
          ('C', 100), ('XC', -20), ('L', 50), ('XL', -20),
          ('X', 10), ('IX', -2), ('V', 5), ('IV', -2),
          ('I', 1)]
def solution(roman):
    return sum(roman.count(s)*v for s,v in values)

# recursion
# here they are using if not input meaning 0 or null
# 2d array is a tuple of a tuple which runs faster because it's immutable
# I love this answer because it takes care of combinations of 4 and 9.
# Here they are checking if the input string starts with the current key letters then return the key value and using recursion reassigning the input to the current input iteration
SYMBOLS = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
)

def solution(input):
    if not input:
        return 0
    for char, value in SYMBOLS:
        if input.startswith(char):
            return value + solution(input[len(char):])