# Find the missing letter
"""
    Find the missing letter
    Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

    You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
    The array will always contain letters in only one case.

    Example:

    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'
    (Use the English alphabet with 26 letters!)
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of string letters
    can they be empty or null?
    will they be case sensitive?    
    will they either always be upper case or lowercase not both?
"""
# Return:
"""
    a string character missing in the ascending sequence of the alphabet
"""
# Examples:
"""
    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'
"""
# Pseudocode:
"""
    # create a copy of the input array using ord() on each element converting over to the number representing the unicode code of a specific character
    # iterate through the array but less than 1 of the length because I want to compare the the 2nd to the last value to the last value
    # NOTE because I'm comparing the current value to the next value and the final value doesn't have a next value, I will get an error. This is why my stop point for the loop is 1 less than the length of the array.
    # if the current element is anything other than 1 less of the next, return that character chr() value + 1
"""

# my answer
def find_missing_letter(chars):
    # create a copy of the input array using ord() on each element converting over to the number representing the unicode code of a specific character
    x = [ord(e) for e in chars]
    # iterate through the array but less than 1 of the length because I want to compare the the 2nd to the last value to the last value
    # NOTE because I'm comparing the current value to the next value and the final value doesn't have a next value, I will get an error. This is why my stop point for the loop is 1 less than the length of the array.
    for i in range(len(x)-1):
        # if the current element is anything other than 1 less of the next, return that character chr() value + 1
        if x[i] +1 != x[i+1]:
            return chr(x[i] +1)
        
# my answer refactored for codewars
def find_missing_letter(chars):
    x = [ord(e) for e in chars]
    return [chr(x[i] +1) for i in range(len(x)-1) if x[i] +1 != x[i+1]][0]

print(find_missing_letter(['a','b','c','d','f'])) # 'e'
print(find_missing_letter(['O','Q','R','S'])) # 'P'

# best practices and most clever
# I changed the variable names to be easier to understand
def find_missing_letter(arr):
    index = 0
    # while the unicode value of the current index is equal to the unicode value of the next index -1
        # add 1 to the index value and repeat the loop
        # so when the current value is not equal to the next value -1 then exit the while loop and return the current element unicode +1 converted to its string character value
    while ord(arr[index]) == ord(arr[index+1]) - 1:
        index += 1
    return chr(1+ord(arr[index]))

# here they are creating a list of all string characters in the alphabet of lower and caps as a list
# Then they declare a start point of the input grabbing the first character of the input and referencing that characters index value in the alphabet list ast a start point. Then check if each next input is the next index in alphabet. If it is not then return the correct next character from the alphabet list.
def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
        
# here they used next() inside a for loop range of -1 to compare the current unicode value to the next
# next(iterable, default)
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))

# only for codewars
# here they are one lining an array and calling the first index to have a one liner
# here they are creating a set of the proper start point + 1 to each value and then comparing it to the input and returning the value that is in the proper step by 1 value not in the input
def find_missing_letter(chars):
    return set(chr(i) for i in range(ord(chars[0]), ord(chars[-1]) + 1)).difference(set(chars)).pop()