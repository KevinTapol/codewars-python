# Delete occurrences of an element if it occurs more than n times
"""
Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of positive integers greater than 0 and an integer representing the count of repeats allowed
    can the array be empty?
"""
# Return:
"""
    return the input array with the accepted amount of repeated values without manipulating the order of the array
"""
# Examples:
"""
    # [1,2,3,1,2,1,2,3], 2 => [1,2,3,1,2,3]
    # [20,37,20,21], 1 => [20,37,21]
    # [1,1,3,3,7,2,2,2,2], 3 => [1, 1, 3, 3, 7, 2, 2, 2]
"""
# Pseudocode:
"""
    # declare an empty array result
    # iterate through the input array
    # if the 2nd param integer is less than the current element count in the result array append it to the result array
    # return the array
"""

# my answer, best practices and most clever
def delete_nth(arr,n):
    # declare an empty array result
    result = []
    # iterate through the input array
    for e in arr:
    # if the 2nd param integer is less than the current element count in the result array append it to the result array
        if result.count(e) < n:
            result.append(e)
    # return the array
    return result


print(delete_nth([1,2,3,1,2,1,2,3], 2)) # [1,2,3,1,2,3]
print(delete_nth([20,37,20,21], 1)) # [20,37,21]
print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) # [1, 1, 3, 3, 7, 2, 2, 2]

# declaring an empty set to turn into a dictionary once key values are added in the for loop 
def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res

# using enumerate to pull index and element if a copy of the order ending at the current index count of the element
def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ] 

# creating a dictionary from imports
from collections import defaultdict

def delete_nth(order,max_e):
    dct = defaultdict(int)
    res = []
    for i in order:
        dct[i] += 1
        if dct[i] <= max_e:
            res.append(i)
    return res

# importing for counter
from collections import Counter

def delete_nth(order, max_e):
    c = Counter()
    result = []
    for element in order:
        if c[element] < max_e:
            c[element] += 1
            result.append(element)
    return result