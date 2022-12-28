"""
Opposites Attract
Parameters or Edge Cases:
    inputs will be non-negative integers 
Return:
    boolean true if one input int is odd and the other even else false
Examples:
    (1,4), True)
    (2,2), False)
    (0,1), True)
    (0,0), False)
Psuedo Code:
    check if the first input has no remainder when divided by 2 and the second does or the first input does and the second doesn't
    return true else false
"""

# my answer
def lovefunc(flower1, flower2):
    # check if the first input has no remainder when divided by 2 and the second does or the first input does and the second doesn't
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 %2 != 0 and flower2 % 2 == 0):
        return True
    else:
        return False

print(lovefunc(1,4)) # True
print(lovefunc(2,2)) # False
print(lovefunc(0,1)) # True
print(lovefunc(0,0)) # False

# my answer refactored lambda one liner
lovefunc = lambda f1, f2: True if(f1 % 2 == 0 and f2 % 2 != 0) or (f1 %2 != 0 and f2 % 2 == 0) else False

# best practices and most clever
# If you add up two odd numbers you get an even number and if you add two even numbers you get even. So the only way you won't get an even sum is when you add an odd to an even.
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

# another clever answer is just to check if the remainders are not equal
def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2

# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# & AND	Sets each bit to 1 if both bits are 1
lovefunc = lambda a, b: (a ^ b) & 1

# funny ... importing Tuple then taking the inputs as integers
from typing import Tuple

def lovefunc(*flowers: Tuple[int]) -> bool:
    """ Are Timmy & Sarah in love? """
    return len(list(filter(lambda _it: _it % 2, flowers))) == 1