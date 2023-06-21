# Sum of the first nth term of Series
"""
Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""
# Parameters or Edge Cases:
"""
    inputs will be Natural Numbers meaning integers
    will the inputs be postive and greater than 0? IN ADVANCED TEST CASES INPUTS CAN BE 0

    can the inputs be empty or null?
"""
# Return:
"""
    return a string representation of a quotient sum of 1 over denominator starting at 1 stopping at length of the input and stepping by 3
"""
# Examples:
"""
    1 => "1.00"
    2 => "1.25"
    3 => "1.39"
"""
# Pseudocode:
"""
    # declare an empty array result
    # declare an integer i and set it to 1
    # while the length of result is less than the input
    # append 1/i to result
    # increment i by 3
    # sum result
    # round result to 2 decimal places and convert it to a string
    # if the length of the string is equal to 3 then append '0'
    # if the input is 0 then return '0.00'
    

"""

# my answer
def series_sum(n):
    # declare an empty array result
    result = []
    # declare an integer i and set it to 1
    i = 1
    # while the length of result is less than the input
    while len(result) < n:
        # append 1/i to result
        result.append(1/i)
        # increment i by 3
        i += 3
    # sum result
    result = sum(result)
    # round result to 2 decimal places and convert it to a string
    result = str(round(result,2))
    # if the length of the string is equal to 3 then append '0'
    if len(str(result)) == 3:
        result += '0'
        return result
    # if the input is 0 then return '0.00'
    if n == 0:
        return '0.00'
    # return result
    return result

# my answer refactored inline declaring variables and sum()round() string converting 
def series_sum(n):
    result, i = [], 1
    while len(result) < n:
        result.append(1/i)
        i += 3
    result = str(round(sum(result),2))
    if len(str(result)) == 3:
        result += '0'
        return result
    if n == 0:
        return '0.00'
    return result


print(series_sum(1)) # "1.00"
print(series_sum(2)) # "1.25"
print(series_sum(3)) # "1.39"
print(series_sum(5)) # "1.57"

# best practices and most clever
# :.2f is forcing 2 decimal places with string interpolation it can also be done with f string f'{value:.2f}'
# the range is going from 1 to n n being exclusive and handling the step by 3 with math internally
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

# similar to the idea of %s and %d but using %.2f instead
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum

# one liner of the above
def series_sum(n):
    return '%.2f' % sum(1.0 / i for i in range(1, 3 * n, 3))

# using f string with :.2f
def series_sum(n):
    return f'{sum(1/d for d in range(1,n*3,3)):.2f}'