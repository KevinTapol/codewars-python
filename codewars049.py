# Convert a string ot an array

# Parameters or Edge Cases:
    # the input string will be a string of strings with spaces and random capital letters
    # the input string can be empty
    # don't worry about capitalization
# Return:
    # an array of separating each string at an empty space
# Examples:
    # (string_to_array("Robin Singh"), ["Robin", "Singh"])
    # (string_to_array("CodeWars"), ["CodeWars"])
    # (string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
    # (string_to_array("1 2 3"), ["1", "2", "3"])
    # (string_to_array(""), [""])
# Psuedo Code:
    # take in the string and use each empty space " " as a separator for each element in a new array
    # return the new array

# my answer best practice and most clever
def string_to_array(s):
    return s.split(' ')

# my answer refactored to lambda implicit return one liner
string_to_array = lambda s: s.split(' ')

print(string_to_array("Robin Singh")) # ["Robin", "Singh"]
print(string_to_array("CodeWars")) # ["CodeWars"]
print(string_to_array("I love arrays they are my favorite")) # ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(string_to_array("1 2 3")) # ["1", "2", "3"]
print(string_to_array("")) # [""]

# manages white space using or instead of .strip()
# splitting an empty string or a string consisting of just whitespace with a None separator returns []
# example " " will return ["",""] and "  " will return ["", "", ""]
def string_to_array(string):
    return string.split() or ['']

# here if someone someone inputs several white spaces return ['']
def string_to_array(string=''):
    return string.split() if string else ['']

# for loop with array methods 
def string_to_array(s):
    # your code here
    result = []
    t = ''
    e = ' '
    for i in s:
        if i not in e:
            t = t + i
        else:
            result.append(t)
            t = ''
    result.append(t)
    return result

# using regex
# not accommodating for white space
import re
def string_to_array(s):

   # your code here
   return re.split(r'[;,\s]\s*', s) 


# using classes
def find_all(string, sub):
    start = 0
    while True:
        start = string.find(sub, start) # using the method string.find(value of sub, start the search, end the search)
        if start == -1: return # .find() returns -1 then the value is not found
        yield start, start + len(sub) # yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value
        start += len(sub)


class SplitError(Exception): # pass on Exception
    pass

# main class creating objects
class Splitter:
    def __init__(self, string: str): # initialized class making the object s
        self.string = string # variable declaration of string with object self

    def split(self, sep: str = " "):
        if not sep:
            raise SplitError("Empty Separator") # call exception error class SplitError
        s = list(find_all(self.string, sep)) # calling the function find_all()
        if not s:
            return [self.string]
        return self.string.split(sep)


def string_to_array(s): # calling the function/method split in the class Splitter on the object s
    return Splitter(s).split()