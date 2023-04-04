# Number of People in the Bus
# Parameters or Edge Cases:
    # inputs will be a 2D arrays of pairs of positive integers
    # the first integer for each pair represents the number of people getting on the bus
    # the second integer for each pair represents the number of people getting off the bus
# Return:
    # the number of people still on the bus after the last stop
# Examples:
    # [[10,0],[3,5],[5,8]] => 5
    # [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]] => 17
    # [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]] => 21
# Pseudocode:
    # declare a global variable integer and set it to 0
    # iterate through each array pair and add the first index to each pair to the declared variable
    # iterate through each array pair and subtract the second index to each pair from the declared variable
    # return the declared variable

# my answer
def number(bus_stops):
    total = 0
    for e in bus_stops:
        total += e[0]
        total -= e[1]
    return total

# my answer refactored implicit return
number = lambda b: sum([e[0] -e[1] for e in b])

print(number([[10,0],[3,5],[5,8]])) # 5
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])) # 17
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])) # 21

# best practices and most clever 
# same as my refactored implicit return but not implicit return
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

# instead of designating index[0] and index[1] they use i, o
def number(stops):
    return sum(i - o for i, o in stops)

# using sum(map()) instead of reduce()
def number(bus_stops):
    return sum(map(lambda x: x[0]-x[1],bus_stops))

# importing operator
import operator
def number(bus_stops):
    return operator.sub(*map(sum, zip(*bus_stops)))

# while loop going through the index 
def number(bus_stops):
    
    counter = 0
    max_index = len(bus_stops) - 1
    y = 0
    z = 0
    
    while counter <= max_index:
        x = bus_stops[counter]
        counter = counter + 1
        y = y + x[0]
        z = z + x[1]
    end = y - z
    return end