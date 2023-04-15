# Find The Parity Outlier
# Parameters or Edge Cases:
    # inputs will be an array with a length of at least 3 
    # elements in the array will be integers 
    # integers can be negative, positive or very large
    # integers will either be all odd and 1 even or all even and 1 odd
# Return:
    # return the odd element if all other elements are even else even element if all other elements are odd
# Examples:
    # [2, 4, 0, 100, 4, 11, 2602, 36]
    # Should return: 11 (the only odd number)
 
    # [160, 3, 1719, 19, 11, 13, -21]
    # Should return: 160 (the only even number)

    # [2, 4, 6, 8, 10, 3] => 3
    # [2, 4, 0, 100, 4, 11, 2602, 36] => 11
    # [160, 3, 1719, 19, 11, 13, -21] => 160
# Pseudocode
    # declare an empty array called odd
    # declare an empty array called even
    # iterate through the input array and if the element is even, append it to the even array
    # if it is odd, append it to the odd array
    # if the length of the even array is 1 then return the first index of that array else return the first index of the odd array

# my answer
def find_outlier(integers):
    odd = []
    even = []
    for e in integers:
        if e % 2 == 0:
            even.append(e)
        else:
            odd.append(e)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]
    
# my answer refactored
def find_outlier(integers):
    odd = []
    even = []
    [even.append(e) if e % 2 == 0 else odd.append(e) for e in integers]
    return odd[0] if len(odd) == 1 else even[0]



print(find_outlier([2, 4, 6, 8, 10, 3])) # 3
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) # 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) # 160

# to funny best practices and most clever is a version of my refactored answer but with odd and even arrays containing the for if statements
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

# declaring only 1 array and adding the remainders of the division using modulus % to the array and sum the array
# sum(elements % 2) on all the elements will return 0's for the evens and 1's for the odds.
# If the array is all evens and 1 odd, then return the index of the element where element % 2 == 1.
# If the array is all odds and 1 even, then return the index of the element where element % 2 == 0.
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

# same answer but refactored by another coder
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(sum(parity) == 1)]

# clever since remainders will either return 0's for evens or 1's for odds
#  use "!=" instead of "^" and it will be faster to execute and easier to read
def find_outlier(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False

# using filter() to create an array of the even integer elements
def find_outlier(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]

# here they are using // 2 to ignore remainder
def find_outlier(nums):

  base_parity = sum( x%2 for x in nums[:3] ) // 2
  
  for i in range(len(nums)):
    if nums[i] % 2 != base_parity:
      return nums[i]

# implicit return one liner using next()
# very clever but as the coder states not meant for production
# here they are comparing the remainders of the first 3 elements
find_outlier=lambda l:l[0] if l[1]%2!=l[0]%2!=l[2]%2 else next(n for n in l if n%2 != l[0]%2)