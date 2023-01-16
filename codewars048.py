# Sentence Smash
# Parameters or Edge Cases:
#     inputs will be an array/list of strings
#     array can be empty and if so, return an empty string ""
#     if the array/list has only 1 word then return that word with no spaces as a string
# Return:
#     a single string with a space in-between each element of the array/list of strings
# Examples:
#     (smash(['hello', 'world', 'this', 'is', 'great'])) # 'hello world this is great'
#     (smash([])) # ''
#     (smash(["hello"])) # "hello"
#     (smash(["hello", "world"])) # "hello world"
#     (smash(["hello", "amazing", "world"])) # "hello amazing world"
#     (smash(["this", "is", "a", "really", "long", "sentence"])) # "this is a really long sentence"
# Psuedo Code:
#     if the array is null or empty, return an empty string no space ''
#     join the array/list into a string joining on a space
#     return the string

# my answer
def smash(words):
    # if the array is null or empty, return an empty string no space ''
    # if len(words) == 0:
    if not words:
        return ''
    else:
        return " ".join(words)
# my answer refactored because " ".join(words) implicitly accounts for [] 
# turned out to be best practice
def smash(words):
    return " ".join(words)

# my answer further refactored to lambda one liner
smash = lambda words: " ".join(words)

print(smash(['hello', 'world', 'this', 'is', 'great'])) # 'hello world this is great'
print(smash([])) # ''
print(smash(["hello"])) # "hello"
print(smash(["hello", "world"])) # "hello world"
print(smash(["hello", "amazing", "world"])) # "hello amazing world"
print(smash(["this", "is", "a", "really", "long", "sentence"])) # "this is a really long sentence"

# most clever
smash = ' '.join
# Strings have a join method defined on them already, and the one on the string ' ' already does what we want.
# All that the tests are checking for is a function that solves the problem with the name "smash". So we can take that existing method ' '.join and just give it the new name smash.

# Compared to your solution, here ' '.join function is just aliased.
# When wrapping ' '.join in another function, your have a call instruction to execute for calling your function before ' '.join is actually called.
# This overhead is in practice very small, but it becomes significant when you run a benchmark looping on this code thousands of times.

# while loop accommodating for length 0
def smash(words):
    
    i=0
    l=len(words)
    str1=""
    while i<l:
        if i<l-1:
            str1+=words[i] + " "
        else: 
            str1+=words[i]
        i+=1
        
    return str1

#  .strip() eliminates empty spaces in the beginning and end of a string
def smash(words):
    return ' '.join(words).strip()

# for loop iterating through and concatenating each word with a space
def smash(words):
    # Begin here
    result = ""
    for i in range(len(words)):
        if i != len(words)-1:
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return result 

# if else conditionals in one line
# result of if condition- condition of if - if - condition of else - else - result of else condition 
def smash(words):
    return " ".join(words) if len(words) >= 1 else ""

# importing re or regex to use .sub() which returns a string where all matching occurrences of the specified pattern are replaced by the replace string
import re
def smash(words):
    return re.sub("[]'',[]", "", str(words))