"""
String Repeat
Parameters or Edge Cases:
      given two inputs interger n and string s
Return:
      the string s integer n times
Examples:
      6, "I"     -> "IIIIII"
      5, "Hello" -> "HelloHelloHelloHelloHello"
Psuedo Code:
      return the product of the inputs for python but for javascript I'd have to use .repeat()
"""

# my answer, best practices and most clever
def repeat_str(repeat, string):
    return repeat*string

print(repeat_str(6,"I")) # "IIIIII"
print(repeat_str(5, "Hello")) # "HelloHelloHelloHelloHello"

# my answer refactored lambda
repeat_str = lambda repeat, string: repeat*string

# for loop using += to a declared string variable
def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution

# using lambda similar to arrow functions for javascript
repeat_str = lambda r, s: s * r

# using .join()
def repeat_str(repeat, string):
    return "".join([string]*repeat)

# using a for loop with array methods and a declared array variable
def repeat_str(repeat, string):
    hill = []
    for k in range(repeat):
        hill.append(string)
    return ''.join(hill)

# using a while loop
def repeat_str(repeat, string):
    counter = 0
    result = ''
    while counter < repeat:
        result = result + string
        counter += 1
    return result

# calling the function on itself to loop
def repeat_str(repeat, string):
    if repeat == 1 : 
        return string
    return string+repeat_str(repeat -1, string)

# another answer that calls the function on itself with an if else statement
def repeat_str(repeat, string):
    return string + repeat_str(repeat-1, string) if repeat else ''

# .mul is a method used to perform multiplication
repeat_str=__import__('operator').mul

# using int() for the integer input
def repeat_str(repeat, string):
    return string + repeat_str(repeat-1, string) if repeat else ''

# using f string
def repeat_str(repeat, string):
    return f"{string * repeat}"

# using reduce() and repeat()
import functools, itertools

def repeat_str(repeat, string):
    return functools.reduce(lambda a, b: a + b, itertools.repeat(string, repeat))