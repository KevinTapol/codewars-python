# Quarter of the year
# Parameters or Edge Cases:
    # input will be an integer from 1 to 12 representing months January to December
# Return:
    # an integer representation of what quarter of the year that month is in
# Examples:
    # quarter_of(3) # 1
    # quarter_of(8) # 3
    # quarter_of(11) # 4
# Psuedo Code:
    # if the input integer is 1-3 return 1
    # if the input integer is 4-6 return 2
    # if the input integer is 7-9 return 3
    # if the input integer is 10-12 return 4

# my answer and best practices
def quarter_of(month):
    # if the input integer is 1-3 return 1
    if 1 <= month < 4:
        return 1
    # if the input integer is 4-6 return 2
    elif 4 <= month < 7:
        return 2
    # if the input integer is 7-9 return 3
    elif 7 <= month < 10:
        return 3
    # if the input integer is 10-12 return 4
    else:
        return 4
    
# my answer refactored implicit return one line lambda with 4 conditionals
quarter_of = lambda m: 1 if 1 <= m < 4 else 2 if 4 <= m < 7 else 3 if 7 <= m < 10 else 4

print(quarter_of(3)) # 1
print(quarter_of(6)) # 2
print(quarter_of(8)) # 3
print(quarter_of(11)) # 4

# most clever
# wow very clever adding the input to 2 so that when you divide by 3 
# you will have either a whole integer greater than 1 or a float greater than 1.0 
# using // divides and only takes the integer and not the remaining float 
def quarter_of(n):
    return (n + 2) // 3

# dividing by 3 so that there are 4 quarters then using ceil() to round up to the nearest whole number which would be 1, 2, 3, or 4 depending upon the input
from math import ceil
def quarter_of(month):
    return ceil(month / 3)

# subtracting by 1 and dividing by 3 which if 1-3 will not return an integer meaning it will be 0 then add 1 resulting in quarter 1
# if 4-7 // 3 will return values 1 to and not including 2 then add 1 resulting in quarter 2 
def quarter_of(month):
    return (month-1) // 3 + 1 

# making a dictionary/object key value pair where the value is an array/list of possible inputs and the key is the quarter
# then looping through and checking to see if the input exists in each value array/list and return the respect key
def quarter_of(month):
    year ={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}   
    for k, v in year.items():
        if month in v:
            return k
        
# same idea as dictionary/object except here they are using individual integers with the same key for values of their respective subsets
def quarter_of(month):
    season = {1: 1, 2: 1, 3: 1, 
              4: 2, 5: 2, 6: 2,
              7: 3, 8: 3, 9: 3,
              10: 4, 11: 4, 12: 4}
    return season[month]

# using .get() for dictionary/object method call with user input
def quarter_of(month):
    q_dict = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4}
    return q_dict.get(month)

# using if statements to see if the input is in an array/list
def quarter_of(month):
    if month in (1,2,3):
        return 1
    elif month in (4,5,6):
        return 2
    elif month in (7,8,9):
        return 3
    elif month in (10,11,12):
        return 4
    
# using nested for loops to check for values in a tuple (an immutable array)
# since tuples are stored in 1 memory block they are faster
def quarter_of(month):
    
    seasons = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    for x in seasons:
        for m in x:
            if m == month:
                return seasons.index(x) + 1
            
# while loop
def quarter_of(month):
    while True:
        
        if month <= 3:
            return 1
            
            
        elif month <= 6:
            return 2
            
            
        elif month <= 9:
            return 3
            
            
        elif month <= 12:
            return 4