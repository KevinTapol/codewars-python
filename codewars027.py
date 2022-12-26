"""
Beginner Series #2 Clock
Parameters or Edge Cases:
    inputs will be integers representing hours minutes seconds with the following constraints
    0 <= hours <= 23
    0 <= minutes <= 59
    0 <= seconds <= 59
Return:
    the time since midnight in milliseconds
Example:
    (past(0,1,1),61000)
    (past(1,1,1),3661000)
    (past(0,0,0),0)
    (past(1,0,1),3601000)
    (past(1,0,0),3600000)
Psuedo Code:
    take in hours and multilpy by 60 to get minutes
    add input minutes to the converted minutes then multiply by 60 to get seconds 
    add input seconds to the converted minutes 
    multiply by 1000 to get the total time into milliseconds
    return the milliseconds
"""

# my answer
def past(h, m, s):
    # take in hours and multilpy by 60 to get minutes 
    # add input minutes to the converted minutes then multiply by 60 to get seconds 
    # add input seconds to the converted minutes multiply by 1000 to get the total time into milliseconds
    # return the milliseconds
    return ((h*60 + m) * 60 + s) * 1000

print(past(0,1,1)) # 61000
print(past(1,1,1)) # 3661000
print(past(0,0,0)) # 0
print(past(1,0,1)) # 3601000
print(past(1,0,0)) # 3600000

# my answer refactored lambda one liner implicit return
past = lambda h, m, s : ((h*60 + m) * 60 + s) * 1000

# best practices and most clever
# here they converted everything to seconds added them up then finally multiplied by 1000 to get milliseconds
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000

# VERY CLEVER!!! using timedelta to do the math
from datetime import timedelta
def past(h, m, s):
    return timedelta(hours=h, minutes=m, seconds=s) // timedelta(milliseconds=1) 

# same as above but using a lambda function
from datetime import timedelta
past = lambda h,m,s: timedelta(hours=h, minutes=m, seconds=s).seconds * pow(10, 3)
# def past(h, m, s):
#     return timedelta(hours=h, minutes=m, seconds=s).seconds

# interseting converting everything to milliseconds declaring an empty variable and adding to it
def past(h, m, s):
    ms = 0
    ms += 3600000 * h
    ms += 60000 * m
    ms += 1000 * s
    return ms

# using decimal notation
def past(h, m, s):
    return h * 3.6e+6 + m * 6e4 + s * 1e3

# converting to a list and using sum() on the list
def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        L=[]
        L.append(h*3600000)
        L.append(m*60000)
        L.append(s*1000)
        return sum(L)