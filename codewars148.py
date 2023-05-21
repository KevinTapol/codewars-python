# WeIrD StRiNg CaSe
"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
"""
# Parameters or Edge Cases:
"""
    inputs will be a string of word or words separated by a single space
    will inputs be empty
"""
# Return:
"""
    the input string with each word letter starting as uppercase and alternating to lowercase
"""
# Examples:
"""
    'String' => 'StRiNg'
    'Weird string case' => 'WeIrD StRiNg CaSe'
"""
# Pseudocode:
"""
# declare an empty array result to append each word to
# take in the input and convert it into an array splitting on white space
# iterate through each word in the array
# locally declare an empty string per each iteration of word to concatenate to
# iterate through the word
# if the index is even
# concat the current element as uppercase to z
# if the index is odd
# concat the current element as lowercase to z
# inside the word for loop append each word to the array result
# outside of the nested for loops convert result into a string joining each element with a white space
# return result
"""
# my answer
def to_weird_case(input):
    # declare an empty array result to append each word to
    result = []
    # take in the input and convert it into an array splitting on white space
    sentence = input.split()
    # iterate through each word in the array
    for word in sentence:
        # locally declare an empty string per each iteration of word to concatenate to
        z = ""
        # iterate through the word
        for i in range(len(word)):
            # if the index is even
            if i % 2 == 0:
                # concat the current element as uppercase to z
                z +=  word[i].upper()
            # if the index is odd
            else:
                # concat the current element as lowercase to z
                z += word[i].lower()
        # inside the word for loop append each word to the array result
        result.append(z)
    # outside of the nested for loops convert result into a string joining each element with a white space
    result = " ".join(result)
    # return result
    return result

# my answer refactored
def to_weird_case(input):
    result = []
    arr = input.split()
    for word in arr:
        z = ""
        for i in range(len(word)):
            if i % 2 == 0:
                z +=  word[i].upper()
            else:
                z += word[i].lower()
        result.append(z)
    return " ".join(result)

print(to_weird_case('String')) # 'StRiNg'
print(to_weird_case('THIs iS a TEST')) # 'ThIs Is A TeSt'

# best practices and most clever
# declared separate functions but executing the exact same logic as my answer
def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())

# single for loop of nested conditionals
# keeping the input as a string all through the code and declaring a count for the current index
def to_weird_case(string):
    count = 0
    result = ''
    for letter in string:
        if letter == ' ':
            result += ' '
            count = 0 # reset the pattern at the start of a new word
        else:
            if count % 2 != 0: # odd letters are lower
                letter = letter.lower()
                result += letter
            else: # even letters are upper
                letter = letter.upper()
                result += letter
            count += 1
    return result

# same idea as best practices but using an implicit return lambda inside of the function instead of calling a function 
def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])

# one liner of best practices
def to_weird_case(string):
    return ' '.join([''.join([y.lower() if i%2 else y.upper() for i, y in enumerate(x)]) for x in string.split()])

# using a boolean instead of a count
def to_weird_case(string):
    newstring = ''
    i = True
    for char in string:
        if i == True:
            newstring += char.upper()
            i = False
        elif i == False:
            newstring += char.lower()
            i = True
        if char == " ":
            newstring += ""
            i = True
    return newstring

# same idea as best practices but using map() instead of for loop
def to_weird_case(string):
    return ' '.join(
      map(
        lambda w: ''.join(l.lower() if i%2 else l.upper() for i,l in enumerate(w)),
        string.split()
      )
    )