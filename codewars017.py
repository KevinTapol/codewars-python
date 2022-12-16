"""
Convert a String to a Number!
Parameters or Edge Cases:
    input will be a string representation of an integer 
    input can be negative
Return:
    integer of the input string
Examples:
    "1234" --> 1234
    "605"  --> 605
    "1405" --> 1405
    "-7" --> -7
Psuedo Code:
    return the string using the int() method
"""

# my answer and best practices
def string_to_number(s):
    return int(s)

print(string_to_number("1234")) # 1234
print(string_to_number("605")) # 605
print(string_to_number("1405")) # 1405
print(string_to_number("-7")) # -7

# my answer refactored to lambda
string_to_number = lambda s: int(s)

# most clever
string_to_number = int

# using try except block
def string_to_number(s):
    # ... your code here
    try:
        return int(s)
    except (ValueError):
        return "Input is not valid " 

# voted 2nd most clever for not using int()
def char_to_digit(s):
    if s == '0':
        return 0
    elif s == '1':
        return 1
    elif s == '2':
        return 2
    elif s == '3':
        return 3
    elif s == '4':
        return 4
    elif s == '5':
        return 5
    elif s == '6':
        return 6
    elif s == '7':
        return 7
    elif s == '8':
        return 8
    else:
        return 9
    
    
def string_to_number(s):
    if isinstance(s, int):
        return s
    
    r = 0
    for c in s:
        if c == '-':
            continue
        r = r * 10 + char_to_digit(c)
    
    return r if s[0] != '-' else -1 * r

# using eval()
"""
eval(expression, /, globals=None, locals=None)
The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.
"""
def string_to_number(s):
    return eval('{}'.format(s))

# multiple checks of the input 
def string_to_number(s):
    # Checking if it's float type
    if "." in s:
        s = float(s)
        return s
    
    # Checking if it's complex type
    elif "j" in s:
        s = complex(s)
        return s
    
    # In python we have 3 number data types, so if the last 2 cheking is false
    # the number must be int data type
    else:
        s = int(s)
        return s

    # Not necessary
    return 0

# another clever answer avoiding using int()
def string_to_number(s):
    result = 0    #Variable to hold running total of integer to return
    place = 1    #Decimal value of place currently being calculated
    i = len(s) - 1
    while i >= 0:
        digit = s[i]    #The piece of the string being transferred
        if digit == '1':
            result += place
        elif digit == '2':
            result += (2*place)
        elif digit == '3':
            result += (3*place)
        elif digit == '4':
            result += (4*place)
        elif digit == '5':
            result += (5*place)
        elif digit == '6':
            result += (6*place)
        elif digit == '7':
            result += (7*place)
        elif digit == '8':
            result += (8*place)
        elif digit == '9':
            result += (9*place)
        elif digit == '-':
            result = -result
        place *= 10
        i -= 1
        
    return result

# using regex
from re import match as m

string_to_number = lambda s: eval(s) if m(r'^[-+]?\d+$', s) else None