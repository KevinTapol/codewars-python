# Printer Errors
"""
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.
"""
# Parameters:
"""
    inputs will be strings of lowercase letters from a-z
    inputs will never be empty or null
"""
# Return:
"""
    a fraction in string format where the numerator is the total count of letters from n-z and the denominator is the length of the input
"""
# Examples:
"""
    "aaabbbbhaijjjm" => "0/14"
    "aaaxbbbbyyhwawiwjjjwwm" => "8/22"
    "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz" => "3/56"
    "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"=> "6/60"
    "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu" => "11/65"
        
"""
# Pseudocode:
"""
    # declare a string n with lowercase letters from n-z
    # declare an integer count and set it equal to 0
    # iterate through the input string and for each element that is in the declared string n add 1 to count
    # return in string format count / length of the input string
"""

# my answer
def printer_error(s):
    # declare a string n with lowercase letters from n-z
    n = 'nopqrstuvwxyz'
    # declare an integer count and set it equal to 0
    count = 0
    # iterate through the input string and for each element that is in the declared string n add 1 to count
    for e in s:
        if e in n:
            count += 1
    # return in string format count / length of the input string
    return f"{count}/{len(s)}"

# my answer refactored
# here I created an array of elements of 1's for every time the input occurs in the declared string n-z then sum it 
def printer_error(s):
    count = sum([1 for e in s if e in 'nopqrstuvwxyz' ])
    return f"{count}/{len(s)}"

# my answer refactored lambda for codewars only
printer_error = lambda s: f"{sum([1 for e in s if e in 'nopqrstuvwxyz' ])}/{len(s)}"
 
print(printer_error("aaabbbbhaijjjm")) # "0/14"
print(printer_error("aaaxbbbbyyhwawiwjjjwwm")) # "8/22"
print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")) # "3/56"
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")) # "6/60"
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu")) # "11/65" 

# best practices and most clever
# using regex and .format()
# they are replacing all letters from a-m with an empty space for the numerator with the regex function sub()
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

# same idea as best practices and most clever but using n-z instead of a-m
def printer_error(s):
    import re
    return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))

# similar to my answer declaring a string of lowercase letters but using not in with a-m instead
# also using string.format() instead of f string
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

# using ascii in comparison for integer values greater than m
def printer_error(s):
    return '{}/{}'.format(sum(color > 'm' for color in s), len(s))

# using f string and sum() with ascii integer values
def printer_error(s):
  return f"{sum(c > 'm' for c in s)}/{len(s)}"

# importing string to use ascii
import string
ERROR_CODES = string.ascii_lowercase[13:]

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x in ERROR_CODES]), len(s))

# using %s instead of .format() or f string
def printer_error(s):
    return '%s/%s' % (sum(1 for c in s if c > 'm'), len(s))