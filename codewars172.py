# Remove the minimum
"""
The museum of incredible dull things
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
    create a string copy result of the input array with string elements
    use the replace method passing in the min of the input array as a string with an empty string and a count of 1
    convert result back into a list of integers and return it
"""
# Return:
"""
    a copy of the input array of integers with the min value removed only once
"""
# Examples:
"""
    [1,2,3,4,5] => [2,3,4,5]
    [5,3,2,1,4] => [5,3,2,4]
    [2,2,1,2,1] => [2,2,2,1]
"""
# Pseudocode:
"""
    # create a list copy of the input array of integers
    # if the copy is not empty or null use the .remove() method that removes the argument only once from the array
    # return result
"""

# my answer, best practices and most clever
def remove_smallest(numbers):
    # create a list copy of the input array of integers
    result = numbers[:]
    # if the copy is not empty or null use the .remove() method that removes the argument only once from the array
    if result:
        result.remove(min(result))
    # return result
    return result

print(remove_smallest([1,2,3,4,5])) # [2,3,4,5]
print(remove_smallest([5,3,2,1,4])) # [5,3,2,4]
print(remove_smallest([2,2,1,2,1])) # [2,2,2,1]

# instead of using if list for empty or null cases, here they use len(list) < 1
# also they are creating list copy up to the first instance of the min integer and concatenating to another copy after it to the end
def remove_smallest(numbers):
    if len(numbers) < 1: 
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx+1:]

# one liner of the same as above with concatenation of lists and not null for returns
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []

# using enumerate for index and element
def remove_smallest(numbers):
    return [n for i, n in enumerate(numbers) if i != numbers.index(min(numbers))]