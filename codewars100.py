# Ones and Zeros
# Parameters or Edge Cases:
    # inputs will be arrays with only 1s and 0s
    # length of arrays can be empty or null
# Return:
    # the binary value of the elements in the array to integer value
# Examples:
    # [0, 0, 0, 1] ==> 1
    # [0, 0, 1, 0] ==> 2
    # [0, 1, 0, 1] ==> 5
    # [1, 0, 0, 1] ==> 9
    # [0, 0, 1, 0] ==> 2
    # [0, 1, 1, 0] ==> 6
    # [1, 1, 1, 1] ==> 15
    # [1, 0, 1, 1] ==> 11
# Pseudo Code:
    # concat the elements in the array into a single string
    # convert the string of 1s and 0s to integer using the 2nd argument of int() with a value of 2 representing binary
    # return the integer

# my answer
def binary_array_to_number(arr):
    b = ""
    for e in arr:
        b += str(e)
    return int(b, 2)

# my answer refactored implicit return
binary_array_to_number = lambda arr: int("".join(str(e) for e in arr), 2)

print(binary_array_to_number([0, 0, 0, 1])) # 1
print(binary_array_to_number([0, 0, 1, 0])) # 2
print(binary_array_to_number([1, 1, 1, 1])) # 15
print(binary_array_to_number([0, 1, 1, 0])) # 6

# best practices and most clever
# using map(convert each element into a string, input to iterate through)
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

# very clever but you need to understand binary for this answer
# If we use double dabble method, then we just put the above process in reverse.
# our number is 1 1 0 1 (so we start with leftmost digit - 1 and continue to the right)
# 0 * 2 + 1 = 1 (does it remind you anything? Look at step 4 of decimal to binary process - 0 is quatinent and 1 is remainder)
# 1 * 2 + 1 = 3 (look at the step 3 of decimal to binary)
# 3 * 2 + 0 = 6
# 6 * 2 + 1 = 13
# One note: when using double dabble method we always start wit 0 * 2 (as there is no previous digit to the left-most digit of the binary number)
def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s

# using the powers of 2 for binary
# also reversed() iterates through the argument in reversed order .reverse() reverses entirely
def binary_array_to_number(arr):
    return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))

# using [::-1] instead of reversed()
def binary_array_to_number(arr):
  return sum( 2**i for i, n in enumerate( arr[ ::-1 ] ) if n )

# using reduce()
# n << 1 | b is bitwise operation: given n and b (one digit each), it returns n*2 for the n<<1 part (bitwise left shift) then do the bitwise operation or between n*2 and b.

# reduce will apply that operation to the elements of arr, but in an accumulating way:

# arr = [0,1,1,0,1] => (n << 1 | b)(0,1) => 0*2 | 1 = 1 => arr is now equivalent to: [1,1,0,1], then => (n << 1 | b)(1,1) => 2 | 1 = as, bits: "10" | "1" = "11" = actually 3 => arr is now equivalent to: [3,0,1], then => ... => arr is now equivalent to: [6,1], then => ... => arr is now equivalent to: [13], then return 13
from functools import reduce

def binary_array_to_number(arr):
    append_bit = lambda n, b: n << 1 | b
    return reduce(append_bit, arr)

# same as above but implicit return inside the reduce()
from functools import reduce

def binary_array_to_number(a):
    return reduce(lambda t,b:t*2+b,a)


# testing for inputs
def binary_array_to_number(arr):
    if type(arr) is list and len(arr)>0:
      return int(''.join(str(e) for e in arr), 2)
    return -1


# using a while loop
def binary_array_to_number(arr):
  no_of_elements = len(arr)
  k = no_of_elements 
  sum = 0
  while k != 0:
      sum = sum + arr[no_of_elements-k]*(2**(k-1))
      k = k - 1
  return sum