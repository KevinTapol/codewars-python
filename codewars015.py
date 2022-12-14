"""
Counting Sheep
Parameters or Edge Cases:
    input will be an array of boolean True False values
Return:
    an integer represtation counting the total number of boolean True in the array
Examples:
    [True,  True,  True,  False,
     True,  True,  True,  True ,
     True,  False, True,  False,
     True,  False, False, True ,
     True,  True,  True,  True ,
     False, False, True,  True]
     returns 17
Psuedo Code:
    declare a count variable and set it to 0
    iterate through the array for every element that equals boolean true add 1 to the variable count
    return the count variable
    MAKE SURE THE FUNCTION NAME IS count_sheeps NOT count_sheep
"""
#  my answer and 2nd best practices
def count_sheeps(sheep):
    # declare a count variable and set it to 0
    count = 0
    # iterate through the array for every element that equals boolean true add 1 to the variable count
    for i in range(len(sheep)):
        if sheep[i] == True:
            count += 1
    # return the count variable        
    return count

# my answer using a list length
def count_sheeps(arr):
    # declare an empty list
    new_list = []
    # loop through the input list and add each boolean true to the empty list
    for i in range(len(arr)):
        if arr[i] == True:
            new_list.append(arr[i])
    # return the length of the list containing all boolean true        
    return len(new_list)        


print(count_sheeps([True,  True,  True,  False,
     True,  True,  True,  True ,
     True,  False, True,  False,
     True,  False, False, True ,
     True,  True,  True,  True ,
     False, False, True,  True])) # 17

# best practices and most clever
# .count() will return the number of occurances of the paramter in this case boolean True
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

# a refactored version of for loop with len()
def count_sheeps(sheep):
  return len([x for x in sheep if x])

# using sum() and filter()
def count_sheeps(sheep):
  return sum(filter(None, sheep))

# one liner lambda with sum() and for loop
count_sheeps = lambda x: sum(1 for i in x if i)

# using len() and one liner for loop
def count_sheeps(sheep):
    return len([1 for i in sheep if i == True])

# using filter()
def count_sheeps(arrayOfSheeps):
  return sum(filter(lambda x: x == True, arrayOfSheeps))

# using lambda with if statements
count_sheeps=lambda a:sum([i if i==True else False for i in a])