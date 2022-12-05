# Parameters or Edge Cases:  inputs will be an array of integers
# if there is nothing to sum, the sum is default to 0
# Return: sum of all pos numbers of a given array
# Examples: [1,-4,7,12] => 1 + 7 + 12 = 20
# Psuedo Code: return 0 for empty arrays 
#               iterate through the array to find all nums > 0 
#               add all the even nums and return the sum

# my answer
def positive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        sum = 0
    for x in arr:
        if x > 0:
            sum = sum + x
    return sum

print(positive_sum([1,-4,7,12])) # 20

# best practices and most clever
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# sum(filter(lambda))
def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

# sum(map(lambda()))
def positive_sum(arr):
    return sum(map(lambda x: x if x > 0 else 0, arr))

# sum(max())
def positive_sum(arr):
    return sum( max(i, 0) for i in arr )