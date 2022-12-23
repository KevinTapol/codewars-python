"""
Beginner - Lost Without a Map
Parameters or Edge Cases:
    input will be an array if integers
Return:
    return the array wich each integer doubled in value
Examples:
    (maps([1, 2, 3]), [2, 4, 6])
    (maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    (maps([]), [])
Psuedo Code:
    take in the array and loop through each element multiplying by 2
    return the new array
"""

# my answer brute force loop
def maps(a):
    arr = []
    for i in range(len(a)): # same thing as - for i in a:
        arr.append(a[i] * 2)
    return arr

# my refactored answer using map(function, iterable, [iterable1, iterable2, ...])
# something to note that you must use list() for python3 outside of map()
def maps(a):
    return list(map(lambda x:x*2, a))

print(maps([1, 2, 3])) # [2, 4, 6]
print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(maps([])) # []

# best practices and most clever
# for loop in one line
def maps(a):
    return [2 * x for x in a]

# nested lambdas this is a one liner of my refactored answer
maps=lambda a:list(map(lambda x:x*2,a))

# one liner lambda of best practices and most clever
maps = lambda a: [2*n for n in a]

# 2nd best practices and most clever but only works with python2 NOT python3 
def maps(a):
    return map(lambda x:2*x, a)
# I adjusted this to work in python3 by converting to a list
def maps(a):
    return list(map(lambda x:2*x, a))

# reseting the orignial input values to be double and returning the input
# it's bad practice to mutate the original instead of creating a copy
def maps(a):
	if len(a) > 0:
		for i in range(len(a)):
			a[i] = a[i] * 2
	return a

# using .__mul__ 
def maps(a):
    return list(map((2).__mul__, a))

# several answers followed this model of creating another function then calling it inside the map() as the first argument
def maps(a):
    results = map(double, a)
    return list(results)
def double(a):
    return a*2
