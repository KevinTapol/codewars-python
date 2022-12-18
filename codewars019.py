"""
Return Strings
Parameters or Edge Cases:
    input will be a string representing a name
Return:
    a string greeting using the input name "Hello, <name> how are you doing today?"
Examples:
    (greet('Ryan'), "Hello, Ryan how are you doing today?")
    (greet('Shingles'), "Hello, Shingles how are you doing today?")
Psuedo Code:
    use an f string for python similar to template literals `` for JS to return an input in a string
"""

# my answer best practices and most clever
def greet(name):
    return f"Hello, {name} how are you doing today?"

print(greet('Ryan')) # "Hello, Ryan how are you doing today?"
print(greet('Shingles')) # "Hello, Shingles how are you doing today?"

# my answer refactored lambda 
greet = lambda name: f"Hello, {name} how are you doing today?"

# using .format() to pass in the argument
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

# lambda using .format()
greet = "Hello, {0} how are you doing today?".format

# using + to concatenate
def greet(name):
    return "Hello, " + name + " how are you doing today?"

# using %s as a place holder for name and then passing in % argument
def greet(name):
    return "Hello, %s how are you doing today?" % name

# using .replace() for the input
def greet(name):
    return "Hello, <name> how are you doing today?".replace('<name>',name)

# when greet is called it creates a new object using the class Hello as the argument passed in that has a method returning an f string with the object name
class Hello:
    
    def __init__(self,name):
        self.name = name
        
    def say_hello(self):
        return f'Hello, {self.name} how are you doing today?'


def greet(name):
    return Hello(name).say_hello()

# using slice and concatenation
def greet(name):
    il = "Hello,  how are you doing today?"
    soup = il[:7] + name + il[7:]
    return soup

# using "".join(argument)
def greet(name):
    name_str="".join(name)
    return "Hello, "+name_str+" how are you doing today?"