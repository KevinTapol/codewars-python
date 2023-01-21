# If you can't sleep, just count sheep!!
# Parameters or Edge Cases:
    # inputs will be non negative integers 
    # input can be 0
# Return:
    # an empty string if the input is 0
    # else string "input sheep..." input times in concatenation
# Examples:
    # count_sheep(0) # ""
    # count_sheep(1) # "1 sheep..."
    # count_sheep(2) # "1 sheep...2 sheep..."
    # count_sheep(3) # "1 sheep...2 sheep...3 sheep..."
# Psuedo Code:
    # declare an empty string sheep
    # loop through starting at index 0 inclusively and ending at n exclusively 
    # add 1 for each index concatenating index + 1 to string " sheep..."
    # return the concatenated string sheep
# my answer
def count_sheep(n):
    # declare an empty string sheep
    sheep = ''
    # loop through starting at index 0 inclusively and ending at n exclusively 
    for i in range(n):
        # add 1 for each index concatenating index + 1 to string " sheep..."
        sheep = sheep + (str(i+1) + " sheep...")
    # return the concatenated string sheep 
    return sheep

# my answer refactored lambda for loop
count_sheep = lambda n: "".join(str(i+1) + " sheep..." for i in range(n))

print(count_sheep(0)) # ""
print(count_sheep(1)) # "1 sheep..."
print(count_sheep(2)) # "1 sheep...2 sheep..."
print(count_sheep(3)) # "1 sheep...2 sheep...3 sheep..."

# best practices and most clever
# using f string and starting at index 1 instead of index 0 and ending at index n + 1 instead of index n
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

# similar to my answer but starting at index 1 inclusively and ending at n+1 exclusively
def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep

# using .format() instead of + for concatenating
def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1))

# using f string instead of .format() or + for concatenating
# also starting at index 0 inclusively and ending at index n exclusively
def count_sheep(n):
    return ''.join(f'{x+1} sheep...' for x in range(n))

# using %d instead of f string, .format(), or + for concatenating
def count_sheep(n):
    return "".join("%d sheep..." % (i + 1) for i in range(n))

# using %i instead of %d
count_sheep = lambda __:''.join('%i sheep...'%(_+1) for _ in range(__))

# while loop starting at 1 inclusively and ending at n inclusively
def count_sheep(n):
    s = ""
    i = 1
    while i <= n:
        s += str(i)+" sheep..."
        i += 1
    return s