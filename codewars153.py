# Data Reverse
"""
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
"""
# Parameters or Edge Cases:
"""
    inputs will be an array of 0's and 1's with a length of 32
    not testing for empty, null, special characters or strings
"""
# Return:
"""
    break the input array into 2d array of 4 arrays each with a length of 8 
    then reverse the order of the arrays and convert it back into a single array
"""
# Examples:
"""
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0] => [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
"""
# Pseudocode:
"""
    # declare an empty array to represent a 2d array of the input
    # iterate through the input stepping by 8
    # append array copies starting at the current index and stopping at the current index + 8 to capture the 8th element inclusively
    # declare an empty array result
    # iterate through the 2d array bytes grabbing each 1d array in reversed order
    # iterate through each 1d array and append each element to result
    # return result
"""

# my answer
def data_reverse(input):
    # declare an empty array to represent a 2d array of the input bytes_2D
    bytes_2D = []
    # iterate through the input stepping by 8
    for i in range(0, len(input), 8):
        # append array copies starting at the current index and stopping at the current index + 8 to capture the 8th element inclusively
        bytes_2D.append(input[i:i+8])
    
    # declare an empty array result 
    result = []
    # iterate through the 2d array bytes_2D grabbing each 1d array in reversed order
    for byte_1D in reversed(bytes_2D):
        # iterate through each 1d array and append each element to result
        for e in byte_1D:
            result.append(e)
    # return result
    return result

# my answer refactored for Codewars
def data_reverse(input):
    bytes_2D = [input[i:i+8] for i in range(0, len(input), 8)]    
    return [e for byte_1D in reversed(bytes_2D) for e in byte_1D]


print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0])) # [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

# best practices
# similar to my answer but reversing the order directly in the range statement
# also instead of result = result.append() they use .extend()
# extend() method adds the specified list elements (or any iterable) to the end of the current list.
def data_reverse(data):
  res = []
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  return res

# most clever
# same as best practices but one liner
def data_reverse(data):
    return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]

# interesting here they declare separate functions for creating a 2d array, reversing each block then flattening the 2d array
def blockify(data):
    result = []
    for i in range(0, len(data), 8):
        result.append(data[i:i+8])
    return result

def unblockify(blocks):
    return [bit for block in blocks for bit in block]

def data_reverse(data):
    return unblockify(blockify(data)[::-1])

# while loop conditional with the length of the input
def data_reverse(data):
    data2 = []
    j = len(data)
    while j > 0:
        data2 = data2 + data[j-8:j]
        j = j - 8
    return data2

# wow... using sum() to flatten lists
def data_reverse(data):
    return sum([data[i-8:i] for i in range(len(data),0,-8)], [])