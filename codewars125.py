# Find the unique number
"""
    There is an array with some numbers. All numbers are equal except for one. Try to find it!
    The tests contain some very huge arrays, so think about performance.
"""
# Parameters or Edge Cases:
"""
    input array will contain at least 3 numbers
"""
# Return:
"""
    the element that occurs only once from the input array
"""
# Examples:
"""
    [ 1, 1, 1, 2, 1, 1 ] => 2
    [ 0, 0, 0.55, 0, 0 ] => 0.55
"""
# Pseudocode:
"""
    since the array can be so large that iterating through it would cause problems, I chose the following solution
    sort the array
    if the 2nd index value is equal to the 1st index value then return the final index at -1 else return the first index

"""

# my answer
def find_uniq(arr):
    n = sorted(arr)
    if n[1] == n[0]:
        return n[-1]
    return n[0]

# my answer refactored 2nd most clever
def find_uniq(a):
    n = sorted(a)
    return n[-1] if n[1] == n[0] else n[0]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ])) # 2
print(find_uniq([ 0, 0, 0.55, 0, 0 ])) # 0.55

# best practices and most clever
# here they created a set of the array with the 2 variable elements in the array
# then they checked for the variable count is 1 in the original input
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

# creating a set but looping through the set to compare the count of the original input array
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
    

# imported Counter()
"""
Counter(arr): O(n).
.most_common(): O(n log n) (because sorting!).
You can make a complete O(n) solution as follows:
return min(Counter(arr).items(), key=itemgetter(1))[0] Or more appropriately for this task: return next(k for k, v in Counter(arr).items() if v == 1)
"""
from collections import Counter

def find_uniq(a):
    return Counter(a).most_common()[-1][0]

# returning an array of a single element and calling it by index location
# They created a set and whichever element of that set has a count equal to 1 from the original input was pushed to an array by itself. Then they called the only element in the array.
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]

# They are using min() to grab the element from a set with the lowest count in the input. 
def find_uniq(arr):
        return min(set(arr),key=arr.count)

# Importing counter but using next()
from collections import Counter

def find_uniq(arr):
    return next(k for k,v in Counter(arr).items() if v == 1)