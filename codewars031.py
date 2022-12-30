"""
Count of positives/sum of negatives
Parameters or Edge Cases:
    input will be an array of intergers that can be postive or negative
    the array can be empty or null
Return:
    a new array of 2 elements the first being the total number count of elements that are positive integers greater than 0 and the second is the sum of the negative numbers 
Examples:
    (count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
    (count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
    (count_positives_sum_negatives([1]),[1,0])
    (count_positives_sum_negatives([-1]),[0,-1])
    (count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
    (count_positives_sum_negatives([]),[])
Psuedo Code:
    if the array is null, return a null array [] 
    common techniques for checking if an array is null is a boolean if conditional
    ex list_null = [] if bool(list_null): return [] or if not list_null: return []
    a less common technique is if array == []: return []

    if the array contains only 0 integers, return [0,0]
    common technique is to use the all() to check if elements in the array are equal to a value
    ex if all(elements == 0 for elements in array)

    declare a variable pos_count integer representing the length of the array of positive integers greater than 0
    declare another variable neg_sum respresenting the sum of negative integers
    take in the array and filter the array taking the positive integers greater than 0
    get the length of that array and set it equal to pos_count
    take in the array and filter the array taking the negative integers
    sum the array and set the sum equal to neg_sum
    return an array with the first element being pos_count and the second being neg_sum
"""

# my answer
def count_positives_sum_negatives(arr):
    # if the array is null, return a null array [] 
    # common techniques for checking if an array is null is a boolean if conditional 
    # ex list_null = [] if bool(list_null): return [] or if not list_null: return []
    if not arr:
        return []
    # if the array contains only 0 integers, return [0,0]
    elif all(x == 0 for x in arr):
        return [0, 0]
    else:
        # declare a variable pos_count integer representing the length of the array of positive integers greater than 0
        pos_count = 0
        # declare another variable neg_sum respresenting the sum of negative integers
        neg_sum = 0
        # take in the array and filter the array taking the positive integers greater than 0
        # get the length of that array and set it equal to pos_count
        pos_count = len(list(filter(lambda e: e > 0, arr)))
        # take in the array and filter the array taking the negative integers
        # sum the array and set the sum equal to neg_sum
        neg_sum = sum(list(filter(lambda f: f < 0, arr)))
    # return an array with the first element being pos_count and the second being neg_sum
    return [pos_count, neg_sum]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) # [10,-65]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])) # [8,-50]
print(count_positives_sum_negatives([1])) # [1,0]
print(count_positives_sum_negatives([-1])) # [0,-1]
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0])) # [0,0]
print(count_positives_sum_negatives([])) # []

# my answer refactored if len([]) like [].length for JS returns 0 and sum([]) returns 0 then I don't need the elif case in my original answer
count_positives_sum_negatives = lambda arr: [] if not arr else [len(list(filter(lambda e: e > 0, arr))), sum(list(filter(lambda f: f < 0, arr)))]

# best practices 
# brute force for loop
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

# most clever
# brute force for loop 
# add 1 for each element greater than 0 
# sum each element less than 0
# return [add, sum]
# here they are using the the boolean if len(arr) meaning boolean true if there is a length and if there isn't meaing false return an empty array
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

# 2nd most clever
def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

# the first is summing the count where n > 0 and the second is summing n where n < 0
# this was a bit confusing at first thinking sum would sum the n values where n > 0 instead of the count of n > 0
# I would much rather use length of the array instead for clarification but it's nice to know this is a possibility
def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []

# one liner lambda works with python3 if arr else reminds me of truthy falsy much cleaner than my lamba function
count_positives_sum_negatives = lambda arr: [len([e for e in arr if e>0]), sum(e for e in arr if e<0)] if arr else []

# same as above but using array methods
def count_positives_sum_negatives(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output

# here they are using if not array for checking null array
def count_positives_sum_negatives(input):
    if not input:
        return []
    count_ = 0
    sum_ = 0
    for element in input:
        if element > 0:
            count_ += 1
        elif element < 0:
            sum_ += element
    return [count_, sum_]

# I love this answer just because it's a function that calls a class. Thank you to WMaC51 for submitting this answer!
class Cpsn():
    def __init__(self, nums=[]): # initializing the class and inputs
        self.nums = nums # setting the input array as nums
        self.count = 0 # declaring a count variable equal to 0
        self.sum = 0 # declaring a sum variable equalt to 0
    @property
    def pos_count(self): # creating a method/function pos_count
        for i in self.nums:
            if i > 0: # for each element greater than 0
                self.count += 1 # add 1 to the variable count 
        return self.count # return the count
    @property
    def neg_sum(self): # creating a method/function neg_sum
        for i in self.nums: 
            if i < 0: # for each element less than 0  
                self.sum += i # add each element to the variable sum
        return self.sum # return the sum

def count_positives_sum_negatives(arr): # the function that Codewars is calling
    if arr == []: # if the array is null
        return [] # return a null array
    cpsn = Cpsn(arr) # creating an object of the class named cpsn where the input is arr
    return [cpsn.pos_count, cpsn.neg_sum] # return an array of the cpsn object function pos_count and function neg_sum