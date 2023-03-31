# Growth of a Population
# Parameters or Edge Cases:
    # inputs will be numbers integers and decimals
    # inputs will not be empty or null
# Return:
    # given a current population with a 2% yearly growth and 50 new inhabitants each year, return the total number of years needed to reach the final input representing a desired population
# Examples:
    # At the end of the first year there will be: 
    # 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
    # 
    # At the end of the 2nd year there will be: 
    # 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)
    # 
    # At the end of the 3rd year there will be:
    # 1141 + 1141 * 0.02 + 50 => 1213
    # 
    # It will need 3 entire years.

    # (1500, 5, 100, 5000) => 15
    # (1500000, 2.5, 10000, 2000000) => 10
    # (1500000, 0.25, 1000, 2000000) => 94
# Pseudo Code:
    # declare an integer called years
    # while the 1st input is less than the 4th input
        # set the 1st input equal to the 2nd input divide by 100 then add 1
        # multiply that result by the 1st input and add that integer value to the 3rd input
        # add 1 to years at the end of the while loop
    # outside of the while loop return years

# my answer
def nb_year(current_pop, percent_pop_per_year, new_inhabitants, goal_pop):
    years = 0
    while current_pop < goal_pop:
        current_pop = int(current_pop*(1 + percent_pop_per_year/100)) + new_inhabitants
        years += 1
    return years
    
print(nb_year(1500, 5, 100, 5000)) # 15
print(nb_year(1500000, 2.5, 10000, 2000000)) # 10
print(nb_year(1500000, 0.25, 1000, 2000000)) # 94

# EVERY ANSWER WAS EITHER RECURSION CONDITIONALS OR A WHILE LOOP!!!!

# best practices and most clever recursion
# declare another variable and give it a value of 0
# recursion of calling the function and adding 1 to the declared variable
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

# importing accumulate() This iterator takes two arguments, iterable target and the function which would be followed at each iteration of value in target
from itertools import accumulate

def nb_year(p0, pct, aug, p):
  return next(i for i, x in enumerate(accumulate([p0] * 1000, lambda px, _: px + .01 * pct * px + aug)) if x >= p)

# import math and using .floor() instead of int()
import math
def nb_year(p0, percent, aug, p):
    pop = p0
    i = 0
    while True:
        i += 1
        pop = math.floor(pop * (1 + percent/100)) + aug
        if pop >= p:
            return i

# putting the recursion outside the if conditional
def nb_year(p_s, f, aug, p_e):
    
    p_new = int(p_s + p_s * (f / 100) + aug)

    if p_new >= p_e:
        return 1

    return 1 + nb_year(p_new, f, aug, p_e)