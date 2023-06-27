# Breaking chocolate problem
"""
Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than or equal to 0
"""
# Return: 
"""
    the amount of breaks to achieve 1 by 1 squares
"""
# Examples:
"""
    5, 5 => 24
    7, 4 => 27
    1, 1 => 0
    0, 0 => 0
    6, 1 => 5
"""
# Pseudocode:
"""
    # if n or m is 0 then return 0
    # return the product of the inputs -1
"""

# my answer
def break_chocolate(n, m):
    # if n or m is 0 then return 0
    if n*m == 0:
        return 0
    # return the product of the inputs -1
    return n*m -1

# my answer refactored
def break_chocolate(n, m):
    return 0 if n*m == 0 else n*m -1

# lambda answer
break_chocolate = lambda n,m: 0 if n*m == 0 else n*m -1

# best practices and most clever
# return values of 0 or more
def breakChocolate(n, m):
    return max(n*m-1,0)

# try except block
def breakChocolate(n, m):
    try:
        int(n)
        int(m)
    except ValueError:
        return 0
    
    if (n > 0) and (m > 0):
        return (n*m)-1
    else:
        return 0
    
# very descriptive comments
def breakChocolate(n, m):
    # == Simple proof that starting vertically and horizontally is the same. ==
    # For an n*m chocolate bar :
    #
    # You first cut vertically, making n-1 cuts
    # You then cut horizontally each pieces (n pieces) m-1 times
    # You get n-1+n*(m-1) = n-1+nm-n = 1+nm
    #
    # Cut horizontally first and you'll make m-1 cuts followed by n-1 cuts for each (m) piece
    # You get m-1+m*(n-1) = m-1+mn-m = 1+nm
    #
    # Both ways, you're gonna have to make n*m-1 cut
    #
    # A more natural representation is to understand that you'll have to manually cut off each
    # and every chocolate piece. At the end you'll have two pieces stuck together, at which
    # point a single cut will "create" two pieces.
    #
    # It's also worth mentioning that it doesn't matter whether you make vertical and horizontal
    # cuts only, whatever you do, even if you zigzag through your chocolate bar with a knife,
    # you'll always need exactly as much slices as pieces you want, minus 1.
    return n*m-1 if n*m>0 else 0