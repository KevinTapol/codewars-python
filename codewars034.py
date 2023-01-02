"""
Are You Playing Banjo?
Parameters or Edge Cases:
    inputs will be strings of letters
Return:
    if the input string starts with "R" or 'r' return "input plays banjo" else "input does not play banjo"
Examples:
    (are_you_playing_banjo("martin"), "martin does not play banjo");
    (are_you_playing_banjo("Rikke"), "Rikke plays banjo");
    (are_you_playing_banjo("bravo"), "bravo does not play banjo")
    (are_you_playing_banjo("rolf"), "rolf plays banjo")
Psuedo Code:
    take in the input name and if the first character is either "R" or "r" return "input plays the banjo"
    else return "input does not play banjo"

"""
# my answer
def are_you_playing_banjo(name):
    # take in the input name and if the first character is either "R" or "r" return "input plays the banjo"
    if name[0] == "r" or name[0] == "R":
        return f'{name} plays banjo'
    # else return "input does not play banjo"
    else:
        return f'{name} does not play banjo'

print(are_you_playing_banjo("martin")) # "martin does not play banjo"
print(are_you_playing_banjo("Rikke")) # "Rikke plays banjo"
print(are_you_playing_banjo("bravo")) # "bravo does not play banjo"
print(are_you_playing_banjo("rolf")) # "rolf plays banjo"

# my answer refactored lambda
are_you_playing_banjo = lambda name: f'{name} plays banjo' if name[0] == "r" or name[0] == "R" else f'{name} does not play banjo'

# best practices
# I don't know why I didn't think to force the input to either upper or lower then compare 
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

# most clever
# I've never seen a semicolon used at the end of a statement in Python like JavaScript
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

# using .startswith() method instead of calling the first index of the input string
def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

# using .format() method to insert input in the placeholder {}
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return "{} plays banjo".format(name)
    return "{} does not play banjo".format(name)

# using %s as an input place holder for %name
def areYouPlayingBanjo(name):
    if name[0] == 'r' or name[0] =='R':
        return ("%s plays banjo"%name)
    else:
        return ("%s does not play banjo"%name)

# using index call based on conditional reminds me of JavaScript truthy falsy
# lambda and concatenation
areYouPlayingBanjo = lambda n: n+[" does not play banjo"," plays banjo"][n[0].lower()=='r']

# same idea as above but checking if first letter is in the string "Rr"
def areYouPlayingBanjo(name):
    return f"{name} {['does not play', 'plays'][name[0] in 'Rr']} banjo"