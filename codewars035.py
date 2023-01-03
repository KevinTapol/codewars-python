"""
Is n divisible by x and y?
Parameters or Edge Cases:
    inputs will be integers greater than 0
Return:
    a boolean True or False if the input n is divisible by both input x and y
Examples:
    1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
    2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
    3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
    4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5
    (is_divisible(3,2,2),False)
    (is_divisible(3,3,4),False)
    (is_divisible(12,3,4),True)
    (is_divisible(8,3,4),False)
Psuedo Code:
    divide n by x and n by y 
    if both statements result in no remainder return true
    else return false
"""
# my answer
def is_divisible(n,x,y):
    # divide n by x and n by y 
    # if both statements result in no remainder return true
    if n % x == 0 and n % y == 0:
        return True
    # else return false
    else:
        return False

print(is_divisible(3,2,2)) # False
print(is_divisible(3,3,4)) # False
print(is_divisible(12,3,4)) # True
print(is_divisible(8,3,4)) # False

# my answer refactored to lambda one liner
is_divisible = lambda n,x,y: True if n % x == 0 and n % y == 0 else False

# best practices
# using implicit boolean return for statements
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

# most clever
# Wow I didn't know you could do multiple equal comparisions with an implicit return.
def is_divisible(n, x, y):
    return n % x == n % y == 0

# De Morgan's Law of unions and opposites of sets are related
def is_divisible(n, x, y):
    return not n % x and not n % y

# another De Morgan's Law
def is_divisible(n,x,y):
    return not (n%x or n%y)

# clever 0 + 0 = 0 implicit boolean return
def is_divisible(n,x,y):
    return n % x + n % y == 0 

# Clever way of checking no remainder without using modulus %
# Using // to divide takes only the whole integer from the number even if there is a float. 
# Using / to divide will return the number in decimal places if it is a float.
def is_divisible(n,x,y):
    if x == 0 or y == 0: return False
    return n//x == n/x and n//y == n/y

# clever using n*n and then dividing by x*y for implicit boolean return
is_divisible = lambda n,x,y: not ((n**2)%(x*y))

# both statments must be True to return a True but here they call by list index
def is_divisible(n,x,y):
    return (False, True)[n%x==0 and n%y==0]

# using is_integer()
# Return True if the float instance is finite with integral value, and False otherwise
def is_divisible(n,x,y):
    x = n/x
    y = n/y
    
    return x.is_integer() and y.is_integer()

# I didn't know that law had a name
def is_divisible(n, x, y):
    return not (n % x or n % y)  # Only False and False will be True (De Morgan's laws)

# De Morgan's first law states that the complement of the union of two sets A and B is equal to the intersection of the complement of the sets A and B.

# De Morgan's Laws describe how mathematical statements and concepts are related through their opposites. In set theory, De Morgan's Laws relate the intersection and union of sets through complements. In propositional logic, De Morgan's Laws relate conjunctions and disjunctions of propositions through negation.