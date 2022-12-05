# Parameters or Edge Cases: input is a number can be negative or 0
# Return: return a negative number
# Examples: make_negative(1);  # return -1
#           make_negative(-5); # return -5
#           make_negative(0);  # return 0
# Psuedo Code: if number is 0 return 0
#              else multiply by -1 return product

# my answer
def make_negative( number ):
    if number <= 0:
        return number
    else:
        return number*(-1)

print(make_negative(1)) # -1
print(make_negative(-5)) # -5
print(make_negative(0)) # 0

# cleaner version of my answer
def make_negative( number ):
    return -number if number>0 else number

# best practices and most clever
def make_negative( number ):
# return negative of number. BUT: negative in = negative out. zero remains zero
    return -abs(number)

# just like js, you can add a - infront of the number
def make_negative( number ):
    return -number if number>0 else number

# taking input number and subtract from 0 interseting way to get the opp
def make_negative(number):
    if number >= 0:
        return (0 - number)
    else:
        return number

# identifying the string '-' in number and adding if not there returns strings then use int() to convert back to integer
def make_negative( number ):
    if "-" in str(number):
        return(number)
    else:
        return int("-" + str(number))

# importing Mathematics
import math as Mathematics
def make_negative( number ):
    if int(number) != 0:
        number_but_better = Mathematics.factorial(abs(number)) * 0
        number2 = number_but_better + number
        number3 = abs(number2)
        number4 = number2 * 0.1 * -1 * 10
        return -abs(number)
    else: return 0

# using .startswith()
def make_negative( number ):
    if str(number).startswith("-"):
        return number
    elif str(number).startswith("0"):
        return number
    else:
        return int("-" + str(number))

# lambda similar to arrow function in js
make_negative = lambda x: x * -1 if x >= 0 else x