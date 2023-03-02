# L1: Set Alarm
# Parameters or Edge Cases:
    # inputs will be boolean values
# Return:
    # true if first input is true and second input is false else return false
# Examples:
    # setAlarm(True, True) -> False
    # setAlarm(False, True) -> False
    # setAlarm(False, False) -> False
    # setAlarm(True, False) -> True
# Pseudo Code:
    # if first input is true and second input is false then return true
    # else return false
# my answer
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False
    
# my answer refactored implicit nested conditionals truthy
set_alarm = lambda e, v: e and not v
    
print(set_alarm(True, True)) # False
print(set_alarm(False, True)) # False
print(set_alarm(False, False)) # False
print(set_alarm(True, False)) # True

# best practices and most clever 
# I strongly disagree with using truthy/falsy
def set_alarm(employed, vacation):
    return employed and not vacation

# IMO most clever
# using * to iterate through the inputs like ... spread in JavaScript
# then using 1 and 0 for true and false implicit return 
# Note the double equal for comparison and not setting input values
set_alarm=lambda *a:a==(1,0)

# using & for and ~ for not
def set_alarm(employed, vacation):
    return employed & ~vacation

# same idea as first input = 1 and second input = 0
def set_alarm(a, b):
    return a - b == 1

# Clever the only True is when employed is true and vacation is false which means employed equals 1 and vacation equals 0
def set_alarm(employed, vacation):
    return employed > vacation

# nesting conditionals 
def set_alarm(employed, vacation):
    # Your code here
    if employed:
        if vacation:
            return False
        return True
    return False

# shortest answer
set_alarm=int.__gt__

# lol this doesn't always work
# what is happening here is a random True False  for both inputs and this will fail repeatedly until the first input randomly tests true and the second input test false
# using random.choice()
import random
def set_alarm(employed, vacation):
    return random.choice((True,False))

# clever commenting
def set_alarm(employed, vacation):
    """
    a | b |  ( a & ~b )
    --|---|-------------
    0 | 0 | (0 & ~0) = 0
    0 | 1 | (0 & ~1) = 0
    1 | 0 | (1 & ~0) = 1
    1 | 1 | (1 & ~1) = 0
    """
    return employed and not vacation

# funny using while condition
def set_alarm(employed, vacation):
    while employed == True and vacation == True:
        return False
    while employed == False and vacation == True:
        return False
    while employed == True and vacation == False:
        return True
    while employed == False and vacation == False:
        return False
    
set_alarm(True, True)
