"""
Is he gonna survive?
Parameters or Edge Cases:
    first integer input represents number of bullets
    second integer input represents number of dragons
    2 bullets are required to defeat a dragon
Return:
    boolean true if there are enough bullets to defeat the dragons else false
Examples:
    (hero(10, 5), True)
    (hero(7, 4), False)
    (hero(4, 5), False)
    (hero(100, 40), True)
    (hero(1500, 751), False)
    (hero(0, 1), False)
Psuedo Code:
    if the second input dragons * 2 is greater than the first input bullets return false else true
"""
# my answer
def hero(bullets, dragons):
    # if the second input dragons * 2 is greater than the first input bullets return false else true
    if dragons * 2 > bullets:
        return False
    else:
        return True

# my answer refactored
hero = lambda b, d: False if d * 2 > b else True

print(hero(10, 5)) # True
print(hero(7, 4)) # False
print(hero(4, 5)) # False
print(hero(100, 40)) # True
print(hero(1500, 751)) # False
print(hero(0, 1)) # False

# best practices and most clever
# implicit return for boolean values based on math statement 
def hero(bullets, dragons):
    return bullets >= dragons * 2

# one line lambda of best practices and most clever
hero = lambda b,d: 2*d<=b

# here they are dividing the bullets by the dragons to make sure you have at least 2 bullets per dragon
# if dragon is zero then you would be dividing by zero which you can't so return true
def hero(bullets, dragons):
    try:
        return bullets / dragons >= 2
    except ZeroDivisionError:
        return True

# funny .find() finds the first instance of l which is in index 2 and multiply the index by the number of dragons
def hero(bullets, dragons):
    return bullets >= dragons * "Hello world!".find('l')

# interesting chaining and statements for boolean returns
def hero(bullets, dragons):
    return (bullets % dragons == 0 or  (bullets > dragons*2)) and (bullets > dragons) 