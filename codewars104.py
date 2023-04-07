# Who likes it?
# Parameters or Edge Cases:
    # inputs will be an array of strings representing names
    # the array can be empty
# Return:
    # return the input array names with the following conditions in examples of empty, 1, 2, 3 and 4 or more
# Examples:
    # []                                -->  "no one likes this"
    # ["Peter"]                         -->  "Peter likes this"
    # ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    # ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    # ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Pseudocode:
    # get the length of the array
    # if it is empty return "no one likes this"
    # if it is 1 return f"{input} likes this"
    # if it is 2 return f"{input 1} and {input 2} like this"
    # if it is 3 return f"{input 1}, {input 2} and {input 3} like this"
    # if it is 4 or greater return f"{input 1}, {input 2} and {length of the array -2} others like this"

# my answer
def likes(names):
    # if it is empty return "no one likes this"
    if len(names) == 0:
        return "no one likes this"
    # if it is 1 return f"{input} likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    # if it is 2 return f"{input 1} and {input 2} like this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    # if it is 3 return f"{input 1}, {input 2} and {input 3} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    # if it is 4 or greater return f"{input 1}, {input 2} and 2 others like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) -2} others like this"

print(likes([])) # "no one likes this"
print(likes(["Peter"])) # "Peter likes this"
print(likes(["Jacob", "Alex"])) # "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"])) # "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"])) # "Alex, Jacob and 2 others like this"

# best practices and most clever
# here they are returning an object based on the length of the input array or the value 4 whichever is lower then using string interpolation with .format() based on the key value pairs
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

# here they declare the dictionary or object outside of the return
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)

# using switch or match case instead of conditionals
def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

# using %s for string interpolation
def likes(names):
    total = len(names)
    return ( 'no one likes this' if total == 0 else
             '%s likes this' % names[0] if total == 1 else
             '%s and %s like this' % (names[0], names[1]) if total == 2 else
             '%s, %s and %s like this' % (names[0], names[1], names[2]) if total == 3 else
             '%s, %s and %s others like this' % (names[0], names[1], total-2) )