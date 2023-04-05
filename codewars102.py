# Odd or Even?
# Parameters or Edge Cases:
    # input will be an array of integers that can be negative
# Return:
    # if the sum of the elements is even return "even" else "odd"
# Examples:
    # [0] => "even"
    # [0, 1, 4] => "odd"
    # [0, -1, -5] => "even"
# Pseudocode:
    # sum the array using sum() 
    # if the result divided by 2 has a remainder return "odd" else return "even"

# my answer, best practices and most clever
def odd_or_even(arr):
    return "even" if sum(arr) %2 == 0 else "odd"

# my answer refactored implicit return
odd_or_even = lambda a : "even" if sum(a) % 2 == 0 else "odd"

print(odd_or_even([0])) # even
print(odd_or_even([0, 1, 4])) # odd
print(odd_or_even([0, -1, -5])) # even

# for element in array
def oddOrEven(arr):
    c = 0
    for i in arr:
        c += i
    if c % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
# using index call of an array
oddOrEven = lambda a: ['even','odd'][sum(a)%2]

# using bitwise operator &
def oddOrEven(arr):
    return 'odd' if sum(arr) & 1 else 'even'

# math index call of an object 
def oddOrEven(arr):
    return {True: 'odd', False: 'even'}[sum(arr)%2]

# index call of a string stepping by 2
oddOrEven=lambda a:'eovdedn'[sum(a)%2::2]