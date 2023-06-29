# Sum of a sequence
"""
Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
"""
# Parameters or Edge Cases:
"""
inputs will be integers greater than or equal to 0
"""
# Return:
"""
the sum of a range starting with the first input, stopping at the second input and stepping by the third input
if the first input is greater than the second input return 0
"""
# Examples:
    # 2,2,2 --> 2
    # 2,6,2 --> 12
    # 1,5,1 --> 15
    # 1,5,3  --> 5
# Pseudocode:
    # if the first input is greater than the second return 0
    # declare an empty array named result
    # iterate through that array starting at the first input, stopping at the second input + 1 to include the stop value and stepping by the 3rd input
    # append each value to result
    # sum result and return it

# my answer
def sequence_sum(start, stop, step):
    # if the first input is greater than the second return 0
    if start > stop:
        return 0
    # declare an empty array named result
    result = []
    # iterate through that array starting at the first input, stopping at the second input + 1 to include the stop value and stepping by the 3rd input
    for i in range(start,stop + 1,step):
    # append each value to result
        result.append(i)
    # sum result and return it
    return sum(result)

# my answer refactored
def sequence_sum(start, stop, step):
    if start > stop:
        return 0
    result = [i for i in range(start,stop + 1, step)]
    return sum(result)

# my answer refactored for Codewars
def sequence_sum(a,b,c):
    return 0 if a>b else sum([i for i in range(a,b+1,c)])

# lambda implicit return for Codewars only
sequence_sum = lambda a,b,c: 0 if a>b else sum([i for i in range(a,b+1,c)])


print(sequence_sum(2,2,2)) # 2
print(sequence_sum(2,6,2)) # 12
print(sequence_sum(1,5,1)) # 15
print(sequence_sum(1,5,3)) # 5

# best practices and most clever
# when generating a range if the start is greater than the stop it will generate an empty object r[0]. Sum() on that object will return 0.
# This means that the my answer of generating an array is unnecessary since range implicitly returns an object that sum() can be used on
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))

# O notation using n * (n+1) / 2 where strides = (stop - start) // step return (strides + 1) * (step * strides/2 + start)
# The coder broke it down with the comment below
def sequence_sum(b, e, s):
  k = (e - b) // s
  return (1 + k) * (b + s * k / 2) if b <= e else 0

"""
# For learning purposes. From slowest to fastest.
#
# sn = sorted(Timer('sequence_sum_n(1, 1_000_000, 18)', steup=this_file).repeat(10, 1000))
# Averages:
# s1 = 5.40761180743560299078
# s2 = 0.00299944687756124049
# s3 = 0.00121562700535378094

def sequence_sum(start, stop, step):
    return sum(range(start, stop+1, step))

def range_sum(n):
    return n * (n+1) / 2

def multiples_sum(divisor, n):
    return range_sum(n//divisor) * divisor

def sequence_sum(start, stop, step):
    diff = stop - start
    return 0 if start > stop else start * (diff // step + 1) + multiples_sum(step, diff)
 
def sequence_sum(start, stop, step):
    strides = (stop - start) // step
    return 0 if start > stop else (strides + 1) * (step * strides/2 + start)
"""