"""
Calculate BMI
Parameters or Edge Cases:
    inputs will be numbers and can be floats or integers
    inputs will never be null, empty or negative
Return:
    a string "Underweight", "Normal", "Overweight" or "Obese" based on bmi formula of given inputs
Examples:
    bmi = weight / height2
    if bmi <= 18.5 return "Underweight"
    if bmi <= 25.0 return "Normal"
    if bmi <= 30.0 return "Overweight"
    if bmi > 30 return "Obese"

    (bmi(50, 1.80), "Underweight")
    (bmi(80, 1.80), "Normal")
    (bmi(90, 1.80), "Overweight")
    (bmi(110, 1.80), "Obese")
    (bmi(50, 1.50), "Normal")
Psuedo Code:
    take in the inputs and divide the weight by the product of the height multiplied by itself
    if the qotient is <= 18.5 return "Underweight"
    if the qotient is <= 25.0 return "Normal"
    if the qotient is <= 30.0 return "Overweight"
    else return "Obese"
"""
# my answer and best practices
def bmi(weight, height):
    # take in the inputs and divide the weight by the product of the height multiplied by itself
    quotient = weight / (height * height)
    # if the qotient is <= 18.5 return "Underweight"
    if quotient <= 18.5:
        return "Underweight"
    # if the qotient is <= 25.0 return "Normal"
    elif quotient <= 25.0:
        return "Normal"
    # if the qotient is <= 30.0 return "Overweight"
    elif quotient <= 30.0:
        return "Overweight"
    # else return "Obese"
    else:
        return "Obese"

# my answer refactored
def bmi(w, h):
    t = w / h**2
    return "Underweight" if t <= 18.5 else "Normal" if t <= 25.0 else "Overweight" if t <= 30.0 else "Obese"

# my answer further refactored into lambda one liner with a () to call the function because of the nested lambda
bmi = lambda w, h: (lambda t = w / h**2: "Underweight" if t <= 18.5 else "Normal" if t <= 25.0 else "Overweight" if t <= 30.0 else "Obese")()

print(bmi(50, 1.80)) # "Underweight"
print(bmi(80, 1.80)) # "Normal"
print(bmi(90, 1.80)) # "Overweight"
print(bmi(110, 1.80)) # "Obese"
print(bmi(50, 1.50)) # "Normal"

# most clever
# wow very clever evalutating the boolean to interger 1 or 0 True or False and adding them to call the index
# for example if all the math results to 18.4 then the list evaluates to only False adding up to 0 and calling [0] in the list index returning 'Underweight'
# if 1 true then 'Normal" 2 trues 'Overweight' all true then 'Obese'
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

# putting return on the same line as the conditionals met
def bmi(weight, height):
    bmeye = (weight/(height**2))
    if bmeye <= 18.5: return("Underweight")
    elif bmeye <= 25.0: return("Normal")
    elif bmeye <= 30.0: return("Overweight")
    elif bmeye > 30: return("Obese")

# someone one line lambda the most clever answer
bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])()

# nesting if conditionals
def bmi(weight, height):
    ratio = weight / height ** 2
    
    if ratio > 18.5:
        if ratio > 25:
            if ratio > 30:
                return 'Obese'
            return 'Overweight'
        return 'Normal'
    return 'Underweight'

# next() function returns the next item in an iterator
# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc
# .split() method splits a string into a list.
bmi=lambda w,h:next(s for s,t in zip("Obese Overweight Normal Underweight".split(),(30,25,18.5,0))if w/h/h>t)
# User explanation
# First you need to understand what generators are.

# str.split creates a list of strings
# 'a b c'.split() == ['a', 'b', 'c']

# zip joins several lists together by taking elements at same index.
# list(zip([1, 2, 3], ['a', 'b', 'c'])) == [(1, 'a'), (2, 'b'), (3, 'c')]

# Finally next is used to iterate on this list of pairs - it stops at first pair matching the condition if w / h / h > t.

# Basically this expression is equivalent to four ifs in a row with different values for s and t.

# if w / h / h > t:
    # return s

# dictionary for loop using math in the for loop as the key call for the dictionary
# They are iterating through the key and if the condition is met at that key return the value.
def bmi(weight, height):
    _bmi = weight / height ** 2

    conditions = {
        18.5 : 'Underweight',
        25.0 : 'Normal',
        30.0 : 'Overweight',
        None : 'Obese'}
    for point in conditions:
        if point is None or _bmi <= point: return conditions[point]

# creating a dictionary and calling a boolean True for when the object key is true given the conditions met for math of inputs
def bmi(weight, height):
    mass = weight//height**2
    weights={mass<=19: 'Underweight', 18<mass<=25: 'Normal',
            25<mass<=30:'Overweight',mass>30:'Obese'}
    return weights[True]