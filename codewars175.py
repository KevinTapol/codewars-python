# Give me a Diamond
"""
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"
A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"
"""
# Parameters or Edge Cases:
"""
    inputs will be integers and can be positive or negative
    can they be empty or null?
"""
# Return:
"""
    if the input is an odd integer return a string representing a diamond with * and \n for new line else return None
"""
# Examples:
"""
    1 => "*\n"
    2 => None
    3 => # " *\n***\n *\n"
    5 => "  *\n ***\n*****\n ***\n  *\n"
    0 => None
    -3 => None
"""
# Psuedocode:
"""
    # if n is less than 0 or even return None
    # declare an empty to concat to
    # to get the top to middle of the diamond iterate starting at 1 stopping at n+2 to include n and step by 2
    # concat to result the product of ' ' and (n - current index) divided by 2 but only take the integer using //
    # concat to result the product of '*' and current index
    # concat to result '\n\'
    # to get the middle to bottom with middle excluded of diamond iterate starting from n -2 stopping at 0 and stepping by -2 and keep the same concat formulas
    # concat to result the product
    # return result
"""

# my answer
def diamond(n):
    # if n is less than 0 or even return None
    if n < 0 or n % 2 == 0:
        return None
    # declare an empty to concat to
    result = ""
    # to get the top to middle of the diamond iterate starting at 1 stopping at n+2 to include n and step by 2
    for i in range(1, n + 2, 2):
        # concat to result the product of ' ' and (n - current index) divided by 2 but only take the integer using //
        result += " " * ((n - i) // 2)
        # concat to result the product of '*' and current index
        result += "*" * i
        # concat to result '\n\'
        result += "\n"
    # to get the middle to bottom with middle excluded of diamond iterate starting from n -2 stopping at 0 and stepping by -2 and keep the same concat formulas
    for i in range(n - 2, 0, -2):
        # concat to result the product
        result += " " * ((n - i) // 2)
        result += "*" * i
        result += "\n"
    # return result
    return result

print(diamond(-1))  # None
print(diamond(0))  # None
print(diamond(1))  # "*\n"
print(diamond(2))  # None
print(diamond(3))  # " *\n***\n *\n"
print(diamond(4))  # None
print(diamond(5))  # "  *\n ***\n*****\n ***\n  *\n"

# best practices 
# here they are iterating only once generating a diamond top to bottom using absolute value in their equations
def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n//2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None
    
# here they are declaring an array generating the top to the middle but middle exclusive to the diamond
# then creating an array copy including the middle diamond and converting into a string and concatenating it
def diamond(n):
    if not n%2 or n<1: return None
    d = [" "*i+"*"*(n-2*i)+"\n" for i in range(n//2,0,-1)]
    return ''.join(d) + "*"*n + "\n" + ''.join(d[::-1])

# same idea as my answer with double for loops stepping by 2 but using arrays and .extend() then converting to string and concatenating
def diamond(n):
    if n % 2 == 0 or n < 1: return None
    d = [' ' * ((n-i)//2) + '*' * i for i in range(1, n, 2)]
    d.extend([' ' * ((n-i)//2) + '*' * i for i in range(n, 0, -2)])
    return '\n'.join(d) + '\n'

# while loop
def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    
    result = "*" * n + "\n"
    spaces = 1
    n = n - 2
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces = spaces + 1
        n = n - 2
        result = current + result + current
    
    return result

# while loop similar to my answer
def diamond(n):
    w = ''
    space = n//2
    starnum = 1
    while starnum < n:
        w += space * ' ' + starnum * '*' + '\n'
        starnum += 2
        space -= 1
    while starnum > 0:
        w += space * ' ' + starnum * '*' + '\n'
        starnum -= 2
        space += 1
    return w if n%2 != 0 and n > 0 else None

# creating separate functions to call inside the for loop
def diamond(n):
    if n%2 == 0 or n <= 0:                        # validate input
        return None
    diamond = "";                                 # initialize diamond string
    for i in range(n):                            # loop diamond section lines
        length = getLength(i, n)                  # get length of diamond section
        diamond += getLine(length, n)             # generate diamond line
    return diamond
    
def getLine(len, max):
    spaces = (max-len)//2                         # compute number of leading spaces
    return (" " * spaces) + ("*" * len) + "\n"    # create line
    
def getLength(index, max):
    distance = abs(max//2 - index)                # find distance from center (max length)
    return max - distance*2                       # compute length of diamond section

# best practices rewritten
def diamond(n):
    if n > 0 and n % 2 == 1:
        return ''.join(' ' * abs((n/2) - i) + '*' * (n - abs((n-1) - 2 * i)) + '\n' for i in range(n))
    return None