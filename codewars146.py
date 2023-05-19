# Two Sum
"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers and an integer
    tests may have multiple answers; any valid solutions will be accepted
    inputs will always valid meaning an array length of 2 or greater and the target integer will always be a sum of 2 of the elements from the array
"""
# Return:
"""
    the indexes where the sum of 2 elements in the array is equal to the integer
"""
# Examples:
"""
    [1,2,3], 4 => [0,2]
    [1234,5678,9012], 14690 => [1,2]
    [2,2,3], 4 => [0,1]
"""
# Pseudocode:
"""
    # declare an empty array named result
    # iterate through the array starting at the next index and check if the element is equal to the result
    # if there exists an element equal to that difference, push both element indexes to result
    # return result
"""
# my answer nested for loop with a boolean break
def two_sum(numbers, target):
    # declare an empty array named result
    result = []
    # declare a boolean true for length of result equal to 2 and set it equal to false
    result_length_two = False
    
    # iterate through the array comparing the difference of the target integer with the current index value
    # and check if that difference exists as an element in the remaining elements
    for i, e in enumerate(numbers):
        # if the length of result is 2 then break the for loop
        if result_length_two:
            break
        
        # if the element is equal to that difference, push both element indexes to result and set result_length_two to true to break the loop
        for j, v in enumerate(numbers):
            if target - e == v and i != j:
                result.append(i)
                result.append(j)
                result_length_two = True  
                break
    
    # return result
    return result

print(two_sum([1,2,3], 4)) # [0,2]
print(two_sum([1234,5678,9012], 14690)) # [1,2]
print(two_sum([2,2,3], 4)) # [0,1]

# best practices
# I strongly disagree a nested for loop is best practices and most clever
# It is very similar to mine but returning the first occurrence of found elements
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
            
# most clever
# To summarize, the solution uses a dictionary d to store previously encountered numbers along with their indices. By iterating through the list and calculating the difference between the target and each number, the solution checks if the difference exists in the dictionary. If it does, a pair of indices is returned representing the two numbers that add up to the target. If no pair is found, the function returns None.
def two_sum(nums, target):
    # here they are declaring an empty set or dictionary to append the results
    d = {}
    # iterate through the input array
    for i, num in enumerate(nums):
        # declare a variable diff for the difference of the target integer and the current element
        diff = target - num
        # if diff exists in d then return the index of diff and the current index of the value that achieved diff
        if diff in d:
            return [d[diff], i]
        # if diff is not found in d store the current num as a key and its index as the value
        # if there is no pairs found the function will implicitly return None
        d[num] = i

# similar to most clever but using range() and referencing only by index
def two_sum(numbers, target):
    compliments = {}
    for i in range(len(numbers)):
        if numbers[i] in compliments:
            return [i, compliments[numbers[i]]]
        compliments[target-numbers[i]] = i

# vary clever!!!
# close to Gauss's theorem of comparing each element to itself in the array
def two_sum(n, target):
    # iterate through the array stopping just before the last element
    for i in range(len(n)-1):
        # if the difference of target and the current element exists in a copy of the remaining elements
        if (target-n[i]) in n[i+1:]:
            # return the indexes of the elements of diff and current index
            return [i, n[i+1:].index(target-n[i])+(i+1)]
    # if no cases exist return none
    return None

# similar to above but updated for python 3.8
# I prefer the previous solution for readability
def two_sum(numbers, target):
    for i in range(len(numbers)):
        if (num := target - numbers[i]) in numbers[i + 1:]:
            return [i, numbers[i + 1:].index(num) + i + 1]
        
# importing a library for combinations
from itertools import combinations as comb

def two_sum(numbers, target):
    for (ia, a),(ib, b) in comb(enumerate(numbers), 2):
        if a+b == target:
            return [ia, ib]