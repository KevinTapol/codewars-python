# Reversed Words
# Parameters or Edge Cases:
    # input will a string of words. 
# Return:
    # the the string reversed but not the individual words reverse
# Examples:
    # reverse_words("hello world!") # "world! hello"
# Psuedo Code:
    # take the input string and split(" ")  each word by white spaced into each element in an array
    # reverse the array using [::-1]
    # convert it back into a string "".join()
    # return the new string

# my answer best practices and most clever
def reverse_words(s):
    return " ".join(s.split(" ")[::-1])

# my answer refactored lambda implicit one liner
reverse_words = lambda s: " ".join(s.split(" ")[::-1])

print(reverse_words("hello world!")) # "world! hello"

# # using reversed() instead of [::-1] to reverse the array/list
def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))

# going line by line
def reverseWords(str): # this function name is deprecated change to reverse_words
    k = str.split(' ') #string to array
    k.reverse() # reverse array
    str = ' '.join(k) # convert back into a string
    return str # return new string

# for loop
def reverseWords(str): # this function name is deprecated change to reverse_words
    new_arr = []
    for word in str.split(): # this line is deprecated change to .split(" ")
        new_arr.append(word)
    new_arr.reverse()   
    return ' '.join(new_arr)

# for loop using [] to convert to array with a for loop one liner
def reverseWords(str): # this function name is deprecated change to reverse_words
    return ' '.join([i for i in str.split(" ")[::-1]])

# using regex to split()
import re
def reverseWords(str):
    return "".join(re.split(r'(\s+)', str)[::-1])