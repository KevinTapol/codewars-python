# 
# Parameters Edge Case:
    # inputs will be an array of integers
    # the integer can be negative and/or more than 1 digit
    # There will always be only one integer that appears an odd number of times.
# Return:
    # the integer the appears an odd number of times
# Examples:
    # [7] should return 7, because it occurs 1 time (which is odd).
    # [0] should return 0, because it occurs 1 time (which is odd).
    # [1,1,2] should return 2, because it occurs 1 time (which is odd).
    # [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
    # [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
# Pseudo Code:
    # iterate through the array for element in the array
        # if that element occurs and odd number of times in the input array return that element

# my answer and best practices
def find_it(seq):
    for e in seq:
        if seq.count(e) %2 != 0:
            return e
        
# my answer refactored implicit return returning a list and grab the first element in the list 
find_it = lambda s: [e for e in s if s.count(e) %2 != 0][0]

print(find_it([7])) # 7
print(find_it([0])) # 0
print(find_it([1,1,2])) # 2
print(find_it([0,1,0,1,0])) # 0
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])) # 4

# most clever
# It works because of two things. First, xor is communicative so you don't have to worry about the order of the values. A list like [1, 2, 3, 1, 2, 3, 4] can be thought of as [1, 1, 2, 2, 3, 3, 4]. Second, there's a truth table involved when xor'ing two values:
# 0 xor 1 is 1 0 xor 123 is 123
# ^^ 0 xor anything is going to produce the other number
# 0 xor 0 is 0 1 xor 1 is 0 123 xor 123 is 0
# So because you're xor'ing all the matching numbers first that's producing 0 (1 xor 1) and then 0 (2 xor 2) and then 0 (3 xor 3) which leaves you with 4 (0 xor 4).
import operator
from functools import reduce
def find_it(xs):
    return reduce(operator.xor, xs)


# variation of my implicit but using truthy
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

# importing Counter(arrayInput).items() instead of .count()
from collections import Counter
def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]

# same idea as grabbing values only once with set() but taking the value with .pop() instead of index call [0]
def find_it(seq):
    nums = set()
    for num in seq:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
    return nums.pop()

# For every number x, we have:
# x ^ x == 0 for any pair of occurrences of x x ^ x ^ x == x for any odd occurrences of x
# As the xor operation is both comutative and associative, so the order of the numbers/operations doesn't matter.
# Thus, every number that appear in pairs are set to zero and the single number with odd occurrences remains with its bits set.
def find_it(seq):
    result = 0
    for x in seq:
        result ^= x
    return result

# groupby() with next()
from itertools import groupby

def find_it(seq):
    return next(k for k, g in groupby(sorted(seq)) if len(list(g)) % 2)