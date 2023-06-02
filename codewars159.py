# Twice as old
"""
Your function takes two arguments:
current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
"""
# Parameters or Edge Cases:
"""
inputs will be integers
"""
# Return:
"""
the age where the first input would be double the second input when scaled either backwards or forwards or 0
"""
# Examples:
"""
    (36,7) => 22
    (55,30) => 5
    (42,21) => 0
    (22,1) => 20
    (29,0) => 29
"""
# Pseudocode:
"""
    # subtract the 1st input by the product of the 2 times the 2nd input
    # return the absolute value of the difference
"""

# my answer
def twice_as_old(d,s):
    # subtract the 1st input by the product of the 2 times the 2nd input
    x = d - 2*s
    # return the absolute value of the difference
    return abs(x)

# my answer refactored implicit return
twice_as_old = lambda d,s: abs(d-2*s)


print(twice_as_old(36,7)) # 22
print(twice_as_old(55,30)) # 5
print(twice_as_old(42,21)) # 0
print(twice_as_old(22,1)) # 20
print(twice_as_old(29,0)) # 29

# best practices and most clever
# similar to my answers
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)

# conditionals with while loops for divisions
def twice_as_old(dad_years_old, son_years_old):
    count = 0
    if son_years_old == 0:
        return dad_years_old
    elif dad_years_old / son_years_old > 2:
        while son_years_old * 2 != dad_years_old:
            dad_years_old += 1
            son_years_old += 1
            count += 1
        return count
    elif dad_years_old / son_years_old < 2:
        while son_years_old != 0 and son_years_old * 2 != dad_years_old:
            dad_years_old -= 1
            son_years_old -= 1
            count += 1
        return count
    else:
        return 0