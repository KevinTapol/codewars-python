"""
Keep Hydrated
Parameters or Edge Cases:
    given a number representing hour(s) that can be a float 
Return:
    an integer representing litres of water to be consumed 
Example:
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
Psuedo Code:
    take the input time float and round down or convert to an int
    multiply by 0.5 then round down or convert to an int
    return the product
"""

# my answer
# From the description of the kata, I thought you are supposed to get the integer of the time AND the integer of the final product. All you need is the final product integer. int(time*0.5)
def litres(time):
    # take the input time float and round down or convert to an int
    # multiply by 0.5 then round down or convert to an int
    # return the product
    return int(int(time)*0.5)

print(litres(3)) # 1
print(litres(6.7)) # 3
print(litres(11.8)) # 5

# my answer refactored to lambda
litres = lambda time: int(int(time)*0.5)

# best practices and most clever
# ! // divides with the integral result discarding the remainder
def litres(time):
    return time // 2

# using math to round down
import math
def litres(time):
    return math.floor(.50 * time)

# using math and remove remainder with .trunc()
import math

def litres(time):
    return math.trunc(time/2)