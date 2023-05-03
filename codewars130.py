# Sort the odd
"""
    You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
"""
# Parameters or Edge Cases:
"""
    input arrays can be empty
    integers will be 0 to 9 inclusively
"""
# Return:
"""
    the input array of integers with the odd numbers sorted and the even numbers kept in their original index locations
"""
# Examples:
"""
    [7, 1]  =>  [1, 7]
    [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""
# Pseudocode:
"""
    declare an empty array result
    create a copy of the input array named even_nums and for numbers that are not even replace them with 'x'
    create a copy of the input array named odd_nums of only odd numbers and sort it
    declare an count and set it equal to 0
    iterate through even_nums
        if the element is not 'x' append it to result
        if it is equal to 'x' append the element at the current count index of odd_nums to result and add 1 to count
    return result
"""

# my answer
def sort_array(arr):
    result = []
    # create a copy of the input array named even_nums and for numbers that are not even replace them with 'x'
    even_nums = [e if e % 2 == 0 else 'x' for e in arr]
    # create a copy of the input array named odd_nums of only odd numbers and sort it
    odd_nums = sorted([e for e in arr if e % 2 !=0])
    # declare an count and set it equal to 0
    count = 0
    # iterate through even_nums
    for i in range(len(even_nums)):
        # if the element is not 'x' append it to result
        if even_nums[i] != 'x':
            result.append(even_nums[i])
        # if it is equal to 'x' append the element at the current count index of odd_nums to result and add 1 to count
        else:
            result.append(odd_nums[count])
            count +=1
    return result


# my answer refactored
def sort_array(arr):
    result = []
    even_nums = [e if e % 2 == 0 else 'x' for e in arr]
    odd_nums = sorted([e for e in arr if e % 2 !=0])
    count = 0
    for i in range(len(even_nums)):
        if even_nums[i] != 'x':
            result.append(even_nums[i])
        else:
            result.append(odd_nums[count])
            count +=1
    return result

print(sort_array([7, 1])) # [1, 7]
print(sort_array([5, 8, 6, 3, 4])) # [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# best practices and most clever
# wow incredible 
# create an array of the odd numbers in the input and reverse sorting it meaning in highest to lowest of element value
# Then return an array where your iterating through the input array. If the current element is even append that element. If it is odd then pop the last value from the reverse sorted odd number array and append it.
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

# broken down and simplified version of my answer
def sort_array(source_array):

    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
            
        else:
            answer.append(i)
            
    odds.sort()
    
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer

# iter() function returns an iterator object.
# using iter() on an array of the odds sorted
# using truthy for current element % 2 if it returns 1 then that means true it is an odd then use next(odds) meaning grab the elements in odds in ascending order 
# else  if current element % 2 returns 0 then it is false and the element is even and return the element 
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]

# using index item for enumerate() instead of index element
def sort_array(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result

# clever how they are using map creating a copy and formatting with a copy of sorted odds as strings then converting back into an array
def sort_array(source_array):

    return [] if len(source_array) == 0 else list(map(int,(','.join(['{}' if a%2 else str(a) for a in source_array])).format(*list(sorted(a for a in source_array if a%2 ==1))).split(',')))

# using an implicit return lambda with filter
def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [], 0
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)    
    return l