# Beginner Series #3 Sum of Numbers
# Parameters or Edge Cases:
    # inputs will be integers that can be positive or negative
# Return:
    # the sum of the integers in-between the inputs inclusively
    # if the 2nd input is greater than the first input increment else decrement
    # if the inputs are equal return one of the inputs
# Examples:
    # (1, 0) --> 1 (1 + 0 = 1)
    # (1, 2) --> 3 (1 + 2 = 3)
    # (0, 1) --> 1 (0 + 1 = 1)
    # (1, 1) --> 1 (1 since both are same)
    # (-1, 0) --> -1 (-1 + 0 = -1)
    # (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# Pseudo Code:
    # range(start, stop, step) solution
    # if first input is greater than second return the sum of the range from a to b -1 decrementing by 1
    # if first input is less than second return the sum of the range from a to b + 1 incrementing by 1

    # brute force solution
    # declare an empty variable set to 0
    # if the inputs are equal return an input
    # if the first input is greater than the second iterate through decrementing by 1 until you reach the second input adding to the set variable each iteration
    # if the first input is less than the second iterate through incrementing by 1 until you reach the second input adding to the set variable each iteration


    
# my answer using range(start, stop, step)
def get_sum(a,b):
    if a > b:
        return sum(range(a, b -1 , -1))
    else:
        return sum(range(a, b +1 , 1))
    
# my answer refactored implicit return
get_sum = lambda a,b: sum(range(a, b -1 , -1)) if a > b else sum(range(a, b +1 , 1))


# my answer brute force while loop
def get_sum(a,b):
    total = 0
    if a==b:
        return a
    elif a > b:
        while a != b -1:
            total += a
            a -= 1
        return total
    else:
        while a != b + 1:
            total += a
            a += 1
        return total
    
print(get_sum(1, 0)) # 1
print(get_sum(1, 2)) # 3
print(get_sum(0, 1)) # 1
print(get_sum(1, 1)) # 1
print(get_sum(-1, 0)) # -1
print(get_sum(-1, 2)) # 2

# best practices
# wow incredibly clever to get around decrementing range()
# grab the lowest value and use it as range start highest value for range stop and increment by 1
# if b is less than a then start at b and end at a incrementing by 1
# if a is less than b then start at a and end at b incrementing by 1
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

# most clever
# Gauss sum formula
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2

# same idea but not using min() and max()
def get_sum(a,b):    
    if a > b:        
        [a,b] = [b,a]
    if b != 0:
        b += 1     
    else:
        b = 0        
    return sum(x for x in range(a, b,1))

# clever way of getting around min and max by resetting inputs
def get_sum(a,b):
    if a>b : a,b = b,a
    return sum(range(a,b+1))

# using sorted() to pull first min() instead of using min() and max()
def get_sum(a,b):
    a,b = sorted((a, b))
    return sum(range(a, b+1))

# same as my brute force answer but using for loops instead of while loops
def get_sum(a,b):
    soma=0
    if a==b:
        return a
    elif a > b:
        for i in range(b,a+1):
            soma += i
        return soma
    else:
        for i in range(a,b+1):
            soma += i
        return soma
    
# creating a list for each element and summing that list
def get_sum(a,b):
    return sum([x for x in range(min(a,b),max(a,b)+1)])