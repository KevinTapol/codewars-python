"""
Parameters or Edge Cases:
        input will be an array of integers that can be negative
        input array will not be empty
        input array will be mutable
Return:
        the smallest integer
Examples:
        find_smallest_int([78, 56, 232, 12, 11, 43]) # 11
        find_smallest_int([78, 56, -2, 12, 8, -33]) # -33
        find_smallest_int([0, 1-2**64, 2**64]) # 1-2**64
Psuedo Code:
        use the min() method to return the smallest integer value in the array
        I could also sort the array and return the first index value

"""
# my answer using min() best practices
def find_smallest_int(arr):
    # use the min() method to return the smallest integer value in the array
    return min(arr)

print(find_smallest_int([78, 56, 232, 12, 11, 43])) # 11
print(find_smallest_int([78, 56, -2, 12, 8, -33])) # -33
print(find_smallest_int([0, 1-2**64, 2**64])) # 1-2**64

# refactored to lambda using min()
find_smallest_int = lambda arr: min(arr)

# my answer using sort()
def find_smallest_int(arr):
    # sort the array and return the first index value
    arr.sort()
    return arr[0]

# most clever
findSmallestInt=min 

# using sorted() instead of sort()
findSmallestInt = lambda a: sorted(a)[0]

"""
# using reduce NOT SUPPORTED BY PYLANCE!
def findSmallestInt(arr):
    #Code here
    return reduce(lambda x,y: x if x<y else y, arr) 

# using reduce() with lambda
findSmallestInt=lambda arr: reduce(lambda a,b: b if b<a else a,arr,+999999)
"""

# this is how I brute force for loop in JavaScript declaring first value as comparison
def findSmallestInt(arr):
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min

# brute force for loop but comparing the last value instead of the first value
def find_smallest_int(arr):
    element = arr.pop()
    for e in arr:
        if e < element:
            element = e
    return element

# using a for loop and comparing each value but instead of declaring the first index as the comparison, they are setting it to an empty list
def findSmallestInt(arr):
    smallest = []
    for i in range(0,len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest

# checking if each element is an integer
def findSmallestInt(arr):
    """
    input: arr, a list of integers
    output: smallest integer in arr
    """
    
    # check that each element is an int
    for num in arr:
        assert type(num) == int
    
    # sort array
    arr.sort()
    
    # return smallest value
    return arr[0]

    # using a while loopdef find_smallest_int(arr):
    i = 0
    min = arr[0]
    while i<len(arr):
        if arr[i]<min:
            min = arr[i]
        i+=1
    return min
    