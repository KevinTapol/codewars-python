"""
Convert a Boolean to a String
Parameters or Edge Cases:
    inputs will be boolean True or False
Return:
    string representation of the boolean input
Examples:
    True -> "True"
    False -> "False"
Psuedo Code:
    take in the input boolean and return it as a string using str()

"""

# my answer best practices and most clever
def boolean_to_string(b):
    return str(b)

print(boolean_to_string(True)) # "True"
print(boolean_to_string(False)) # "False"

# my answer refactored lambda one liner
boolean_to_string = lambda b: str(b)

# popular clever answer
# I keep forgetting that this is possible in Python.
boolean_to_string = str

# using .__str__()
def boolean_to_string(b):
    return b.__str__()

# using if else
def boolean_to_string(b):
    return 'True' if b else 'False'

# lambda if else
boolean_to_string = lambda x: "True" if x else "False"

# creating a list and calling the element with truthy index location similar to array for Javascript
def boolean_to_string(b):
    return ('False', 'True')[b]

# lambda list
boolean_to_string = lambda b : ["False", "True"][b];

# using f string as a return similar to template literals for JavaScript
def boolean_to_string(b):
    return f"{b}"

# using object key value pair and calling it with the input key
def boolean_to_string(b):
    d = {True : "True", False : "False"}
    return d[b]

# using *
def boolean_to_string(b):
    return b*"True" or "False"

# using format()
def boolean_to_string(b):
    return format(b)