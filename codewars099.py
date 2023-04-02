# Categorize New Member
# Parameters or Edge Cases:
    # inputs will be a 2D array where each element is an array
    # first input of each pair will represent age and the 2nd handicap from -2 to 26
    # can the arrays be empty?
# Return:
    # "Senior" if the pair first index is equal to or greater than 55 and the handicap is is greater than 7 else "Open" FOR EACH PAIR IN THE ARRAY! 
# Examples:
    # [(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)] => ["Open", "Open", "Senior", "Open", "Open", "Senior"]
    # [(45, 12),(55,21),(19, -2),(104, 20)] => ['Open', 'Senior', 'Open', 'Senior']
    # [(16, 23),(73,1),(56, 20),(1, -1)] => ['Open', 'Open', 'Senior', 'Open']
# Pseudo Code:
    # declare an empty array
    # iterate through the array and for each index check if the first element in each index is equal to or greater than 55 and the 2nd element is greater than 7
    # if both conditions meet, append the string "Senior" to the empty array else "Open"
    # return the new string

# my answer and second best practices
def open_or_senior(data):
    x = []
    for e in data:
        if e[0] >= 55 and e[1] > 7:
            x.append("Senior")
        else:
            x.append("Open")
    return x

# my answer refactored implicit return
# imo cleaner version of best practices and most clever but using index locations with implicit return
open_or_senior = lambda d: ["Senior" if e[0] >= 55 and e[1] > 7 else "Open" for e in d]


print(open_or_senior([(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)])) # ["Open", "Open", "Senior", "Open", "Open", "Senior"]
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])) # ['Open', 'Senior', 'Open', 'Senior']
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])) # ['Open', 'Open', 'Senior', 'Open']

# best practices and most clever very similar to my refactored answer
def open_or_senior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# outdated... you must wrap the map() with list() ex list(map())
def open_or_senior(data):
    return map(lambda d: 'Senior' if d[0] >= 55 and d[1] > 7 else 'Open', data)

# encapsulating map() with list() to return list(map())
def open_or_senior(data):
    return list(map(lambda x: "Senior" if x[0] >= 55 and x[1] > 7 else "Open", data))


# using += instead of .append()
def open_or_senior(data):
    categories = []
    for i in data:
        a,h = i
        if a > 54:
            if h > 7: categories += ["Senior"]
            else: categories += ["Open"]
        else: categories += ["Open"]
    return categories

# Boolean expression maps to int which is used as an index to select either value from the list for each tuple in data.
def open_or_senior(data):
    return [['Open', 'Senior'][age >= 55 and handicap > 7] for age, handicap in data]

# instead of using else return "Open" outside of the if
def open_or_senior(data):
    def categorize(age, handicap):
        if age >= 55 and handicap > 7:
            return 'Senior'
        return 'Open'

    return [ categorize(*item) for item in data ]