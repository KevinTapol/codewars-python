# Equal Sides Of An Array
"""
You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
"""
# my description
"""
    given an array whose length returns an odd number, find the element in the array where the sum of the elements to the left are equal to the sum on the right. Return that index not the value. If no value exists, return -1. If the array is even, return -1. 
    
    If you are given an array with multiple answers, return the lowest correct index. I think what they mean to say is if the array is full of integer 0, then return the index of the first 0
    what if the array length is 1? do I return index 0?
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of integers that can be negative or 0    
    length of the array can be 0 < arr < 1000 meaning it will never be empty or null
"""
# Return:
"""
    the index location of the element where the sum of the elements to the left are equal to the sum on the right of an odd length array else return -1
"""
# Examples:
"""
    [1,2,3,4,3,2,1] =>3
    [1,100,50,-51,1,1] =>1
    [1,2,3,4,5,6] =>-1
    [20,10,30,10,10,15,35] =>3
    [20,10,-80,10,10,15,35] =>0
    [10,-80,10,10,15,35,20] =>6
    list(range(1,100)) =>-1
    [0,0,0,0,0]) =>0,"Should pick the first index if more cases are valid meaning return array[0]"
    [-1,-2,-3,-4,-3,-2,-1]) =>3
    list(range(-100,-1))) =>-1
"""
# Pseudocode:
"""
    # declare sum of elements starting left to right and set it to 0
    # sum the input array
    # using enumerate, iterate through the input array starting at 0
    # subtract the current element value from sumR
    # if sumL is equal to sumR return the current i
    # else add the value of the current element to sumL
    # outside of the for loop return -1
"""

# my answer
def find_even_index(arr):
    # declare sum of elements starting left to right and set it to 0
    sumL = 0
    # sum the input array
    sumR = sum(arr)
    # using enumerate, iterate through the input array starting at 0
    for i, e in enumerate(arr, 0):
        # subtract the current element value from sumR
        sumR -= e
        # if sumL is equal to sumR return the current i
        if sumL == sumR:
            return i
        # else add the value of the current element to sumL
        sumL += e
    # else return -1
    return -1

# my answer without comments
def find_even_index(arr):
    sumL = 0
    sumR = sum(arr)
    for i, e in enumerate(arr, 0):
        sumR -= e
        if sumL == sumR:
            return i
        sumL += e
    return -1

print(find_even_index([1,2,3,4,3,2,1])) # 3
print(find_even_index([1,100,50,-51,1,1])) # 1
print(find_even_index([1,2,3,4,5,6])) # -1
print(find_even_index([20,10,-80,10,10,15,35])) # 0
print(find_even_index([0,0,0,0,0])) # 0 


# best practices and most clever
# Here they are creating the sum of array copies. One that ends at the current iterator value and one that starts at the current iterator value + 1.
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# same line thinking as best practices and most clever but one lining the for loop
def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
    return r[0] if r else -1

# You can declare multiple variables in one line
def find_even_index(arr):
    left, right = 0, sum(arr)
    for i, e in enumerate(arr):
        right -= e
        if left == right:
            return i
        left += e
    return -1

# implicit return lambda using next() with enumerate() here they are using __ for element representation but not using it
# They are using enumerate to avoid nesting a for loop inside a for loop. This way they can one line the answer.
find_even_index = lambda arr: next((i for i, __ in enumerate(arr) if sum(arr[:i]) == sum(arr[i+1:])), -1)

# using while loop instead of a for loop
def find_even_index(arr):
    arridx= 0
    arrlen= len(arr)
    while arridx < arrlen:
        lnum= sum(arr[0:arridx])
        rnum= sum(arr[arridx+1:arrlen])
        if lnum == rnum: break #skips else also. so, break means found...
        arridx += 1
    else:
        arridx= -1
        pass
    return arridx #solution above takes less time, than one extra if checked below.
    #return arridx if arridx < arrlen else -1