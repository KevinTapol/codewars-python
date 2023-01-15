"""
Reversed sequence
Parameters or Edge Cases:
    inputs will be positive integers greater than 0
Return:
    an array in descending order decrementing by 1 starting at the given input integer and stopping at 1
Examples:
    (reverse_seq(5),[5,4,3,2,1])
Psuedo Code:
    create an empty list
    append n to the list and decrement by 1 appending each time until n = 0 exclusively
    return the list
    or create a new list() specifying the range() start at n end at 0 exclusively and decrement by -1
"""
# my answer using a while loop I need to practice while loops for pygame!!!!!
def reverse_seq(n):
    # create an empty list
    x = []
    # append n to the list and decrement by 1 appending each time until n = 0 exclusively
    while n != 0:
        x.append(n)
        n -= 1
    # return the list
    return x


# my answer best practices and most clever
def reverse_seq(n):
    # create a new list() specifying the range() start at n end at 0 exclusively and decrement by -1
    print(n)
    return list(range(n, 0, -1))

# my answer further refactored to lambda one liner implicit return
reverse_seq = lambda n: list(range(n, 0, -1))

print(reverse_seq(5)) # [5,4,3,2,1]

# 2nd best practices and most clever but doesn't work in python 3 which is what Codewars uses!!!
# To make it work, wrap range(n, 0, -1) with list() => return list(range(n, 0, -1))
# Also I noticed that the function name is different too using reverseseq instead of reverse_seq as did #1 best practices and most clever!!!
def reverseseq(n):
    return range(n, 0, -1)

# message to user to pick a number greater than 0
def reverse_seq(a):
    if a > 0:
        return(list(range(a, 0, -1)))
    else:
        return("pick a positive number")

# for loop
def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output

# Here they are creating a list with a for loop specifying the range start at 1 inclusively and end at n+1 exclusively
# Then reverse the list with [::-1]
# Works with python3. You don't need to wrap range() with list() because they are using a for loop.
def reverse_seq(n):
    return [x for x in range(1,n+1)][::-1]

# same as above but descending resulting in not needing to reverse the list
def reverse_seq(n):
    return [i for i in range(n, 0, -1)]

# using reversed() to reverse the range
def reverse_seq(n): 
    return list(reversed(range(1,n+1)))

# [*] is replacing list()
# * is used to iterate through the range and [] is converting it to a list 
def reverse_seq(n):
    return [*range(n,0,-1)]

# subtracting the input integer by the index and setting the index value equal to the result
def reverse_seq(n):
    return [n-x for x in range(n)]

# using .reverse() to reverse the list
def reverse_seq(n):
    l = [x for x in range(1,n+1)]
    l.reverse()
    return l

# interesting adding the while loop decrementing as the first statement
def reverse_seq(n):
    digits = []
    digits.append(n)
    while n:   
        n -= 1
        if n == 0:
            return(digits)
        else:
            digits.append(n)

# wow very clever imo
# creating a list range(n) includes 0 stops at n and increments by 1
# Then use pop(0) to remove the first index value which is 0 in this case and reverse the list with .reverse().
def reverse_seq(n):
    n+=1
    mass = [ x for x in range(n) ]
    mass.pop(0)
    mass.reverse()
    return mass