# Split Strings
"""
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it  should replace the missing second character of the final pair with an underscore ('_').
"""
# Parameters or Edge Cases:
"""
    Inputs will be a string of lowercase letters only and no white space in-between them
    the string can be empty
"""
# Return:
"""
    an array with each index holding 2 string characters and if the length is odd then add an underscore to the last character to make it an even pair
"""
# Examples:
"""* 
    'abc' =>  ['ab', 'c_']
    'abcdef' => ['ab', 'cd', 'ef']
    "" => []
    "x" => ["x_"]
"""
# Pseudocode:
"""
    -declare an empty array
    -create a string copy
    -if the length of the input string is odd then concat '_' to the copy
    -iterate through the input string
    -for the current iteration append the current element and the next element as a string pair to the empty array
    return the array
"""

# my answer
def solution(s):
    # declare an empty array
    result = []
    # create a string copy
    x = s[:]
    # if the length of the input string is odd then concat '_' to the copy
    if len(s) % 2 != 0:
        x += '_'
    # iterate through the input string
    for i in range(0,len(x), 2):
        # for the current iteration append the current element and the next element as a string pair to the empty array
        result = result + [x[i] + x[i+1]]
    # return the array    
    return result

# my answer refactored
def solution(s):
    x = s[:]
    if len(s) % 2 != 0:
        x += '_'
    return [x[i] + x[i+1] for i in range(0,len(x), 2)]

# my answer refactored one liner basing my if else conditions on the current iteration of the index range instead of the length of the input string being odd or even
def solution(s):
    return [s[i] + s[i+1] if i < len(s) - 1 else s[-1] + "_" for i in range(0, len(s), 2)]

# my answer further refactored to an implicit return lambda
solution = lambda s : [s[i] + s[i+1] if i < len(s) - 1 else s[-1] + "_" for i in range(0, len(s), 2)]


print(solution('abc')) # ['ab', 'c_']
print(solution('abcdef')) # ['ab', 'cd', 'ef']
print(solution("")) # []
print(solution("x")) # ["x_"]

# best practices
# here they appended s[i:i+2] instead of concatenating the result of s[i] + s[i+1] 
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

# most clever is regex
# The dot character "." matches any character except for a newline.
# The curly braces "{2}" specify that the preceding pattern (the dot character) should be matched exactly two times.
# In the code, the function adds an underscore "_" to the end of the input string "s". This is done to ensure that any remaining characters in the string that are not matched by the pattern are included in the output.
# Finally, the re.findall() function is called with the pattern and the modified input string as arguments. This function returns a list of all non-overlapping matches of the pattern in the input string, which are exactly two characters in this case.
import re

def solution(s):
    return re.findall(".{2}", s + "_")

# brilliant answer for codewars scenario
# here they are basing their if else conditionals on the current iteration comparison to the length of the input string 
def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

# same answer but deconstructed
def solution(s):
    result = []
    for x in range(0, len(s), 2):
        if x < len(s) - 1:
            result = result + [s[x:x+2]]
        else:
            result = result + [s[-1] + "_"]
    return result

# (s + '_') operation is made every cycle step concatenating "_" each time
# So, very short code but very large operation cycle
def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

# same as most clever but using '..' to match any 2 characters instead of ".{2}"
import re

def solution(s):
    return re.findall('..', s + '_')