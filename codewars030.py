"""
Beginner Series #1 School Paperwork
Parameters or Edge Cases:
    inputs will be integers and can be negative
    if n < 0 or m < 0 return 0
Return:
    an integer representation of how many blank pages you need given integer n number of students and m number of blank pages
Examples:
    (paperwork(5,5), 25, "Failed at Paperwork(5,5)")
    (paperwork(-5,5), 0, "Failed at Paperwork(-5,5)")
    (paperwork(5,-5), 0, "Failed at Paperwork(5,-5)")
    (paperwork(-5,-5), 0, "Failed at Paperwork(-5,-5)")
    (paperwork(5,0), 0, "Failed at Paperwork(5,0)") 
Psuedo Code:
    if either inputs are less than 0 return 0
    else return the product of the inputs
"""

# my answer 
def paperwork(n, m):
    # if either inputs are less than 0 return 0
    if n < 0 or m < 0:
        return 0
    # else return the product of the inputs
    else:
        return n*m

print(paperwork(5,5)) # 25
print(paperwork(-5,5)) # 0
print(paperwork(5,-5)) # 0
print(paperwork(-5,-5)) # 0
print(paperwork(5,0)) # 0

# my answer refactored lambda oneliner
paperwork = lambda n, m: 0 if n < 0 or m < 0 else n*m

# best practices
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

# most clever
# very clever here they are using the product of the max values of either 0 or the input
# this reminds me of JS Math.max((n, 0)*(m, 0))
def paperwork(n, m):
    return max(n, 0)*max(m, 0)

# lambda one liner of product return but using min() if the product is less than 0 return 0 else return the product
paperwork = lambda a,b: a*b if min(a,b)>0 else 0

# using abs() for absolute value
def paperwork(n, m):
    return 0 if abs(n) != n or abs(m) != m else n*m

# using lists
def paperwork(n, m):
    return [0, n * m][n > 0 and m > 0]

# *args and **kwarsg agruments and key word arguements 
# importing methods reduce() and mul()
from operator import mul
from functools import reduce

def paperwork(*args):
    return reduce(mul, args) if min(args) > 0 else 0