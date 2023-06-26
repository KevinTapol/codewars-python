# Sort Numbers
"""
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of positive integers
    inputs can be empty or null
"""
# Return:
"""
    the input array of integers sorted in ascending order
"""
# Examples:
"""
    [1,2,3,10,5] => [1,2,3,5,10]
    None => []
    [] => []
    [20,2,10] => [2,10,20]
    [2,20,10] => [2,10,20]
"""
# Pseudocode:
"""
    # if the input array is empty or null return an empty array as []
    # return the input array sorted
"""

# my answer
def solution(nums):
    # if the input array is empty or null return an empty array as []
    if not nums:
        return []
    # return the input array sorted
    return sorted(nums)

# my answer refactored
def solution(nums):
    return [] if not nums else sorted(nums)

# lambda refactored Codewars Only
solution = lambda nums: [] if not nums else sorted(nums)

print(solution(None)) # []
print(solution([])) # []
print(solution([1,2,3,10,5])) # [1,2,3,5,10]
print(solution([20,2,10])) # [2,10,20]
print(solution([2,20,10])) # [2,10,20]

# best practices 
# similar to my answer but using if nums instead of if not nums
def solution(nums):
    return sorted(nums) if nums else []

# returns nums if nums is not null or empty else []
def solution(nums):
    return sorted(nums or [])

# try catch block
def solution(nums):
    try:
        return sorted(nums)
    except TypeError:
        return []
    
# brute force for loop
def solution(nums):
    if nums == None:
        return []
    else:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j],nums[j + 1] = nums[j + 1],nums[j]
        return nums
    
# using .sort() instead of sorted()
def solution(nums):
    if nums != None and nums != []:
        nums.sort()
        return nums
    else:
        return []