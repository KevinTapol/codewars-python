# Sum Mixed Array
# Parameters or Edge Cases:
    # inputs will be an array of strings and numbers
    # will the array be emtpy?
    # will they always be either strings or numbers?

# Return:
    # the sum of the array values as if all elements were numbers

# Examples:
    # [9, 3, '7', '3'] => 22
    # ['5', '0', 9, 3, 2, 1, '9', 6, 7] => 42
    # ['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'] => 41
    # ['1', '5', '8', 8, 9, 9, 2, '3'] => 45
    # [8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7] => 61
# Pseudo Code:

# my answer for element in the array
def sum_mix(arr):
    total = 0
    for e in arr:
        total += int(e)
    return total

# my answer refactored implicit one liner using sum with a for each element in the array
sum_mix = lambda arr:sum(int(e) for e in arr)

print(sum_mix([9, 3, '7', '3'])) # 22
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])) # 42
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])) # 41
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3'])) # 45
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7])) # 61

# best practices and most clever
# here they are using map() similar to JS .map() but when making a shallow array copy they are specifying that each input be an integer
# then sum the new integer array
def sum_mix(arr):
    return sum(map(int, arr))

# manipulating each element using int() with array brackets for element in array instead of using map()
def sum_mix(arr):
    return sum([int(i) for i in arr])

# try except block
# clever here they are using the case when the element is a string and returns a TypeError convert it to an int() then add it to result
def sum_mix(arr):
    result = 0
    for a in arr:
        try:
            result += a
        except TypeError:
            result += int(a)
    return result

# creating a new array and appending to the array each element as an integer then summing the array
def sum_mix(arr):
  L = []
  for i in arr:
    L.append(int(i))
  return sum(L)

# using float() instead of int()
def sum_mix(arr):
    return sum(float(x) for x in arr)

# using reduce() with a lambda inside
from functools import reduce
def sum_mix(arr):
    #your code here
    return reduce((lambda x,y: int(x)+int(y)),arr)

# using eval
def sum_mix(arr):
    return eval('+'.join(str(x) for x in arr))