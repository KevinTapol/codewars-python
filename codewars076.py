# Highest and Lowest
# Parameters or Edge Cases:
    # inputs will be a string of numbers separated by a single space
    # numbers will be valid Int32 integers that can be negative or positive 
    # there will be at least 1 number in the input string meaning no empty strings
# Return:
    # the highest and lowest value integer in the input string with the highest first then empty space then lowest as a string
# Examples:
    # igh_and_low("1 2 3 4 5")  # return "5 1"
    # high_and_low("1 2 -3 4 5") # return "5 -3"
    # high_and_low("1 9 3 4 -5") # return "9 -5"
# Pseudo code:
    # convert the string into an array separating the elements on the empty spaces
    # create shallow copy array of the elements as integers and sort them
    # return a string of the last index with a space and the first index
# my answer
def high_and_low(numbers):
    x = list(numbers.split(' '))
    s = sorted(int(e) for e in x)
    return f"{s[-1]} {s[0]}"

# my answer refactored to implicit one liner not dry code though
high_and_low = lambda a: f"{sorted(int(e) for e in list(a.split(' ')))[-1]} {sorted(int(e) for e in list(a.split(' ')))[0]}" 
print(high_and_low("1 2 3 4 5")) # "5 1"
print(high_and_low("1 2 -3 4 5")) # "5 -3"
print(high_and_low("1 9 3 4 -5")) # "9 -5"
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) # "542 -214"

# best practices and most clever
# string interpolation for python using %i
# here they are using math max() and min() for values instead of sorting
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# implicit return lambda one liner very similar to my refactored but using key=int instead of int() and + instead of f""
high_and_low=lambda x:max(x.split(' '),key=int)+' '+min(x.split(' '),key=int)

# using map() first argument for map says to treat inputs as int
def high_and_low(numbers):
    return ' '.join([str(max(map(int, numbers.split()))), str(min(map(int, numbers.split())))])

# key=int tells Python to treat the data as an integer instead of a string w/o it the min() and max() will fail
# I'm not sure why you don't need () for max, min
# read as for function in (max,min):
def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))
# As functions are objects in Python, they can be iterated, so he is iterating a tupple that contains two functions, min and max, and applying the same argument to them, therefore the result is a list with only 2 elements, the min and the max. It can be written the same as below
"""
    numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
    lst = []
    
    for function in (max, min):
       val = function(numbers.split(), key=int)
       lst.append(val)
    
    max_str = str(lst[0])
    min_str = str(lst[1])
    print(max_str + ' ' + min_str)
"""

# string interpolation with f string f"{var}"

# brute force while loop
def high_and_low(numbers):
    numlist = numbers.split(" ")
    i = 0
    highest = int(numlist[0])
    lowest = int(numlist[0])
    while i < len(numlist):
        numlist[i] = int(numlist[i])
        if numlist[i] > highest:
            highest = numlist[i]
        if numlist[i] < lowest:
            lowest = numlist[i]
        i += 1
    highest = str(highest)
    lowest = str(lowest)
    return  highest+" "+lowest

# brute force for loop comparing values in the list
def SSsSsSSSSsssSs(s):
    S = s.split(' ')
    Ss = SS = sssSssS(S[0])
    for SSs in S:
        SSs = sssSssS(SSs)
        if SSs > Ss:
            Ss = SSs
        elif SSs < SS:
            SS = SSs
    SSS = SSssSsSsS(Ss) + ' ' + SSssSsSsS(SS)
    return SSS

# concatenation with +
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))

# .format() string interpolation
def high_and_low(numbers):
    a = list(map(int, numbers.split()))
    return "{} {}".format(max(a), min(a))

# nested lambdas
# inside lambda for answer format return and outer for converting to list of integers for each element in string
high_and_low = lambda n: (lambda x: "{} {}".format(max(x), min(x)))([int(e) for e in n.split()])

# using %s instead of %i for string iterpolation
high_and_low = lambda numbers: "%s %s" % (max(map(int, numbers.split())), min(map(int, numbers.split())))

# using regex
import re
def high_and_low(numbers):
    nums = [int(number) for number in re.findall(r"-{0,1}[0-9]{1,}", numbers)]
    return f'{max(nums)} {min(nums)}'