# Grasshopper - Check for factor
"""
This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number.
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
"""
# Return:
"""
    return true if the first input divided by the second input does not have a remainder else false
"""
# Examples:
"""
    10, 2 => True
    9, 2 => False
"""
# Psuedocode:
"""
    divide base by factor and compare the result equal to 0 to implicitly return true for 0 else false
"""

# my answer and best practices
def check_for_factor(base, factor):
    return base % factor == 0

# my answer refactored implicit return
check_for_factor = lambda b,f: b % f == 0

print(check_for_factor(10, 2)) # True
print(check_for_factor(9, 2)) # False

# most clever
# using truthy falsy for all values not 0 return true else false
def check_for_factor(b,f):
    return not b%f

# using .is_integer() to check if it is an integer
# the only integer returned would be 0 for true else they would be fractions for false
check_for_factor = lambda b, f: (b/f).is_integer()