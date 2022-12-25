"""
A Needle in the Hatstack
Parameters or Edge Cases:
    input will be an array of multiple data types 
    input will NOT be empty
    input will contain the string 'needle'
Return:
    find the index of the string needle and return "found the needle at possition {index of string "needle"}"
Examples:
    ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
    
    find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]), 'found the needle at position 3')
    find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']), 'found the needle at position 5')
    find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]), 'found the needle at position 30')
Psuedo Code:
    search the array and return the .index() of the string "needle"
    return an f string "found the needle at position {array.index("needle", start_pos, end_pos)}"
"""
# my answer
def find_needle(arr):
    # search the array and return the .index() of the string "needle"
    # return an f string "found the needle at position {array.index("needle", start_pos, end_pos)}"
    return f"found the needle at position {arr.index('needle')}"

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])) # "found the needle at position 5"
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])) # 'found the needle at position 3'
print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'])) # 'found the needle at position 5'
print(find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54])) # 'found the needle at position 30'

# my answer refactored lambda one liner
find_needle = lambda arr: f"found the needle at position {arr.index('needle')}"

# best practices and most clever
# %d is replaced by whatever is after the % assuming it is a number; anything else will throw a TypeError. If there is more than one marker (i.e. "%d %s"), put everything in a tuple after the %-sign.
def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

# alternative answers
# 'found the needle at position %d' % haystack.index('needle')
# 'found the needle at position {}'.format(haystack.index('needle'))
# f'found the needle at position {haystack.index('needle')}

# concatenation
def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

# brute force for loop
def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i

# using .format()
def find_needle(haystack):
    return 'found the needle at position {position}'.format(position = haystack.index('needle'))

# using while loop
def find_needle(haystack):
    i = 0
    while i < len(haystack):
        if haystack[i] == 'needle':
            return 'found the needle at position ' + str(i)
        i += 1