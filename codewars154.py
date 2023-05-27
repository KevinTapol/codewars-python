# Sums of Parts
"""
Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.

Other Examples:
ls = [1, 2, 3, 4, 5, 6] 
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers
    inputs can be empty 
"""
# Return:
"""
    an array of elements of the sum of the input array of elements removing the first value of the array till it is empty
"""
# Examples:
"""
    [] => [0]
    [0, 1, 3, 6, 10] => [20, 20, 19, 16, 10, 0]
    [1, 2, 3, 4, 5, 6] => [21, 20, 18, 15, 11, 6, 0]
    [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358] => [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
"""
# Pseudocode:
"""
    # declare an integer total equal to the sum of the input array
    # declare an array result with total as the first element
    # iterate through the input array 
    # declare a local variable diff equal to the difference of the total and the current index
    # append diff to result
    # reassign input equal to diff
    # return result
"""

# my answer
def parts_sums(ls):
    # declare an integer total equal to the sum of the input array
    total = sum(ls)
    # declare an array result with the sum of the input array as the first element
    result = [total]
    # iterate through the input array 
    for i in range(len(ls)):
    # declare a local variable diff equal to the difference of the total and the current index
        diff = total - ls[i]
    # append diff to result
        result.append(diff)
    # reassign input equal to diff
        total = diff
    # return result
    return result

# my answer refactored
def parts_sums(ls):
    total = sum(ls)
    result = [total]
    for i in range(len(ls)):
        diff = total - ls[i]
        result.append(diff)
        total = diff
    return result

print(parts_sums([])) # [0]
print(parts_sums([0, 1, 3, 6, 10])) # [20, 20, 19, 16, 10, 0]
print(parts_sums([1, 2, 3, 4, 5, 6])) # [21, 20, 18, 15, 11, 6, 0]
print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358])) # [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]

# best practices and most clever
# for each iteration they are taking the last appended element in the result array and subtracting by the current element in the for loop then appending the difference as the next element in result to be used for the next iteration
def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result

# importing to use accumulate() instead of sum and reversing the array for the difference of the last element instead of the first being pushed to the output array answer
from itertools import accumulate

def parts_sums(ls):
    return [0, *accumulate(reversed(ls))][::-1]


# using the spread operator *
from itertools import accumulate

def parts_sums(ls):
    return [*accumulate(ls[::-1])][::-1]+[0]

# using a while loop
def parts_sums(ls):
    r=[sum(ls)]
    while ls: r.append(r[-1] - ls.pop(0))
    return r