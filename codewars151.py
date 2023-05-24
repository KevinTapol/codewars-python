# Make the Deadfish Swim
"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""
# Parameters or Edge Cases:
"""
    inputs will be a string of lowercase letters

"""
# Return:
"""
    an array of elements of the current value if current value is 'o' is in the string
"""
# Examples:
"""
    "iiisdoso" => [8, 64]
    "ooo" => [0,0,0]
    "ioioio" => [1,2,3]
    "idoiido" => [0,1]
    "isoisoiso" => [1,4,25]
    "codewars" => [0]

"""
# Psuedocode:
"""
    # declare a count variable and set it equal to 0
    # declare an empty array result
    # iterate through the input
    # if the current element is 'i' then add 1 to count
    # if the current element is 'd' then remove 1 from the count
    # if the current element is 's' then square the current count and reassign count equal to the result
    # if the current element is 'o' then push the current count to result
    # return result
"""
# my answer
def parse(data):
    # declare a count variable and set it equal to 0
    count = 0
    # declare an empty array result
    result = []
    # iterate through the input
    for e in data:
    # if the current element is 'i' then add 1 to count
        if e == 'i':
            count += 1
    # if the current element is 'd' then remove 1 from the count
        if e == 'd':
            count -= 1
    # if the current element is 's' then square the current count and reassign count equal to the result
        if e == 's':
            count = count**2
    # if the current element is 'o' then append the current count to result
        if e == 'o' and count != 0:
            result.append(count)
    # if the current element is 'o' and the count equals 0 then append 0 to result
        if e == 'o' and count == 0:
            result.append(0)
    # return result
    return result

# refactored removing unecessary count conditional
def parse(data):
    count = 0
    result = []
    for e in data:
        if e == 'i':
            count += 1
        if e == 'd':
            count -= 1
        if e == 's':
            count = count**2
        if e == 'o':
            result.append(count)
    return result

# practicing switch case
def parse(data):
    count = 0
    result = []
    for e in data:
        match e:
            case 'i':
                count += 1
            case'd':
                count -= 1
            case 's':
                count = count**2
            case 'o':
                result.append(count)
    return result

print(parse("iiisdoso")) # [8, 64]
print(parse("ooo")) # [0,0,0]
print(parse("ioioio")) # [1,2,3]
print(parse("idoiido")) # [0,1]
print(parse("isoisoiso")) # [1,4,25]
print(parse("codewars")) # [0]

# best practices 
# same as my conditional but using elif instead of if
def parse(data):
    value = 0
    res=[]
    for c in data:
        if c=="i": value+=1
        elif c=="d": value-=1
        elif c=="s": value*=value
        elif c=="o": res.append(value)
    return res

# most clever
# created a dictionary with the current element as key and the implicit return lambda functions as the value
def parse(data):
    action = {'i': lambda v, r: v + 1,
              'd': lambda v, r: v - 1,
              's': lambda v, r: v * v,
              'o': lambda v, r: r.append(v) or v}
    v, r = 0, []
    for a in data:
        v = action[a](v, r) if a in action else v
    return r

# nice! user built an entire class using a dictionary
# the codewars function creates a new object, 
# initiates an empty array and 0 integer, 
# creates an array with a for loop calling the current element based on the dictionary function value, 
# and returns the array of the object initially initiated.
class Deadfish:
    commands = {
        'i': lambda df: df.i(),
        'd': lambda df: df.d(),
        's': lambda df: df.s(),
        'o': lambda df: df.o()
    }

    def __init__(self):
        self.value = 0
        self.outputs = []

    def i(self): self.value += 1
    def d(self): self.value -= 1
    def s(self): self.value **= 2
    def o(self): self.outputs.append(self.value)

    def apply(self, command):
        try: Deadfish.commands[command](self)
        except KeyError: pass

def parse(commands):
    df = Deadfish()
    [df.apply(c) for c in commands]
    return df.outputs

# here they excluded '0' from the object and implemented it in the function logic
COMMANDS = {
    'i': lambda x: x + 1,
    'd': lambda x: x - 1,
    's': lambda x: x * x,
}

def parse(data):
    result, x = [], 0
    for c in data:
        if c == 'o':
            result.append(x)
        elif c in COMMANDS:
            x = COMMANDS[c](x)
    return result

# they created the object internally with the for loop
def parse(data):
    v, r = 0, []
    for c in data:
        v, r = v + {'i': 1, 'd': -1, 's': v * (v - 1)}.get(c, 0), r + [v] * (c == 'o')
    return r