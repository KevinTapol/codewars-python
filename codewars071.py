# Double Char
# Parameters or Edge Cases:
    # inputs will be strings
    # can be upper or lower case
    # can be empty or null?
# Return:
    # the input string repeated next to each element
# Examples:
    # "String"      -> "SSttrriinngg"
    # "Hello World" -> "HHeelllloo  WWoorrlldd"
    # "1234!_ "     -> "11223344!!__  "
# Pseudo Code:
    # iterate through the input string copy and concat each element
    # return the new string

# my answer
def double_char(s):
    new_str = ""
    for i in s:
        new_str += (i*2)
    return new_str

# my answer implicit return one line for element in string in "".join
double_char = lambda s: "".join(i*2 for i in s)

print(double_char("String")) # "SSttrriinngg"
print(double_char("Hello World")) # "HHeelllloo  WWoorrlldd"
print(double_char("1234!_ ")) # "11223344!!__  "


# best practices and most clever
# same as my implicit return
def double_char(s):
    return ''.join(c * 2 for c in s)

# nesting lambda in map()
def double_char(s):
    return ''.join(map(lambda e:e*2,s))

# using [] for array for elements in list/array and i+i to concat
def double_char(_s):
    return ''.join([i+i for i in _s])

# string interpolation .format
# interesting how output is being declared outside of the function
OUTPUT = '{0}{0}'.format
def double_char(s):
    return ''.join(OUTPUT(a) for a in s)

# nested lambda inside a map()
# here they are intentionally creating | character in-between each
def double_char(s: str) -> str:
    return "".join(list(map(lambda _: _ * 2, "|".join(s).split("|"))))

# using for x in range length of input string
def double_char(s):
    new_string = ''
    for x in range(len(s)):
        new_string += s[x]*2
    return new_string

# using array methods append
def double_char(s):
    result = 0
    y = []
    for i in s:
        result = i * 2
        y.append(result)
    return ''.join(y)