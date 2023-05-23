# Multiplication table
"""
Your task, is to create N×N multiplication table, of size provided in parameter.
For example, when given size is 3:
1 2 3
2 4 6
3 6 9
should return [[1,2,3],[2,4,6],[3,6,9]]
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
    inputs will not be empty
"""
# Return:
"""
    a 2d array representing a multiplication table where the input both the number of arrays inside the 2d array and elements in each array
"""
# Examples:
"""
    1 => [[1]]
    2 => [[1, 2], [2, 4]]
    3 => [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    4 => [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    5 => [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
"""
# Pseudocode:
"""
    # declare a variable count and set it equal to 1
    # declare an empty array named result
    # iterate to the length of the input integer
    # declare a local array to the for loop called row
    # iterate to the length of the input integer 
    # multiply count by the current index + 1 and append the product to row
    # outside the inner for loop, append row to result
    # outside the nested for loop return result
"""
# # my answer
# def multiplication_table(size):
#     # declare a variable count and set it equal to 1
#     count = 1
#     # declare an empty array named result
#     result = []
#     # iterate to the length of the input integer
#     for i in range(size):
#     # declare a local array to the for loop called row
#         row = []
#     # iterate to the length of the input integer 
#         for j in range(size):
#     # multiply count by the current index + 1 and append the product to row
#             row.append(count*(j+1))
#         count += 1
#     # outside the inner for loop, append row to result
#         result.append(row)
#     # outside the nested for loop return result
#     return result

# my answer refactored
# removing count and starting at 1 stopping at input+1 for both loops
def multiplication_table(size):
    result = []
    for i in range(1,size +1):
        row = []
        for j in range(1,size +1):
            row.append(i*(j))
        result.append(row)
    return result

# my answer refactored for Codewars implicit return lambda one liner
multiplication_table = lambda s: [[i*j for j in range(1, 1+s)] for i in range(1, 1+s)]

print(multiplication_table(1)) # [[1]]
print(multiplication_table(2)) # [[1, 2], [2, 4]]
print(multiplication_table(3)) # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
print(multiplication_table(4)) # [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
print(multiplication_table(5)) # [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

# best practices and most clever
# my lambda but not implicit return
# Strongly disagree for best practices as it's not easily readable
def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

# here they are adding 1 to each index internally instead of setting the index to 1
def multiplicationTable(size):
    return [[(x + 1) * (y + 1) for y in range(size)] for x in range(size)]

# same idea as best practices but they are using list() instead of []
def multiplicationTable(n):
    return [ list(range(i, n*i +1, i)) for i in range(1, n +1) ]

# here they are using map() to create a copy of the outer for loop using _ instead of j
multiplication_table = lambda _: [[*map(lambda _: _*c,range(1,_+1))] for c in range(1,_+1)]

# using a while loop
# declaring an empty list globally, appending to it locally, and resetting it back to empty
def multiplication_table(size):
    n=1
    list1=[]
    list2=[]
    while n!=size+1:
        for i in range(1,size+1):
                list1.append(n*i)
        list2.append(list1)
        list1=[]
        n+=1
    return list2