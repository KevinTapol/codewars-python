# Grasshopper - Messi goals function
# Parameters or Edge Cases:
    # inputs will be three integers equal to or greater than 0
# Return:
    # the sum of the inputs
# Examples:
    # (0, 0, 0) => 0
    # (5, 10, 2) => 17
# Pseudo Code:
    # add up the three inputs
    # return the sum

# my answer using + to add instead of sum() and *args because sum() can take only 2 arguments
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# my answer refactored *args or spread in JavaScript implicit return to add up all the inputs
# *args creates a tuple out of the arguments received by the function
# **kwargs creates a dictionary/object of arguments received by the function
goals = lambda *a: sum(a)

print(goals(0, 0, 0)) # 0
print(goals(5, 10, 2)) # 17

# best practices and most clever similar to my refactored
# using *args like spread in JavaScript to iterate through each input
def goals(*a):
    return sum(a)

# converting the inputs into a list then using sum() on the list
def goals(laLiga, copaDelRey, championsLeague):
    lList = [laLiga,copaDelRey,championsLeague]
    return sum(lList)

# creating an empty list then appending the inputs to the list and use sum() on the list
def goals(laLiga, copaDelRey, championsLeague):
    arr = []
    arr.append(laLiga)
    arr.append(copaDelRey)
    arr.append(championsLeague)
    return sum(arr)

# using for each element with *args
def goals(* args):
    return sum(x for x in args)

# using for elements in locals() get the values() and sum()
def goals(laLiga, copaDelRey, championsLeague):
    return sum([x for x in locals().values()])

# using .reduce()
import functools
def goals(laLiga, copaDelRey, championsLeague):
    return functools.reduce(lambda a, b: a + b, [laLiga, copaDelRey, championsLeague])

# using *args but only selecting values at index 0 1 and 2
def goals(*args):
    return sum(i for i in [args[0], args[1], args[2]])

# specifying to only add up ints
from typing import List

def goals(*goals: List[int]) -> int:
  return sum(goals)