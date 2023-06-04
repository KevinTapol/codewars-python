# Find the missing term in an Arithmetic Progression
"""
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers
    will the first element always be 1?
    can the array be empty?
"""
# Return:
"""
    the integer in the array that doesn't have the same step in difference with neighboring elements
"""
# Examples:
"""
    [1, 2, 3, 4, 6, 7, 8, 9] => 5
    [1, 3, 4, 5, 6, 7, 8, 9] => 2
"""
# Pseudocode:
"""
    # add the first element to the last element and multiply the result of (the length of the input array + 1) divided by 2
    # subtract the result by the sum of the input array
    # return the difference as an integer
"""

# my answer
def find_missing(input):
    # add the first element to the last element and multiply the result of (the length of the input array + 1) divided by 2
    x = (input[0] + input[-1]) * ((len(input) + 1)/2)
    # subtract the result by the sum of the input array
    x = x - sum(input)
    # return the difference as an integer
    return int(x)

# my answer refactored
def find_missing(input):
    return int((input[0] + input[-1]) * ((len(input) + 1)/2)-sum(input))

# my answer refactored for Codewars implicit return lambda
find_missing = lambda i: int((i[0] + i[-1]) * ((len(i) + 1)/2)-sum(i))

print(find_missing([1, 2, 3, 4, 6, 7, 8, 9])) # 5
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9])) # 2
print(find_missing([1, 3, 5, 9, 11])) # 7

# best practices and most clever
# cleaner version of my answer but not mutating the original input and leaving the answer as a float instead of converting to an integer
def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)


# taking the last value minus the first value then dividing by the length of the input array to establish the proper interval for each element
# enumerate through the input starting at index 1 instead of 0 with each index and element
# if the current element - the previous element is not equal to the interval then return the current element minus the interval for the proper element missing in the sequence
def find_missing(sequence):
    interval = (sequence[-1] - sequence[0])/len(sequence)
    for previous, item in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval
        
# same idea as above but adding the difference to the previous value instead of subtracting by the current
def find_missing(sequence):
    totalGap=sequence[len(sequence)-1]-sequence[0]
    eachGap = totalGap/len(sequence)
    for i in range(len(sequence)-1):
        if sequence[i]+eachGap != sequence[i+1]:
            return sequence[i]+eachGap
        
# take the first 3 elements of the input array
# take the minimum difference absolute value of the current element and the previous
# iterate through the elements in the input array
# if the current element does not equal the first element in the copy then return a else add the min difference until they are not equal and return a
def find_missing(nums):
    a, b, c = nums[:3]
    diff = min(b - a, c - b, key=abs)
    for d in nums:
        if d != a:
            return a
        a += diff

# using an implicit return lambda as a key for sorted()
def find_missing(sequence):
    """Identify the missing element in an arithmetic expression
    following a constant rule
    """
    # A linear list of differences between each element in sequence.
    dif = [sequence[x + 1] - sequence[x] for x in range(len(sequence) - 1)]

    # An array of individual elements and their frequency in dif; [[element, frequency],]
    dif_freq = [[x, dif.count(x)] for x in set(dif)]

    # Sorting by ascending frequency
    sorted_dif_freq = sorted(dif_freq, key=lambda x: x[1])

    outlier = sorted_dif_freq[0][0]
    constant = sorted_dif_freq[-1][0]

    return sequence[dif.index(outlier)] + constant