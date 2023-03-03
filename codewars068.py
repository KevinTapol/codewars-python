# Sum without highest and lowest number
# Parameters or Edge Cases:
    # inputs will be arrays
    # inputs can be empty or null
# Return:
    # the sum all the numbers of a given array except the highest and the lowest value 
# Examples:
    # [ 6, 2, 1, 8, 10 ] => 16
    # [ 1, 1, 11, 2, 3 ] => 6
# Pseudo Code:
    # checking if array is null or empty  
        # not array 
        # len(arr or []) 
        # array == None 
        # None in array
    # sort the array
    # slice from 1 to length of the array -1 
    # return the sum of the shallow copy

# my answer
def sum_array(arr):
    if not arr or len(arr) < 2:
        return 0
    else:
        a = sorted(arr[:])
        del a[-1] #same as saying del a[len(a) -1] or delete last item in the array
        del a[0]
        return sum(a)
    
# my answer refactored implicit lambda 
sum_array = lambda a: 0 if not a or len(a) < 2 else sum(sorted(a)[1:-1])

print(sum_array([ 6, 2, 1, 8, 10 ])) # 16
print(sum_array([])) # 0
print(sum_array([1, 2])) # 0
print(sum_array([ 1, 1, 11, 2, 3 ])) # 6

# best practices
# using max() and min()
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# most clever similar to my refactored
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

# using array == None instead of not array for null arrays
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])

# using sum() on array and [] for null arrays
def sum_array(arr):
    return sum(sorted(arr or [])[1:-1])

# using a for loop and declaring s for string 
# mi and ma are unnecessary 
def sum_array(arr):
  
  if arr is None or len(arr) < 2:
    return 0
  
  mi, ma, s = arr[0], arr[0], 0
  
  for x in arr:
    if x > ma:
      ma = x
    elif x < mi:
      mi = x
    
    s += x
  
  return s - mi - ma

# try except
def sum_array(arr):
    try: return sum(arr) - max(*arr) - min(*arr)
    except: return 0

# using .remove() instead of del array[index]
def sum_array(arr):
    try:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)
    except:
        return 0
    
# try except with TypeError
def sum_array(arr):
    try:
        return sum(sorted(arr)[1:-1])
    except TypeError:
        return 0
    
# using .sort() instead of sorted()
def sum_array(arr):
    #your code here
    if arr is None or len(arr) == 0:
        return 0
    arr.sort()
    return sum(arr[1:-1])

# using [:] in for statement for shallow array copy
def sum_array(arr):
    if not arr or len(arr) < 3: return 0
    sum = min = max = arr[0]
    for x in arr[1:]:
        if x < min:
            min = x
        elif x > max:
            max = x
        sum += x
    return sum - min - max

# using .pop()
def sum_array(arr):
    if not arr or len(arr) <=2: 
        return 0
    else:
       arr.sort()
       print(arr)
       arr.pop(0)
       arr.pop(-1)
       print(arr)
       sum = 0
       for i in arr:
          sum += i
            
       return sum