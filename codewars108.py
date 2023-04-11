# Array.diff
# Parameters or Edge Cases:
    # input will be 2 arrays of integers
# Return:
    # an array of inputs that are in the 1st array but not in the 2nd array
# Examples:
    # array_diff([1,2],[1]) == [2]
    # array_diff([1,2,2,2,3],[2]) == [1,3]
# Pseudocode
    # declare an empty array
    # iterate through the inputs and check for what is in the first input but not in the second

# my answer
def array_diff(a, b):
    x = []
    for e in a:
        if e not in b:
            x.append(e)
    return x

# my answer refactored implicit return
array_diff = lambda a,b: [e for e in a if e not in b]

print(array_diff([1,2],[1])) # [2]
print(array_diff([1,2,2,2,3],[2])) # [1,3]

# best practices and most clever 
# same as my implicit return answer
def array_diff(a, b):
    return [x for x in a if x not in b]

# filter()
def array_diff(a, b):
    return filter(lambda i: i not in b, a)

# while nested inside a for
def array_diff(a, b):
    #your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a

# using count() as a while condition
def array_diff(a, b):
    for x in b:
        while a.count(x) != 0:
            a.remove(x)
    return a

# triple nested conditional iterations
def array_diff(a, b):
    i = 0
    while i < len(a):
        for x in b:
            for y in a:
                if y == x:
                    a.pop(a.index(x))
        i += 1
    return a