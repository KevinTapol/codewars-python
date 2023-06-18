# Make a function that does arithmetic!
"""
Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5
Try to do it without using if statements!
"""
# Parameters or Edge Cases:
"""
    input 1 and 2 will be positive integers
    input 3 will be a string representation of math operators
"""
# Return:
"""
    the result of the numbers and the math operator
"""
# Examples:
"""
    5, 2, "add"      --> 7
    5, 2, "subtract" --> 3
    5, 2, "multiply" --> 10
    5, 2, "divide"   --> 2.5
"""
# Psuedocode:
"""
    # create an object where the input strings for math are the key and the math functions are the value
    # return the a object calling the input operator key

    # also do one as switch cases matching the operator as the condition
"""

# my answer using an object call
def arithmetic(a, b, o):
    # create an object where the input strings for math are the key and the math functions are the value
    math = {'add': a + b, 'subtract': a - b, 'multiply': a * b, 'divide': a / b}
    # return the a object calling the input operator key
    return math[o]

# my answer refactored for codewars only
# Also best practices and most clever
def arithmetic(a, b, o):
    return {'add':a+b,'subtract':a-b,'multiply':a*b,'divide':a/b}[o]

# my answer refactored lambda for codewars only
arithmetic = lambda a,b,o: {'add':a+b,'subtract':a-b,'multiply':a*b,'divide':a/b}[o]

# my answer using switch case
def arithmetic(a, b, operator):
    match operator:
        case 'add':
            return a+b
        case 'subtract':
            return a-b
        case 'multiply':
            return a*b
        case 'divide':
            return a/b

print(arithmetic(5, 2, "add")) # 7
print(arithmetic(5, 2, "subtract")) # 3
print(arithmetic(5, 2, "multiply")) # 10
print(arithmetic(5, 2, "divide")) # 2.5


# using eval for string operators and .format() with object call
def arithmetic(a, b, operator):
    op = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    return eval("{} {} {}".format(a, op[operator], b))

# using .get() instead of [] for object key call
def arithmetic(a, b, operator):
    formats = {
        "add": a+b,
        "subtract": a-b,
        "divide": a/b,
        "multiply": a*b
        }
        
    return formats.get(operator)

# using if statements but the kata asked us not to
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    #your code here


# importing operator for math with object call
from operator import add, mul, sub, truediv

def arithmetic(a, b, operator):
    ops = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': truediv}
    return ops[operator](a, b)

# similar to my switch case but they included an error statement
def arithmetic(a, b, operator):
    match operator:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            return a / b
        case _:
            raise ValueError(f'Unknown type of operator: {operator}')