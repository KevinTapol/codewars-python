# Mexican Wave
"""
The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position.

The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced. (Source Wikipedia)

In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

 wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
"""
# Parameters or Edge Cases:
"""
    inputs will be a string word and always lowercase
    inputs can be empty
    inputs can have white space in between characters
"""
# Return:
"""
    an array of strings with every combination of all characters to lowercase except for 1 which rotates from first to last
"""
# Examples:
"""
    "" => 
    "hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    "two words" => ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
"""
# Pseudocode:
"""
    # declare an empty array called result
    # take in the string people and create an array with each character as an element called word
    # iterate through word
    # if the current index is not white space
    # lowercase each element in word
    # grab the current index string, uppercase it and reassign the element at that index to the uppercase string element
    # convert word into a string and append it to result
    # return result
"""

# my answer
# Here I used enumerate() because I originally thought of referencing the index and change just the element.
def wave(people):
    # declare an empty array called result
    result =[]
    # take in the string people and create an array with each character as an element called word
    word = [e for e in people]
    # iterate through word 
    for i,e in enumerate(word):
        # if the current index is not white space
        if word[i] != " ":
            # lowercase each element in word
            word = [e.lower() for e in word]
            # grab the current index string, uppercase it and reassign the element at that index to the uppercase string element
            word[i] = word[i].upper()
            # convert word into a string and append it to result
            result.append("".join(word))
    # return result
    return result

# my answer refactored
# Here I referenced the for loop by the input length instead of declaring an array for word outside of the for loop.
def wave(input):
    result =[] 
    for i in range(len(input)):
        if input[i] != " ":
            word = [e.lower() for e in input]
            word[i] = word[i].upper()
            result.append("".join(word))
    return result

print(wave("")) # []
print(wave("hello")) # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave("two words")) # ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]


# best practices and most clever
# I strongly disagree for best practices but agree for most clever.
# IMO best practices should never include a for loop inside a one liner.
# Very clever!
# Per each iteration, they are creating a copy of the input up to just before the current index, concatenating it to the current index to uppercase and concatenating an input copy after the current index to the end of the input.
# Here they used .isalpha() to check if the current index contains a character instead of checking if it not a white space.
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

# I ripped apart best practices and most clever to what I strongly agree of what best practices should have been. It is the same answer and method of thinking but easier to read.
def wave(str):
    result = []
    for i in range(len(str)):
        if str[i].isalpha():
            result.append(str[:i] + str[i].upper() + str[i+1:])
    return result

# very similar to my answer but they used list(input) to create an array of strings of the input.
def wave(words):
    result = []
    chars = list(words)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            result.append(''.join(copy))
    return result

# same idea as best practices and most clever but using .capitalize() and if the current index is not a white space
def wave(s):
    return [s[:i].lower() + s[i:].capitalize() for i in range(len(s)) if s[i] != " "]

# using f string and {} to concatenate and format each iteration of the for loop 
# same idea as creating a copy up to just before the index, uppercase the current index, and concatenate everything after the current index.
def wave(s):
    return [f'{s[:i]}{s[i].upper()}{s[i+1:]}' for i,x in enumerate(s) if x != ' ']

# you can use .isspace() instead of checking if the current index is equal to " "
def wave(s):
    return [f'{s[:i]}{s[i].upper()}{s[i+1:]}' for i in range(len(s)) if not s[i].isspace()]