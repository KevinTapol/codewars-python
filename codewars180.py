# Find the stray number
"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers
    can the array be empty or null?
"""
# Return:
"""
    the integer in the array with a count of 1
"""
# Example:
"""
    [1, 1, 1, 1, 1, 1, 2] => 2
    [2, 3, 2, 2, 2] => 3
    [3, 2, 2, 2, 2] => 3
"""
# Pseudocode:
"""
    # iterate through the input array 
    # if the current element count in the array is equal to 1 return the element
"""

# my answer and best practices
def stray(arr):
    # iterate through the input array and return the element whose count() equals 1
    for e in arr:
        # if the current element count in the array is equal to 1 return the element
        if arr.count(e) == 1:
            return e
        
# my answer refactored for Codewars
def stray(arr):
    return [e for e in arr if arr.count(e) == 1][0]

# lambda of my refactored answer
stray = lambda a: [e for e in a if a.count(e) == 1][0]
        
print(stray([1, 1, 1, 1, 1, 1, 2])) # 2
print(stray([2, 3, 2, 2, 2])) # 3
print(stray([3, 2, 2, 2, 2])) # 3

# most clever 
# using 2nd argument of min() where the key equals count
def stray(arr):
    return min(arr, key=arr.count)


# sorting the input array and comparing the first and last elements to another element in the array checking for duplicates
def stray(arr):
    arr.sort()
    return arr[-1] if arr[0] == arr[1] else arr[0]

# iterating through the array using the next method for comparison
def stray(arr):
    return next(x for x in set(arr) if arr.count(x) == 1)