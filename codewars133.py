# Build Tower
"""
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
"""
# Return:
"""
    an array of with a with a length of the input value
    each input value will be a string of white spaces and '*'
    the final input will be only  '*' and each preceding element strings first and last '*' will be replaced with white spaces until you reach the first element which will have only 1 '*' and contain only white spaces.
"""
# Examples:
"""
    3 => [
  "  *  ",
  " *** ", 
  "*****"
]
    6 => [
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
"""
# Pseudocode:
"""
    # declare a string of the length of each element of the array with every space being the '*' given the input of n_floors
    # declare an array and append that first string value
    # loop through until the center of the string length exclusively
    # convert the individual string into an array of each element with a string character
    # replace the first that is not white space with white space
    # replace the last character that is not white space with white space
    # reassign the string asterisks as the current iteration array back into a string
    # append that string to result
    # reverse result
    # return result
"""

# my answer
def tower_builder(n_floors):
    # declare a string of the length of each element of the array with every space being the '*' given the input of n_floors
    asterisks = '*'*(n_floors*2 -1)
    # declare an array and append that first string value
    result = [asterisks]
    # loop through until the center of the string length exclusively
    for i in range(n_floors -1):
        # convert the individual string into an array of each element with a string character
        x = [e for e in asterisks]
        # replace the first that is not white space with white space
        x[i] = ' '
        # replace the last character that is not white space with white space
        x[n_floors*2 - (2 + i)] = " "
        # reassign the string asterisks as the current iteration array back into a string
        asterisks = "".join(x)
        # append that string to result
        result.append(asterisks)
    # reverse result 
    result = list(reversed(result))
    # return result
    return result

def tower_builder(n_floors):
    asterisks = '*'*(n_floors*2 -1)
    result = [asterisks]
    for i in range(n_floors -1):
        x = [e for e in asterisks]
        x[i] = ' '
        x[n_floors*2 - (2 + i)] = " "
        asterisks = "".join(x)
        result.append(asterisks)
    result = list(reversed(result))
    return result



print(tower_builder(1)) # ['*']
print(tower_builder(2)) # [' * ', '***']
print(tower_builder(3)) # ['  *  ', ' *** ', '*****']
print(tower_builder(6)) # ['     *     ', '    ***    ', '   *****   ', '  *******  ', ' ********* ', '***********']

# best practices and most clever
# The center() method will center align the string, using a specified character (space is default) as the fill character.
# using a for loop starting at 1 and ending at input + 1
# return an array with each element of "*" multiplied by the current index *2 -1 and center it with the string of length input*2 -1
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# if the input is 0 return an empty array
# loop through and append to an empty array append the current index spaces multiplied by white space concatenated to the current count of "*" and current index white spaces 
def tower_builder(n_floors):
    if n_floors == 0:
        return []
        
    count = 1
    result = []

    for i in range(1, n_floors + 1):
      stars = '*' * (2 * i - 1)
      space = ' ' * (n_floors - i)
      result.append(space + stars + space)
    
    return result

# for loop starting at 0 ending at input
# return an array for each element of the current index maths times white space concatenated by the current index maths "*" concatenated by again the current index maths times white space
def tower_builder(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]

# brute force for loop using a count reference instead of index reference
def tower_builder(n_floors):
    tower = []
    spacing = n_floors - 1
    stars = 1
    for i in range(0, n_floors):
        tower.append(' ' * spacing + '*' * stars + spacing * ' ')
        stars += 2
        spacing -= 1
    return tower

# Here ^ is the center align operator. EX '{:^3}'.format('*') evaluates to: ' * '
def tower_builder(n):
    length = n * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in range(1, length + 1, 2)]

# declaring the length of each string and using .center() to center the '*'
def tower_builder(n_floors):
    width = 2*n_floors - 1
    return [('*' * (2*i + 1)).center(width) for i in range(n_floors)]

# declaring an empty array and using array methods to append a series of concatenations
def tower_builder(n_floors):
    floors = []
    for i in range(n_floors):
        n_floors -= 1
        floors.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)

    return floors