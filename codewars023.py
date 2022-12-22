"""
Convert number to reversed array of digits
Parameters or Edge Cases:
    inputs will be a multiple digit non-negative number
Return:
    the input in reversed order with each digit in an index in an array
Examples:
    (digitize(35231),[1,3,2,5,3])
    (digitize(0),[0])
    (digitize(23582357),[7,5,3,2,8,5,3,2])
    (digitize(984764738),[8,3,7,4,6,7,4,8,9])
    (digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
    (digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])
Psuedo Code:
    convert the input into a string
    declare an empty array
    loop through the string input and push each digit into their own index converting back into an int
    reverse the list
"""

# my answer brute force for loop
def digitize(n):
    # convert the input into a string
    n = str(n)
    # declare an empty array
    arr = []
    # loop through the string input and push each digit into their own index converting back into an int
    for i in range(len(n)):
        arr.append(int(n[i]))
    # reverse the list
    return arr[::-1]

print(digitize(35231)) # [1,3,2,5,3]
print(digitize(0)) # [0]
print(digitize(23582357)) # [7,5,3,2,8,5,3,2]
print(digitize(984764738)) # [8,3,7,4,6,7,4,8,9]
print(digitize(45762893920)) # [0,2,9,3,9,8,2,6,7,5,4]
print(digitize(548702838394)) # [4,9,3,8,3,8,2,0,7,8,4,5]

# my answer refactored
def digitize(n):
    return [int(x) for x in (str(n))][::-1] 

# same as my refactored answer but using reverse inside instead of outside
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

# best practices and most clever ONLY WORKS WITH PYTHON2!!!!
def digitize(n):
    return map(int, str(n)[::-1])
# python3 equivalent of above
def digitize(n): return list(map(int, str(n)[::-1]))

# python3 lambda one liner
digitize=lambda n: list(map(int, list(str(n))[::-1]))

# python3 lambda one liner but without declaring the list() in the 2nd map param for reverse
digitize = lambda n: list(map(int, str(n)[::-1]))

# python2 lambda
digitize = lambda n: map(int, str(n)[::-1])

# interesting using a one line but calling the function on itself
digitize = lambda n, s=[]: digitize(n // 10 , s = s + [n % 10]) if n > 9 else s + [n]

# I couldn't remember the .reverse() JS equivalent in Python was reversed()
def digitize(n):
    return [int(x) for x in reversed(str(n))]

# how .reverse() is used in python
def digitize(n):
    mylist = [int(i) for i in str(n)]
    mylist.reverse()
    return mylist

# while loop
def digitize(n):
    result = []
    while n >= 1:
        result.append(n%10)
        n //= 10
    return result

# using .instert() instead of append()
def digitize(n):
    num_array = [] # make empty array
    for number in str(n): # make n into string to interate through 
        num_array.insert(0, int(number)) # insert number into 1st position (reverses it)
    return num_array # return array