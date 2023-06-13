# The highest profit wins!
"""
Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

Examples (Input --> Output)
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
Remarks
All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.
"""
# Parameters or Edge Cases:
"""
input will be an array of positive integers
"""
# Return:
"""
 an array with the first element being the lowest value in the input array and the second element being the highest number in the array
"""
# Examples:
"""
    [1,2,3,4,5] => [1, 5]
    [2334454,5] => [5, 2334454]
"""
# Pseudocode:
"""
    return an array with index 0 as min value of the input array and index 1 as the max value of the input array
"""

# my answer and best practices
def min_max(arr):
    return [min(arr), max(arr)]

# my answer refactored lambda for Codewars only
min_max = lambda x: [min(x), max(x)]

print(min_max([1,2,3,4,5])) # [1, 5]
print(min_max([2334454,5])) # [5, 2334454]

# most clever
# using .sort() and return first and last values of the input array
def min_max(lst):
  lst.sort()
  tempor = [lst[0],lst[-1]]
  return tempor

# brute force for loop
def min_max(lst):
  # Too easy, but requires two pases
  # return[min(lst), max(lst)]
  
  # Single pass:
  l, u = None, None
  for n in lst:
      if l is None or n < l:
          l = n
      if u is None or n > u:
          u = n
  return [l, u]

# using sorted()
def min_max(lst):
    return [sorted(lst)[0],sorted(lst)[-1]]

# while loop
def min_max(lst):
  minVal = lst[0]
  maxVal = lst[0]
  count = 1
  while count < len(lst):
      if lst[count] < minVal: minVal = lst[count]
      if lst[count] > maxVal: maxVal = lst[count]
      count += 1
  return [minVal, maxVal]