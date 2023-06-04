# Build a pile of Cubes
"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45

findNb(91716553919377) --> -1
"""
# Parameters or Edge Cases:
"""
inputs will be integers
"""
# Return:
"""
the value of n where m = the iteration of (n - index)**3 where index is from 0 to n but exclusive to n meaning the final value will be 1**3 and not 0**3
"""
# Examples:
"""
    4183059834009 => 2022
    24723578342962 => -1
    135440716410000 => 4824
    40539911473216 => 3568
    26825883955641 => 3218
"""
# Pseudocode:
"""
    # declare a global variable for volume and set it at 0
    # iterate from 1 to m + 1 to include m
    # add the current element to the power of 3 to volume
    # if volume is equal to m then return n
    # once volume has iterated to more than m return -1
"""

# my answer
def find_nb(m):
    # declare a global variable for volume and set it at 0
    volume = 0
    # iterate from 1 to m + 1 to include m
    for n in range(1, m+1):
        # add the current element to the power of 3 to volume
        volume += n**3
        # if volume is equal to m then return n
        if volume == m:
            return n
        # once volume has iterated to more than m return -1
        elif volume > m:
            return -1


    
print(find_nb(4183059834009)) # 2022
print(find_nb(24723578342962)) # -1
print(find_nb(135440716410000)) # 4824
print(find_nb(40539911473216)) # 3568
print(find_nb(40539911473216)) # 3568

# best practices
def find_nb(m):
    # start at n equal to 1
    n = 1
    # declare a variable and set it equal to 0 to represent the volume per each iteration comparing to the input volume m
    volume = 0
    # while the volume is less than m
    while volume < m:
        # reassign volume adding n^3 per each loop
        volume += n**3
        # if the current volume is equal to m then return the current n
        if volume == m:
            return n
        # increment by 1 per each iteration
        n += 1
    # once volume is no longer less than m return -1
    return -1

# most clever DEPRECATED!!
from math import floor, sqrt

def find_nb(m):
    # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
    # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
    # so take square root and round down the result.
    n_canidate = int(floor(sqrt(2 * sqrt(m))))
    if (n_canidate * (n_canidate + 1) / 2 )**2 == m:
        return n_canidate
    else:
        return -1
    
# most clever updated
def find_nb(m):
    n = int((2*m**0.5)**0.5) # Inverse of (n*(n+1)/2)**2 with int() as smart floor function.
    if (n*(n+1))**2 == 4*m:  # Check if possible, multiply away the division to avoid floats.
        return n
    return -1

# similar to best practices while loop
def find_nb(m):
    i,sum = 1,1
    while sum < m:
        i+=1
        sum+=i**3
    return i if m==sum else -1

# while loop with m counting backwards
def find_nb(m):
    n = 0
    while (m > 0):
        n += 1
        m -= n**3
    return n if m == 0 else -1

# similar to most clever but switching the conditional returns
def find_nb(m):
    '''
    n cube sum m = (n*(n+1)//2)**2
    then n**2 < 2*m**0.5 < (n+1)**2
    and we can proof that for any n, 0.5 > (2*m**0.5)**0.5 - n**2 > 2**0.5 - 1 > 0.4
    '''
    n = int((2*m**0.5)**0.5)
    if (n*(n+1)//2)**2 != m: return -1
    return n