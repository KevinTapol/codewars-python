# Thinkful - Logic Drills: Traffic light
# Parameters or Edge Cases:
    # inputs will be strings either 'green' 'yellow' or 'red'
# Return:
    # the progression of a stop light green => yellow => red => green
# Example:
    # 'green' => 'yellow'
    # 'yellow' => 'red'
    # 'red' => 'green'
# Pseudo Code:
    # if the input is 'green' return 'yellow'
    # if the input is 'yellow' return 'red'
    # if the input is 'red' return 'green'


# my answer
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    else:
        return 'green'

# my answer refactored implicit return nested conditionals
update_light = lambda c: 'yellow' if c == 'green' else 'red' if c == 'yellow' else 'green'
     
print(update_light('green')) # 'yellow'
print(update_light('yellow')) # 'red'
print(update_light('red')) # 'green'

# best practices and most clever
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

# tuple immutable using index + 1 to call next color in series
def update_light(current):
    color = ['green', 'yellow', 'red']
    return color[(color.index(current)+1)%len(color)]

# implicit return dictionary with .get
update_light = {"green":"yellow", "yellow":"red", "red":"green"}.get

# .get() with input
def update_light(current):
  return {"green": "yellow", "yellow": "red", "red": "green"}.get(current)

# index call of input for key value pair
def update_light(current):
    light_order = {'red':'green', 'yellow':'red', 'green':'yellow'}
    
    return light_order[current]

# declaring another variable for the array so that we can one line implicit return
update_light = lambda c,l=["yellow","green","red"]: l[l.index(c)-1]

# match case
def update_light(current):
    match current:
        case 'red': return 'green'
        case 'yellow': return 'red'
        case 'green': return 'yellow'

# while importing for cycle() method
from itertools import cycle

def update_light(current):
    lights = cycle(["green", "yellow", "red"])
    while True:
        if next(lights) == current:
            return next(lights)