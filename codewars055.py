# Grasshopper-Personalized Message
# Parameters or Edge Cases:
    # input will be 2 string names 
    # first input will be guest and second will be owner
    # string will not be empty
# Return:
    # "Hello boss" if both inputs are equal else "Hello guest"
# Examples:
    # greet('Daniel', 'Daniel'), # 'Hello boss'
    # greet('Greg', 'Daniel'), # 'Hello guest'
# Psuedo Code:
    # if both inputs are equal return string "Hello boss" else "Hello guest"

# my answer
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
    
# my refactored lambda implicit return conditional 
greet = lambda n, o:"Hello boss" if n == o else "Hello guest"
    
print(greet('Daniel', 'Daniel')) # 'Hello boss'
print(greet('Greg', 'Daniel')) # 'Hello guest'

# best practices
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

# most clever
def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")

# using list start at if n == 0 returns true then start at 1 and step/increment by 2
# if false start at 0 and step/increment by 2
greet=lambda n,o:'Hello '+'gbuoessst'[n==o::2]

# truthy/falsy
# same idea of name == owner is true then it evaluates to 1 calling index 1 which is 'boss' and concat to "Hello"
# if false then it evaluates to 0 calling index 0 which is "guest" and concat to "Hello"
def greet(name, owner):
    return 'Hello '+['guest','boss'][name==owner]

# using f string with nested conditional
def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"

# using .format and truthy falsy index call
greet = lambda n,o: "Hello {}".format(["guest","boss"][n==o])

# using %s instead of f string or .format with a nested conditional
def greet(name, owner):
    return 'Hello %s' %('boss' if name==owner else 'guest')

# using not equals for to reverse the list index location call
def greet(name, owner):
    return ("Hello boss", "Hello guest")[name != owner]