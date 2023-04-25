# Tribonacci Sequence
"""I put the description in ChatGPT to better understand it. ChatGPT returned the following description. Step by index of 1.
 Do you know what the Fibonacci sequence is? It's a sequence of numbers where each number is the sum of the two previous ones. So it starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

Now, have you heard of the Tribonacci sequence? It's like the Fibonacci sequence, but instead of adding the last two numbers to get the next one, you add the last three numbers! So, if we start with the numbers 1, 1, 1, we get 1, 1, 1, 3, 5, 9, 17, 31, and so on.

But wait! What if we start with 0, 0, 1 instead? Well, we still add the last three numbers, but now we get a different sequence: 0, 0, 1, 1, 2, 4, 7, 13, 24, and so on.

So, here's the challenge: write a program that can generate the first n numbers of the Tribonacci sequence, given a starting set of three numbers. And if n is zero, the program should return an empty list.
"""
# Parameters or Edge Cases:
"""
inputs will be a list of 3 integers representing the Tribonacci sequence start point and an integer representing the length of the list.
input list can be a float

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified
"""
# Return:
"""Return a list with the input list as the start point and list length of the 2nd input
    if the 2nd input is 0 then return an empty list 
"""
# Examples:
""" (tribonacci([1, 1, 1], 10) => [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    (tribonacci([0, 0, 1], 10) => [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    (tribonacci([0, 1, 1], 10) => [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    (tribonacci([1, 0, 0], 10) => [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
    (tribonacci([0, 0, 0], 10) => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    (tribonacci([1, 2, 3], 10) => [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    (tribonacci([3, 2, 1], 10) => [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
    (tribonacci([1, 1, 1], 1) => [1]
    (tribonacci([300, 200, 100], 0) => []
    (tribonacci([0.5, 0.5, 0.5], 30) => [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]
"""
# Pseudocode:
""" copy the input list
    if the 2nd input is 0 then return an empty list
    iterate through to the list length of the 2nd input
        if the length of the input array is greater than the 2nd input
            return a copy of the input list stopping at n ie list[:n]
        else append the sum of the values of the index iterations of i, i+1 and i+2
    return the new list with the length of n

"""

# my answer
def tribonacci(signature, n):
    # copy the input list
    t = signature[:]
    # if the 2nd input is 0 then return an empty list
    if n == 0:
        return []
    # iterate through to the list length of the 2nd input
    for i in range(n):
        # if the length of the input array is greater than the 2nd input
        if len(t) > n:
            # return a copy of the input list stopping at n ie list[:n]
            return t[:n]
        # else append the sum of the values of the index iterations of i, i+1 and i+2
        else:
            t.append(t[i] + t[i+1] + t[i+2])
    # return the new list with the length of n        
    return t

# my answer refactored 
# sum(t[-3:]) is replacing t[i] + t[i+1] + t[i+2] by grabbing the previous 3 index values of the current iteration of list t
def tribonacci(signature, n):
    t = signature[:]
    for i in range(n - len(signature)):
        t.append(sum(t[-3:]))
    return t[:n]


# my answer using a while loop
def tribonacci(signature, n):
    t = signature[:]
    if n == 0:
        return []
    while len(t) < n:
        t.append(sum(t[-3:]))
    return t[:n]

    
print(tribonacci([300, 200, 100], 0)) # [0]
print(tribonacci([1, 1, 1], 1)) # [1]
print(tribonacci([1, 1, 1], 2)) # [1, 1]
print(tribonacci([1, 1, 1], 3)) # [1, 1, 1]
print(tribonacci([1, 1, 1], 4)) # [1, 1, 1, 3]
print(tribonacci([1, 1, 1], 5)) # [1, 1, 1, 3, 5]
print(tribonacci([1, 1, 1], 10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

# best practices and most clever
def tribonacci(signature, n):
    # here they are creating a copy of the list with the first three indexes being filled with the copied list and the remaining indexes as undeclared and not empty; otherwise it would return an array of declared empty strings
    res = signature[:n]
    # looping through to the 2nd input integer -3 because you're taking the sum of the previous 3 indexes  and appending it to the copy
    for i in range(n - 3): 
        res.append(sum(res[-3:]))
    return res

# clean while loop that appends to the input array while the length of the array is less than the 2nd input then returning a copy stopping at the 2nd input. This works because you start at 0 for index and end at 9 meaning < 10 exclusively
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]

# way cleaner version of my unrefactored answer
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]

# recursion on a conditional else with new inputs
def tribonacci(signature,n):
    return signature[:n] if n<=len(signature) else tribonacci(signature + [sum(signature[-3:])],n)

# one line return for index in range start at 3 and stop at n
def tribonacci(signature,n):
    [signature.append(sum(signature[i-3:i])) for i in range(3,n)]
    # signature[:n] works as well since 0 is the default start
    return signature[0:n]

#  using input list += [result] instead of list.append(result)
# this means that you can concatenate an array to an array
def tribonacci(s, n):
    while n > len(s):
        s += [sum(s[-3:])]
    return s[:n]

# concatenating the list with recursion on conditionals
def tribonacci(signature,n):
    return signature[:1] + tribonacci(signature[1:] + [sum(signature)], n - 1) if n > 0 else []