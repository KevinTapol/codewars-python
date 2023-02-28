# Remove exclamation marks
# Parameters or Edge Cases:
    # inputs will be strings and can be empty
# Return:
    # the input string without '!'
# Examples:
    #  ("Hello World!") => "Hello World"
    #  ("Hello World!!!") => "Hello World"
    #  ("Hi! Hello!") => "Hi Hello"
    #  ("") => ""
    #  ("Oh, no!!!") => "Oh, no"
# Pseudo Code:
    # iterate through the input string and if it contains '!' replace every instance with an empty string ''
    # return the new string

# my answer
def remove_exclamation_marks(s):
    n = []
    for e in s:
        if e != "!":
            n.append(e)
    return ''.join(n)
    
# my answer refactored implicit return 
remove_exclamation_marks = lambda s: ''.join([e for e in s if e != '!'])

print(remove_exclamation_marks("Hello World!")) # "Hello World"
print(remove_exclamation_marks("Hello World!!!")) # "Hello World"
print(remove_exclamation_marks("Hi! Hello!")) # "Hi Hello"
print(remove_exclamation_marks("")) # ""
print(remove_exclamation_marks("Oh, no!!!")) # "Oh, no"


# best practices and most clever
# I completely forgot about .replace()
def remove_exclamation_marks(s):
    return s.replace('!', '')

# creating an empty string and concat with +=
def remove_exclamation_marks(s):
    """ return s.replace('!', '') """
    new_s = ''
    for i in s:
        if i != '!':
            new_s += i
    return new_s

# split() on character(s) to omit and join back on the array created by the split()
def remove_exclamation_marks(s):
    a = s.split("!")
    s = ("").join(a)
    return s

# using .strip() to remove '!'
# also nesting a lambda inside map()
def remove_exclamation_marks(s):
    return ''.join(list((map(lambda x:x.strip('!'), list(s)))))

# using not in instead of in
def remove_exclamation_marks(s):
    lst = [i for i in s if i not in '!+(?=.*\!)']
    return ''.join(lst)

# using regex
def remove_exclamation_marks(s):
    return re.sub(r'!', '', s)

# another regex but a bit cleaner
import re

def remove_exclamation_marks(s):
    return re.sub('[\!]','',s)

# using split() on '!' then join the array back into a string
def remove_exclamation_marks(s):
    return ''.join(i for i in s.split('!'))

# using while element in list()
def remove_exclamation_marks(s):
    temp = list(s)
    while '!' in temp:
        temp.remove('!')
    return ''.join(temp)   

# lambda with a filter() with a nested lambda
remove_exclamation_marks=lambda s: ''.join(list(filter(lambda x: x != '!', s)))

# .find()
def remove_exclamation_marks(s):
    exclamation = '!?'
    res = ''
    
    for i in s:
        if (exclamation.find(i) < 0):
            res += i
    return res

# while condition with .count()
def remove_exclamation_marks(s):
    #your code here
    s = list(map(str,s))
    i=0
    while i < s.count("!"):
        s.remove('!')
    return "".join(s)

# nesting .find() in .replace()
def remove_exclamation_marks(s):
    while s.find("!") != -1:
        s = s.replace(s[s.find("!")], "")
    return s