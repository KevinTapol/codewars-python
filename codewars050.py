# Jenny's secret message
# Parameters or Edge Cases:
   # inputs will be a single word string representing a name starting with a Capital letter
# Return:
   # "Hello, my love!" if the input is "Johnny" else "Hello, <input>!"
# Examples:
   # (greet("James"), "Hello, James!")
   # (greet("Jane"), "Hello, Jane!")
   # (greet("Jim"), "Hello, Jim!")
   # greet("Johnny"), "Hello, my love!")
# Psuedo Code:
   # if the input is "Johnny" return "Hello, my love!" else "Hello, <input>!"

# my answer and best practices
def greet(name):
    # if the input is "Johnny" return "Hello, my love!" else "Hello, <input>!"
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
# my answer refactored lambda implicit return conditional
greet = lambda name: "Hello, my love!" if name == "Johnny" else "Hello, %s!"%name

print(greet("James")) # "Hello, James!"
print(greet("Jane")) # "Hello, Jane!"
print(greet("Jim")) # "Hello, Jim!"
print(greet("Johnny")) # "Hello, my love!"

# most clever
# wow I never thought about putting the conditional in the .format()
def greet(name):
    return "Hello, {name}!".format(name = ('my love' if name == 'Johnny' else name))

# using .replace() nested inside .format()
def greet(name):
    return "Hello, {name}!".format(name=name.replace("Johnny", "my love"))   

# lambda using %s for string plug in variable as a key value pair list call
greet = lambda _: "Hello, %s!"%([_,'my love'][_=='Johnny'])

# lambda with concatenation
greet = lambda name: "Hello, " + ("my love" if name == "Johnny" else name) + "!"

# using an f string same as template literals in JavaScript
def greet(name):
    return f"Hello, {'my love' if name == 'Johnny' else name}!"

# dictionary object key value .get() conditionals of input
greet=lambda n:{"Johnny":"Hello, my love!"}.get(n,"Hello, {}!".format(n))

# f string condition true n == "Johnny" list call index == 1
def greet(n):
    return (f"Hello, {n}!", "Hello, my love!")[n=="Johnny"]

# nested lambdas
def greet(name):
    return [lambda name: 'Hello, {}!'.format(name), lambda name: 'Hello, my love!'][name == 'Johnny'](name)