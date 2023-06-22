# Remove the minimum
"""
The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers
    input array can be empty or null
"""
# Return:
"""
    the array with the first min value removed or if the array is empty/null return an empty array
"""
# Examples:
"""
    [1, 2, 3, 4, 5] => [2, 3, 4, 5]
    [5, 3, 2, 1, 4] => [5, 3, 2, 4]
    [1, 2, 3, 1, 1] => [2, 3, 1, 1]
    [] => [],
"""
# Pseudocode:
"""
    # declare a copy of the input array named result
    # if result is empty or null return an empty array
    # grab the first index item of result and name it min_val
    # iterate through result and if the current element is less than min_val set min_val equal to that element
    # remove the first occurrence of the element min_val in result
    # return result
"""

# my answer
def remove_smallest(numbers):
    # declare a copy of the input array named result
    result = numbers[:]
    # if result is empty or null return an empty array
    if not result:
        return result
    # grab the first index item of result and name it min_val
    min_val = result[0]
    # iterate through result and if the current element is less than min_val set min_val equal to that element
    for e in result:
        if e < min_val:
            min_val = e
    # remove the first occurrence of the element min_val in result
    result.remove(min_val)
    # return result
    return result

# my answer refactored
def remove_smallest(numbers):
    if not numbers:
        return []
    result = numbers[:]
    min_val = result[0]
    for e in result:
        if e < min_val:
            min_val = e
    result.remove(min_val)
    return result    

print(remove_smallest([])) # []
print(remove_smallest([1, 2, 3, 4, 5])) # [2, 3, 4, 5]
print(remove_smallest([5, 3, 2, 1, 4])) # [5, 3, 2, 4]
print(remove_smallest([1, 2, 3, 1, 1])) # [2, 3, 1, 1]
print(remove_smallest([20, 103, 92, 80, 0, 289, 303, 130])) # [20, 103, 92, 80, 289, 303, 130]


# best practices and most clever
# same idea as my solution but taking the opposite approach in that if a is not null or empty then remove the first occurrence of the min value of the list copy of the input and return it
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

# using length checks of the array for empty or null
# here they found the index of the min value and copied the input array from start to the first index with min value exclusively and concatenated to the copy of the index after the first min value occurrence to the end 
def remove_smallest(numbers):
    if len(numbers) < 1: 
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx+1:]

# one liner similar to the solution above of array copies
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []

# using enumerate() to reference index and element
def remove_smallest(numbers):
    return [n for i, n in enumerate(numbers) if i != numbers.index(min(numbers))]