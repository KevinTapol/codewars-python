# Stop gninnipS My sdroW!
# Parameters or Edge Cases:
    # inputs will be a singe string of one or more words
    # strings will consist of only letters and spaces between the words
# Return:
    # return the string but with all 5 or more letter words in reverse
# Examples:
    # "Hey fellow warriors"  => returns "Hey wollef sroirraw" 
    # "This is a test" => returns "This is a test" 
    # "This is another test" => returns "This is rehtona test"
# Pseudocode:
    # convert the input string into an array of strings
    # iterate through the array and if the length of each individual string is 5 or more then reverse the string
    # convert the array of strings back into a single string
    # return the new string

# my answer
def spin_words(sentence):
    x = sentence.split()
    for i in range(len(x)):
        if len(x[i]) >= 5:
            x[i] = x[i][::-1]
    return " ".join(x)

# my answer refactored one line but without implicit return, best practices and most clever
def spin_words(s):
    return " ".join(x[::-1] if len(x) >= 5 else x for x in s.split(" "))

# my answer refactored implicit return 
spin_words = lambda s: " ".join(x[::-1] if len(x) >= 5 else x for x in s.split(" "))

print(spin_words("Hey fellow warriors")) # "Hey wollef sroirraw"
print(spin_words("This is a test")) # "This is a test"
print(spin_words("This is another test")) # "This is rehtona test"

# declaring an array an array of the input split on white space
# reassign the array elements in reverse if the length of the element is 5 or more
# convert the array into a string adding back the white space in between each word
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

# declare an empty array and append to it
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

# using <5 instead of >= 5
def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())

# using regex
import re

def spin_words(sentence):
    # Your code goes here
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)

# using map()
def spin_words(sentence):
    return ' '.join(list(map(lambda x: x if len(x) <5 else x[::-1], sentence.split(' '))))