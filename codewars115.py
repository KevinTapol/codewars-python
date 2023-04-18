# Take a Ten Minutes Walk
"""You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise."""
# Parameters or Edge Cases:
    # input will be an array of string letters 'n', 's', 'e' and 'w'
    # inputs will never be empty
# Return:
    # If the length of the input array is 10 elements and the count of the input string cardinal directions are equal to the input string opposite cardinal direction return true else false
# Examples:
    # ['n','s','n','s','n','s','n','s','n','s'] => True
    # ['w','e','w','e','w','e','w','e','w','e','w','e'] => False
    # ['w'] => False
    # ['n','n','n','s','n','s','n','s','n','s'] => False
    # ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] => True
# Pseudocode
    # if the count of the strings are equal to its string opposite cardinal direction and the length of the input array is 10 return true
    # else false

# my answer
def is_valid_walk(walk):
    if (walk.count("n")==walk.count("s") and walk.count("e")==walk.count("w") and len(walk)==10):
        return True
    else:
        return False

# my answer refactored, best practice and most clever
def is_valid_walk(x):
    return x.count("n")==x.count("s") and x.count("e")==x.count("w") and len(x)==10

# my answer refactored implicit return
is_valid_walk = lambda x: len(x) == 10 and x.count('n') == x.count('s') and x.count('e') == x.count('w')


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # False
print(is_valid_walk(['w'])) # False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # False
print(is_valid_walk(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'])) # True


# for element in array counting 
def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    x, y = 0, 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        else:
            return False

    return x == 0 and y == 0

# importing Counter
from collections import Counter

def is_valid_walk(walk):
    if len(walk) == 10:
        walkmap = Counter(walk)
        return walkmap['n'] == walkmap['s'] and walkmap['e'] == walkmap['w']
    return False

# creating a object/dictionary 
# # In this solution, instead of using an iterating counter,
# I added a dictionary to count opposite directions to assure
# we get to the starting point and avoiding unnecessary iterations

def is_valid_walk(walk):
    #Reduced time with dictionary count
    my_dict = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for i in walk:
        my_dict[i] += 1
        
    if (len(walk) == 10 and 
    my_dict['n'] == my_dict['s'] and 
    my_dict['e'] == my_dict['w']):
        return True
    return False