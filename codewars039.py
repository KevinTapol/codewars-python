"""
Simple multiplication
Parameters or Edge Cases:
    inputs will be positive integers
Return:
    the product of 8 and even integer inputs else product of 9 and odd integer inputs
Examples:
    (simple_multiplication(2), 16)
    (simple_multiplication(1), 9)
    (simple_multiplication(8), 64)
    (simple_multiplication(4), 32)
    (simple_multiplication(5), 45)
Psuedo Code:
    if the input integer when divided by 2 does not have a remainder then multiply by 8 and return the product
    if the input integer when divided by 2 has a remainder then multiply the input integer by 9 and return the product
"""
# my answer
def simple_multiplication(number):
    # if the input integer when divided by 2 does not have a remainder then multiply by 8 and return the product
    if number % 2 == 0:
        return number * 8
    # if the input integer when divided by 2 has a remainder then multiply the input integer by 9 and return the product
    else:
        return number * 9

print(simple_multiplication(2)) # 16
print(simple_multiplication(1)) # 9
print(simple_multiplication(8)) # 64
print(simple_multiplication(4)) # 32 
print(simple_multiplication(5)) # 45

# my answer refactored
simple_multiplication = lambda n: n*8 if n % 2 == 0 else n*9

# best practices
# if number %2 returns a remainder return number * 9 
def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

# most clever
# n%2 will return either 0 no remainder or 1 there is a remainder 
# if the number is even n  * (8 + 0)
# if the number is odd n * (8 + 1)
def simple_multiplication(n) :
    return n * (8 + n%2)

# ANDing a value with 1 like this will result in 1 if the value's rightmost bit is set, and 0 if it is not.
# And because 0 is generally considered "false" in most languages, and non-zero values considered "true", we can simply say as a shortcut:
#  bitwise AND operator. The value 1 in binary is expressed as 1:
simple_multiplication = lambda a : a * (8 + (a & 1))

# list call for index
def simple_multiplication(n):
    return n * [8, 9][n % 2]