# Playing with digits
"""
    Some numbers have funny properties. For example:
    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

    Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
    we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
    In other words:

    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
"""
# Parameters or Edge Cases:
"""
    inputs will be positive integers
    the 1st input is the integer we are breaking up into individual digits and raising it to the powers of (p + current index iteration)
"""
# Return:
"""
    if the quotient of the sum of all the individual digits to the power of (p + current index iteration) is a positive integer then return that quotient else return -1
"""
# Examples:
"""
    n is being broken up into the alphabet in ascending order progression
    (n, p) = > (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    (89, 1) => 1
    (92, 1) => -1
    (46288, 3) => 51
    (41, 5) => 25
    (114, 3) => 9
    (8, 3) => 64
"""
# Pseudocode:
"""
    take in the integer n and break it up into an array of digits
    iterate through the array of digits starting at the first digit take the value to the power of (p + current index value)
    sum the array and divide the result by the original input integer that we broke up into an array
    if the quotient is a positive integer return that quotient else return -1
"""

# my answer
def dig_pow(n, p):
    # declare an empty array
    y = []
    # take in the integer n and break it up into an array of digits
    x = [int(e) for e in str(n)]
    # iterate through the array of digits starting at the first digit take the value to the power of (p + current index value)
    for i in range(len(x)):
        y.append(x[i]**(p + i))
    # sum the array and divide the result by the original input integer that we broke up into an array
    # if the quotient is a positive integer return that quotient else return -1
    if sum(y) % n == 0:
        return int(sum(y)/n)
    return -1

# # my answer refactored
def dig_pow(n, p):
    x = [int(e) for e in str(n)]
    y = [x[i]**(p + i) for i in range(len(x))]
    return int(sum(y)/n) if sum(y) % n == 0 else -1

print(dig_pow(89, 1)) # 1
print(dig_pow(92, 1)) # -1
print(dig_pow(46288, 3)) # 51
print(dig_pow(41, 5)) # 25
print(dig_pow(114, 3)) # 9
print(dig_pow(8, 3)) # 64

# best practices and most clever 
# This is returning floats!!! The only change would be in the return statement int(s/n).
# using enumerate() to grab both index and element of the object you're iterating/stepping through adding to a declared integer
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

# The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
# using divmod() to divide the result of the sum of the array by the original input and assigning it to the variable to k and the remainder to fail
# if there is a remainder represented by if fail exists return -1 else return k
# personal note: I love the one liner enumerate in this example
def dig_pow(n, p):
    # quotient, remainder = divmod(dividend, divisor)
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k

# here they are using // to divide and only return whole integers
def dig_pow(n, p):
  t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)) )
  return t//n if t%n==0 else -1

# brute force loop for e in string example and not relying on index location 
# instead they are stepping by 
# I love clean and easy this code is to step through.
def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1

# here they are using map() inside enumerate to change the values back into an integer type instead of per each iteration
def dig_pow(n, p):
    digits = sum([d**(p+i) for i, d in enumerate(map(int, str(n)))])
    return digits/n if digits%n is 0 else -1