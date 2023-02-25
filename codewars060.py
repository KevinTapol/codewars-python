# Total Amount of Points
# Parameters:
    # input will be an array of 10 elements of strings integer:integer
    # the integers will be 0-4 inclusively 
    # the first integer we will represent as x and the second as y
# Return:
    # count the total points where x > y = 3 points, x < y = 0 points and x = y 1 point
# Examples:
        # ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'] => 30
        # ['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'] => 10
        # ['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'] => 0
        # ['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'] => 15
        # ['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'] => 12
# Psuedo Code:
    # declare an empty integer total
    # iterate through the array of elements splitting at : and compare each first element to the second element
    # if the first element is greater than the second add 3 to total
    # if the first element is equal to the second add 1 to the total
    # return total

# my answer
def points(games):
    # declare an empty integer total
    total = 0
    # iterate through the array of elements splitting at : and compare each first element to the second element
    for e in games:
        # if the first element is greater than the second add 3 to total
        if e[0] > e[2]:
            total += 3
        # if the first element is equal to the second add 1 to the total
        if e[0] == e[2]:
            total += 1

    return total

# my answer refactored implicit return lambda for each element in games 
points = lambda games: sum(3 if e[0] > e[2] else 1 if e [0] == e[2] else 0 for e in games)

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])) # 30
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'])) # 10
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'])) # 0
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'])) # 15
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'])) # 12

# best practices 
# very similar to my unrefactored answer but using .split() instead
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count

# most clever
# using .split()
def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

# interesting using index call given math evaluation
def points(games):
	return sum([0,1,3][1+(g[0]>g[2])-(g[0]<g[2])] for g in games)

# I like how they separated out the given parameters of 3 characters to x,_,y
points = lambda g: sum((x>y)*3 or x==y for x,_,y in g)

# similar to my refactored answer but using .split()
def points(games):
    return sum(3 if x > y else 0 if x < y else 1 for x, y in (score.split(":") for score in games))

# using a nested function to grab the first and last indexes
def points(games):
    def convert(game):
        x, y = int(game[0]), int(game[2])
        return 3 if x > y else 1 if x == y else 0
    return sum(convert(game) for game in games)

# using .match()
def points(games):
    count = 0
    for match in games:
        x = match.split(":")
        if x[0] > x[1]:
            count += 3
        elif x[0] == x[1]:
            count += 1
    return count

# using += on the index call for each element string eval
def points(games):
    points = 0
    for game in games:
        x, y = game.split(":")
        points += [0, 1, 3][(x >= y) + (x > y)]
    return points

# using map() with nested lambdas
def points(games):
    diff = map(lambda x: int(x[0]) - int(x[-1]), games)  # goal difference
    wins = map(lambda x: 3 if x > 0 else x, diff)  # change wins to 3 points
    return sum(list(map(lambda x: 1 if x == 0 else x * (x > 0), wins)))  # change draws and losses to 1 and 0 points