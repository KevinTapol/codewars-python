# Array plus array
# Parameters or Edge Cases:
    # inputs will be 2 arrays of integers
    # sum the integers of both arrays 
    # each array will have integers that can be negative or positive
# Return:
    # the sum of both arrays of integers
# Examples:
    #  ([1, 2, 3], [4, 5, 6]) => 21
    #  ([-1, -2, -3], [-4, -5, -6]) => -21
    #  ([0, 0, 0], [4, 5, 6]) => 15
    #  ([100, 200, 300], [400, 500, 600]) => 2100
# Pseudo Code:
    # add up all the elements in array 1 and array 2
    # return the sum of both arrays

# my answer and 2nd best practices
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

# my answer refactored implicit return *args
array_plus_array = lambda *a: sum(a[0] + a[1])

print(array_plus_array([1, 2, 3], [4, 5, 6])) # 21
print(array_plus_array([-1, -2, -3], [-4, -5, -6])) # -21
print(array_plus_array([0, 0, 0], [4, 5, 6])) # 15
print(array_plus_array([100, 200, 300], [400, 500, 600])) # 2100

# best practices and most clever
def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

# Very Clever!
# using * to create a tuple/array of the input lists/arrays to be passed in. 2-D array or matrix similar to JS
# then creating a shallow copy of an array summing each individual list creating a 1-D array of single integers
# then using sum() again on the 2 integers of the sums of each list
def array_plus_array(*args):
    return sum(map(sum, args))

# chain() as an iterator
from itertools import chain
def array_plus_array(arr1,arr2):
    return sum(chain(arr1, arr2))

# using for element in array for each input list and adding to declared variable
def array_plus_array(arr1,arr2):
    counter = 0
    for i in arr1:
        counter += i
    for i in arr2:
        counter += i
    return counter

# shortest answer using lambda
array_plus_array=lambda a,b: sum(a+b)

# for each list in the list[arr1, arr2] for each element in each list
# similar to the concept of nested for loops
def array_plus_array(arr1,arr2):
    return sum(i for a in [arr1, arr2] for i in a)

# using *args as spread for creating a list of the inputs then sum for each element in the list 
def array_plus_array(*args):
    return sum([sum(arg) for arg in args])

# using zip() similar to chain() iterator
# if the arrays were of unequal length zip would truncate the longer list.
def array_plus_array(arr1,arr2):
    result=0
    for ar1,ar2 in zip(arr1,arr2):
        result = result + (ar1+ar2)
    return result

# for element in maths
# I didn't know you could do this.
def array_plus_array(x,y):
    sum= 0
    for i in x + y:
        sum += i 
    return sum

# using chain to iterate 
from itertools import chain

def array_plus_array(*arrays):
    return sum(chain.from_iterable(arrays))

# reduce() I'm surprised that the comma after a, isn't creating errors
# unnamed lambda with inputs and what to do with the inputs, and an array
# arr0 = arr1 + arr2 creates a single array of all the elements in both input arrays
from functools import reduce

def array_plus_array(arr1,arr2):
    arr0 = arr1 + arr2
    return reduce(lambda a, b: a + b, arr0)

# using .extend() to append the arrays
def array_plus_array(arr1,arr2):
    arr1.extend(arr2)
    sum = 0
    for i in arr1:
        sum = sum+i
    return sum  

# declaring an empty array and appending both arrays to the new array to sum a single array
def array_plus_array(arr1,arr2):
    arr=[]
    for number in arr1:
        arr.append(number)
    for number2 in arr2:
        arr.append(number2)
        
    return sum(arr)

# while loop appending both input arrays then using a while condition for the length of the new array
# updating the while condition with i += 1
def array_plus_array(arr1, arr2):
    final_array = arr1 + arr2
    i = 0
    sum = 0
    
    while i < len(final_array):
        sum += final_array[i]
        i += 1
        
    return sum

# using *args in the math instead of the inputs
array_plus_array = lambda x, y: sum([*x, *y])