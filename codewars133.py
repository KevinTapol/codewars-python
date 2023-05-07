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