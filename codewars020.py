"""
Basic Mathematical Operations
Parameters or Edge Cases:
    first input will be a string representation of + - * /
    second and third inputs will be integers
Return:
    the result of applying input math function
Examples:
    ('+', 4, 7) --> 11
    ('-', 15, 18) --> -3
    ('*', 5, 5) --> 25
    ('/', 49, 7) --> 7
Psuedo Code:
    create conditional statements checking the input and returning the math function 
"""

# my answer
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return "Operator unknown"

print(basic_op('+', 4, 7)) # 11
print(basic_op('-', 15, 18)) # -3
print(basic_op('*', 5, 5)) # 25
print(basic_op('/', 49, 7)) # 7


# best practices was only if statements
def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

# most clever using eval() and .format()
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

# using a dictionary key value pair call on operator
def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)

# using eval()  
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

# eval() and f string
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

# using a dictionary key value pair with lambdas as the value
def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b, 
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)

# importing math operators
from operator import add, div, mul, sub

def basic_op(op, a, b):
    return {'+': add, '/': div, '*': mul, '-': sub}[op](a, b)

# one liner lambda using eval() ans str()
basic_op = lambda o,a,b: eval(str(a)+o+str(b))

# switch cases for JS are match cases for Python
def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            return value1 / value2

# using one liner conditionals
def basic_op(op, v1, v2):
    return v1+v2 if op == "+" else v1-v2 if op == "-" else  v1*v2 if op == "*" else  v1/v2

# creating a dictionary and importing math as dot notation
import operator as op

OPERATIONS = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.div,
}

def basic_op(operator, value1, value2):
    return OPERATIONS[operator](value1, value2)

# one liner lambda importing math operator creating a dictionary and calling it based on input key o
basic_op = lambda o, v1, v2: __import__("operator").__dict__[{"+":"add","-":"sub", "*":"mul", "/":"truediv"}[o]](v1,v2)