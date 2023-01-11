"""
Will you make it?
Parameters or Edge Cases:
    inputs will be integers greater than 0
Return:
    boolean True or False if you can make it to the first input or given distance with the second input rate of travel multiplied by the third input of remaining fuel
Examples:
        (zero_fuel(50, 25, 2), True)
        (zero_fuel(100, 50, 1), False)
Psuedo Code:
    if the distance is less than or equal to the product of rate of travel and fuel remaining then return false else true
    I am going to use the math statement distance <= rate * fuel to implicitly return True/False
"""
# my answer and best practices
def zero_fuel(distance_to_pump, mpg, fuel_left):
    # I am going to use the math statement distance <= rate * fuel to implicitly return True/False
    return distance_to_pump <= mpg * fuel_left

# my answer refactored lambda one liner
zero_fuel = lambda d, r, f: d <= r * f

print(zero_fuel(50, 25, 2)) # True
print(zero_fuel(100, 50, 1)) # False

# most clever
# "".join(str({':(': 4, ':/': 7, ':D': 1, '=/': 6, ':P': 2, '=)': 5, ';)': 9, ':)': 0, ':{': 8, ':S': 3}[i]) for i in x.split()) bit sets up a dictionary where ":(" == 4 and so on. The map(chr,[int(...)) takes the resulting array of numbers after the translation and turns them into an array of ascii chars. The rest exec("".join(...)) just joins up the array into a string and evaluates it.
exec("".join(map(chr,[int("".join(str({':(': 4, ':/': 7, ':D': 1, '=/': 6, ':P': 2, '=)': 5, ';)': 9, ':)': 0, ':{': 8, ':S': 3}[i]) for i in x.split())) for x in 
""":D :) :)  :D :) :D  :D :) :P  :S :P  :D :P :P  :D :) :D  :D :D :(  :D :D :D  :/ :)  :D :D
:/  :D :) :D  :D :) :{  :( :)  :D :) :)  :D :) =)  :D :D =)  :D :D =/  ;) :/  :D :D :)  ;) ;)  
:D :) :D  ;) =)  :D :D =/  :D :D :D  ;) =)  :D :D :P  :D :D :/  :D :) ;)  :D :D :P  :( :(  :S 
:P  :D :) ;)  :D :D :P  :D :) :S  :( :(  :S :P  :D :) :P  :D :D :/  :D :) :D  :D :) :{  ;) =)  
:D :) :{  :D :) :D  :D :) :P  :D :D =/  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :P  :D :D 
:(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  :D :) :)  :D :) =)  :D :D =)  :D 
:D =/  ;) :/  :D :D :)  ;) ;)  :D :) :D  ;) =)  :D :D =/  :D :D :D  ;) =)  :D :D :P  :D :D :/  
:D :) ;)  :D :D :P  :S :P  =/ :)  =/ :D  :S :P  :D :) ;)  :D :D :P  :D :) :S  :S :P  :( :P  :S 
:P  :D :) :P  :D :D :/  :D :) :D  :D :) :{  ;) =)  :D :) :{  :D :) :D  :D :) :P  :D :D =/  :D :)"""
.split("  ")])))

# most are variations of the solution if else boolean return
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    else: 
        return True

# my answer If I were to one line lambda the common solution
zero_fuel = lambda d, r, f: False if d > r * f else True

# using 1 and 0 return for True and False
def zero_fuel(d, m, f):
    return 1 if d / m <= f else 0