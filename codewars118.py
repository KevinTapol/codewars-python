# Convert string to camel case
"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized."""
# Parameters or Edge Cases:
    # inputs will be a string of words separated by either dash - or underscore_
    # the first word may or may not be capitalized
    # Will the other letters be capitalized mid word? if so then lowercase all but the first letter of each word
    # the input can be empty
# Return:
    # snakeCase if the first word in the string is lowercase PascalCase if the first word in the string is uppercase
# Examples:
    # "the-stealth-warrior" => "theStealthWarrior"
    # "The_Stealth_Warrior" => "TheStealthWarrior"
    # "The_Stealth-Warrior" => "TheStealthWarrior"
# Pseudocode:
    # declare an empty string variable named x
    # if the input string contains dash or - replace it with underscore _ so that all separators are underscore _
    # split the string into an array of elements at underscore _
    # remove the first element of the array and set x equal to the element with pop
    # iterate through the array capitalizing each element
    # convert the array into a string
    # concat the new string to the previously removed first index element assigned to x
    # return the new string
# my answer
def to_camel_case(text):
    # declare an empty string variable named x
    x = ""
    # if the input string contains dash or - replace it with underscore _ so that all separators are underscore _
    s = text.replace("-", "_")
    # split the string into an array of elements at underscore _
    s = s.split("_")
    # remove the first element of the array and set x equal to the element with pop
    x = s.pop(0)
    # iterate through the array capitalizing each element
    s = list(map(lambda p: p.capitalize(), s))
    # convert the array into a string
    s = "".join(s)
    # concat the new string to the previously removed first index element assigned to x
    s = x + s 
    # return the new string
    return s

# my answer refactored
def to_camel_case(text):
    s = text.replace("-", "_").split("_")
    return s.pop(0) + "".join(list(map(lambda p: p.capitalize(), s)))

# my answer refactored using index call instead of .pop()
def to_camel_case(text):
    s = text.replace("-", "_").split("_")
    return s[0] + "".join(list(map(lambda p: p.capitalize(), s))[1:])

# my answer refactored implicit return one liner
to_camel_case = lambda text: text.replace("-", "_").split("_")[0] + "".join(list(map(lambda p: p.capitalize(), text.replace("-", "_").split("_")))[1:])

print(to_camel_case("the-stealth-warrior")) # "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior")) # "TheStealthWarrior"
print(to_camel_case("The_Stealth-Warrior")) # "TheStealthWarrior"

# best practices
# here they are replacing both "_" and "-" with " " instead of making them either all "_" or "-". Also they use index 0 instead of pop.
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

# most clever
# grabbing the first element with [:1] and concatenating starting at the 2nd element and on with [1:] while using .title() 
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

# using regex
import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)

# using .title() instead of .capitalize()
def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])

# brute force for loop
def to_camel_case(text):
    cap = False
    newText = ''
    for t in text:
        if t == '_' or t == '-':
            cap = True
            continue
        else:
            if cap == True:
                t = t.upper()
            newText = newText + t
            cap = False
    return newText

# in line for element in string with conditionals
def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''

# another regex
import re
def to_camel_case(text):
    arr = re.split('-|_', text)
    return ''.join(arr[:1] + [t.title() for t in arr[1:]])

# using enumerate() to get the index and element
def to_camel_case(text):
    return "".join([i if n==0 else i.capitalize() for n,i in enumerate(text.replace("-","_").split("_"))])