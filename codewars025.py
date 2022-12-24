"""
Abbreviate a Two Word Name
Parameters or Edge Cases:
    inputs will be two string words with one space in between them
    output must be two capital letters with a dot separating them
Return:
    a string of two capital letters with a dot separating them
Examples:
    ("Sam Harris"), "S.H")
    ("patrick feenan"), "P.F")
    ("Evan C"), "E.C")
    ("P Favuzzi"), "P.F")
    ("David Mendieta"), "D.M")
Psuedo Code:
    uppercase the string and split() it at the space
    grab the first character of each element with f string  them and concat them with '.'
    return the new string
"""

# my answer
def abbrev_name(name):
    # uppercase the string and split() it at the space
    x = name.upper().split()
    # grab the first character of each element with f string  them and concat them with '.'
    return f"{x[0][0]}.{x[1][0]}"

print(abbrev_name("Sam Harris")) # "S.H"
print(abbrev_name("patrick feenan")) # "P.F"
print(abbrev_name("Evan C")) # "E.C"
print(abbrev_name("P Favuzzi")) # "P.F"
print(abbrev_name("David Mendieta")) # "D.M"

# best practices and most clever
# split the input at the empty space
# loop through and grab the first index of each element
# join on '.' and uppercase the string
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

# upper case the input and split the string into elements at each space
# declaring multiple variables in one line of each element
# concat the first variable first index variable with '.' with the next variable first index
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

# the only difference here from best practices is uppercase each first index element instead of uppercase the final return
def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())

# brute force for loop
def abbrevName(name):
    first_initial = name[0]
    for letter in range(len(name)):
        if name[letter]  == ' ':
            last_initial = name[letter + 1]
          
    return (first_initial.upper() + "." + last_initial.upper())

# using boolean isupper() and title() to upper case instead of upper() with filter()
def abbrevName(name):
    return '.'.join(filter(str.isupper,name.title()))

# creating a new list grab the first index and the index after the space 
# concat them with "." and upper case it with .title()
def abbrevName(name):
    return name[:1].title() + "." + name[name.find(' ')+1].title()

# declare a new list and append the first indexes to the list and join on "."
def abbrevName(name):
    L=[]
    a = name.split(" ")
    for i in a:
        L.append(i[0].upper())
    return ".".join(L)

# nice comments
def abbrev_name(name):
    # Convert name to uppercase
    uppername = name.upper()
    # Split string
    words = uppername.split()
    # Get first letters
    letters = [word[0] for word in words]
    # Return + join letters with a seperating "."
    return (".".join(letters))