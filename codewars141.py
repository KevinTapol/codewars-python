# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!! 
"""
The number 89
89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 
89 = 8**1 + 9**2

The next number in having this property is 135:
See this property again 135: 1**1 + 3**2 + 5**3

We need a function to collect these numbers, that may receive two integers a,b that defines the range [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
"""
# Parameters or Edge Cases:
"""
    inputs will always be 2 positive integers 
"""
# Return:
"""
    return an array given the inputs range inclusively where the sum of the individual digits to the power of their index location starting at 1 is equal to the number itself.
"""
# Examples:
"""
    90, 100 --> []
    1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
"""
# Pseudocode:
"""
    # declare an empty array result
    # iterate starting and stopping at the given inputs INCLUSIVELY meaning stop + 1 
    # if the current element is equal to the sum of each digit to the power of its index location starting at index + 1
    # append the element to result
    # return result
"""

# my answer
def sum_dig_pow(a, b): 
    # declare an empty array result
    result = []
    # iterate starting and stopping at the given inputs INCLUSIVELY meaning stop + 1 
    for i,e in enumerate(range(a, b+1)):
        # if the current element is equal to the sum of each digit to the power of its index location starting at index + 1
        if e == sum([int(v)**(i+1) for i, v in enumerate(str(e))]):
            # append the element to result
            result.append(e)
    # return result
    return result

# my answer refactored eliminating the outer nested enumerate to range
def sum_dig_pow(a, b): 
    result = []
    for e in range(a, b+1):
        if e == sum([int(v)**(i+1) for i, v in enumerate(str(e))]):
            result.append(e)
    return result

# my answer refactored for codewars ALSO MOST CLEVER!!!
def sum_dig_pow(a, b): 
    return [e for e in range(a, b+1)  if e == sum([int(v)**(i+1) for i, v in enumerate(str(e))])]

# my answer refactored to implicit return for codewars only
sum_dig_pow = lambda a,b: [e for e in range(a, b+1)  if e == sum([int(v)**(i+1) for i, v in enumerate(str(e))])]

print(sum_dig_pow(90, 100)) # []
print(sum_dig_pow(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_dig_pow(1, 100)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

# best practices
# the same idea as my answer but they split up the nested for loop into another function
def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow(a, b): 
    return [x for x in range(a,b + 1) if x == dig_pow(x)]

# same idea as all the previous answers but broken down into easier to read code of nested for loops
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for number in range(a, b+1):
        digits = [int(i) for i in str(number)]
        s = 0
        for idx, val in enumerate(digits):
            s += val ** (idx + 1)
        if s == number:
            res.append(number)
    return res

# same idea but using a while loop 
def sum_dig_pow(a, b):
    ans = []
    while a <= b:
        if sum(int(j) ** k for j,k in zip(str(a),range(1,len(str(a)) + 1))) == a:
            ans += [a]
        a += 1
    return ans