# Count the Digit
"""
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.

Examples:
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.
"""
# Parameters or Edge Cases:
"""
input n will be integers greater than or equal to 0
input d will be an integer greater than or equal to 0 and less than or equal to 9
"""
# Return:
"""
    the total count that input d occurs in the array of squares of inputs from 0 to n
"""
# Examples:
"""
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.

    5750, 0 => 4700
    11011, 2 => 9481
    12224, 8 => 7733
    11549, 1 => 11905
    14550, 7 => 8014
    8304, 7 => 3927
    10576, 9 => 7860
    12526, 1 => 13558
    7856, 4 => 7132
    14956, 1 => 17267
"""
# Pseudocode:
"""
    # declare an integer count and set it equal to 0
    # iterate from 0 to n inclusively so use n+1 to include n
    # declare a local for loop variable named num_string and set it equal to an empty string
    # square each integer, convert it into a string and set it equal to num_string
    # for each instance of input d converted to string occurs in num_string add 1 to count
    # outside of the for loop return count

"""

# my answer
def nb_dig(n, d):
    # declare an integer count and set it equal to 0
    count = 0
    # iterate from 0 to n inclusively so use n+1 to include n
    for e in range(n+1):
    # declare a local for loop variable named num_string and set it equal to an empty string
        num_string = ''
    # square each integer, convert it into a string and set it equal to num_string
        num_string = str(e**2)
    # for each instance of input d converted to string occurs in num_string add 1 to count
        count += num_string.count(str(d))
    # outside of the for loop return count
    return count

# my refactored answer removing the local variable num_string
def nb_dig(n, d):
    count = 0
    for e in range(n+1):
        count += str(e**2).count(str(d))
    return count

# my refactored answer for Codewars only
def nb_dig(n, d):
    return sum([str(e**2).count(str(d)) for e in range(n+1)])

# lambda implicit return one liner
nb_dig = lambda n,d: sum([str(e**2).count(str(d)) for e in range(n+1)])

print(nb_dig(10,1)) # 4
print(nb_dig(25,1)) # 11
print(nb_dig(5750, 0)) # 4700
print(nb_dig(11011, 2)) # 9481
print(nb_dig(12224, 8)) # 7733

# best practices and most clever
# similar to my answer but using element * element instead of element**2
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))

# this answer returns as a string of the count and not an index return
def nb_dig(n, d):
   return ''.join(str(n * n) for n in range(n + 1)).count(str(d))

# using regex findall() with f string returning an integer
# very clever imo
# returning the length of the string of occurrences of d in each element^2 
import re
def nb_dig(n, d):
    count = 0
    for i in range(n+1):
        count += len(re.findall(f"{d}", str(i**2)))
    return count

# using map()
def nb_dig(n, d):
    d = str(d)
    return sum([i.count(d) for i in list(map(str, map(lambda x:x*x , range(n+1))))])