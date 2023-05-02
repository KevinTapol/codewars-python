# Are they the "same"?
"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

Note for C
The two arrays have the same size (> 0) given as parameter in function comp.
"""
# Parameters or Edge Cases:
"""
    inputs will be 2 arrays of the same size length 
    inputs can be null or empty
    the elements will be positive integers
"""
# Return:
"""
    if one and not both of the arrays are null/empty return false
    if both inputs are null/empty return true
    if both arrays are equal length and the 2nd input array elements are squares of the 1st input array per element return true
    else false
"""

# Examples:
"""
    [121, 144, 19, 161, 19, 144, 19, 11] , [121, 14641, 20736, 361, 25921, 361, 20736, 361] => True
    because 2nd input array of elements square root exists in the 2nd input [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

    [121, 144, 19, 161, 19, 144, 19, 11] , [231, 14641, 20736, 361, 25921, 361, 20736, 361] => False
    [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19] 231 is not a square root

    [121, 144, 19, 161, 19, 144, 19, 11] , [121, 14641, 20736, 36100, 25921, 361, 20736, 361] => False
    [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19] 190 does not exist in the 1st input

"""
# Pseudocode:
"""
    if both inputs are null or empty return True
    if one and not both the of the input arrays are null return false
    create an array of the elements squared from the 1st input array
    sort the array and compare it to a sorted copy of the 2nd input array for boolean return true for equal false for not
"""
# my answer
def comp(a, b):
    # if both inputs are null or empty return True
    if a is None and b is None:
        return True
    # if one and not both the of the input arrays are null return false
    if a is None or b is None:
        return False
    # create an array of the elements squared from the 1st input array
    c = [e*e for e in a]
    # sort the array and compare it to a sorted copy of the 2nd input array for boolean return true for equal false for not
    return sorted(b) == sorted(c)

# best practices and most clever
# here they are using a try except for true false
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


# conditionals checking for several cases 
def comp(array1, array2):
    if any([array1 is None, array2 is None]):
        if array1 == array2 is None:
            print("Both None")
            return True
        else:
            print("Only one is None")
            return False
    elif len(array1) != len(array2):
        print("Lengths not equal")
        return False
    else:
        array1 = [abs(int_) for int_ in array1]
        array2 = [abs(int_) for int_ in array2]
        array1.sort()
        array2.sort()
        print("Comparing equal length arrays.")
        return all([array1[i] ** 2 == array2[i] for i in range(len(array1))])

# cleaner solutions of my answer using [] instead of None
# here they are also appending instead of creating a one line copy per element squared 
def comp(a, b):
    if a == [] and b == []:
        return True
    if a == [] or b == []:
        return False
    c = []
    for i in sorted(a):
        c.append(i*i)
    return sorted(c) == sorted(b)

# one line version of my answer using None
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

# using if input instead of None or == []
def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []

# using isinstance() instead of None [] or if input
def comp(a1, a2):
    return isinstance(a1, list) and isinstance(a2, list) and sorted(x*x for x in a1) == sorted(a2)

# something I forgot is that you can shorten the import as a variable in the import statement
from collections import Counter as c
def comp(a1, a2):
    return a1 != None and a2 != None and c(a2) == c( elt**2 for elt in a1 )

# using zip() for array comparison
def comp(a1, a2):
    return None not in (a1, a2) and all(x**2 == y for x, y in zip(sorted(a1), sorted(a2)))