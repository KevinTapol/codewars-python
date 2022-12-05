# Parameters or Edge Cases: inputs are strings
# Return: reversed input strings
# Examples: 'world'  =>  'dlrow'
#           'word'   =>  'drow'
# Psuedo Code: simple method start stop step but this starts at the end if values of start and stop are empty and steps by -1
# side note in js I would .split('') but you CANNOT split by individual character strings. This throws an error. The method .reverse() works with strings too.

# my answer best practices and most clever
def solution(string):
    return string[::-1]

print(solution("world")) # "dlrow"
print(solution("word")) # "drow"
print(solution("string")) # "gnirts"
print(solution("racecar")) # "racecar"

# using lambda reminds me of an arrow function
solution = lambda s: s[::-1]

# define variables then use a for loop
def solution(string):
    newstring = ""
    letter = len(string) - 1
    for x in string:
        x = string[letter]
        newstring = newstring + x
        letter = letter -1 
    return newstring

# simple for loop
def solution(string):
    word = ''
    for i in range(len(string)):
        word += string[(-1-i)]
    return word

# using .reverse() and .join() and instead of .split() use list(string)
# if I want to split a string into individual character elements in an array use list(string)
def solution(string):
    temp = list(string)
    temp.reverse()
    return ''.join(temp)

# reversing the string using a for loop and the length method len()
def solution(string):
    s = list(string)
    j = len(s)-1
    for i in range(len(s)):
        if (i<j):
            s[i], s[j] = s[j], s[i]
            j = j-1
        else:
            continue
    s1 = ''.join(s)
    return s1

# reversed is a built-in function in Python used to get a reversed iterator of a sequence. reversed function is similar to the iter() method but in reverse order
def solution(string):
    return ''.join(i for i in reversed(string))

# declare empty string loop through input string and reassign to empty string
def solution(string):
    s1=''
    for x in string:
        s1= x+s1
    return s1 