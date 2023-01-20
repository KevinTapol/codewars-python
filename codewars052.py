# Transportation on vacation
# Parameters or Edge Cases:
    # input will be an integer greater than 0
    # Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total. NOTE!!! when you get to 7 or more days it is not both $20 and $50!!! 7 or more gets you an additional $30 discount on top of the $20
# Return:
    # an integer representing the total cost for renting a car for given in put number of days
# Examples:
    # rental_car_cost(1) # 40
    # rental_car_cost(4) # 140
    # rental_car_cost(7) # 230
    # rental_car_cost(8) # 270
# Psuedo Code:
    # if the input is less than 3 days return the given input * 40
    # if the input is greater than or equal to 3 days AND less than 7 return (input * 40) - 20
    # if the input is greater than or equal to 7 return (input * 40) - 70

# my answer
def rental_car_cost(d):
    # if the input is less than 3 days return the given input * 40
    if d < 3:
        return d*40
    # if the input is greater than or equal to 3 days AND less than 7 return (input * 40) - 20
    elif 3 <= d < 7:
        return d*40 - 20
    # if the input is greater than or equal to 7 return (input * 40) - 70
    else:
        return d*40 -50

# my answer refactored lambda implicit return one liner of nested conditions similar to JavaScript arrow function nested ternaries ? : (? :)
# rental_car_cost = lambda d: result if condition else result if condition else result
rental_car_cost = lambda d: d*40 if d < 3 else d*40 - 20 if 3 <= d < 7 else d*40 -50

print(rental_car_cost(1)) # 40
print(rental_car_cost(4)) # 140
print(rental_car_cost(7)) # 230
print(rental_car_cost(8)) # 270

# best practices
def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result

# most clever
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30

# using else if instead of elif
def rental_car_cost(d):
    return d*40 - 50 if d >= 7 else d*40 -20 if d >= 3 else d*40  

# wow incredibly clever nested truthy falsy calls
# if d < 3 then [d < 3] evaluates to true or 1 and index call of ((50, 20)[d < 7], 0) of 1 is 0 returning 40*d - 0
# if d > 3 then [d < 3] evaluates to false or 0 which calls d < 7 
    # if d < 7 then [d < 7] evaluates to true or 1 and index calls (50, 20) as 20 returning 40*d - 20
    # if d > 7 then [d < 7] evaluates to false or 0 and index calls (50, 20) as 50 returning 40*d - 50
def rental_car_cost(d):
    return 40 * d - ((50, 20)[d < 7], 0)[d < 3]

# same idea of index call but the index call statement evaluates to adding true false statement evaluations of 0 and 1
rental_car_cost = lambda d: 40*d-[0,20,50][(d>=3)+(d>=7)]

