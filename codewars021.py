"""
Century From Year
Parameters or Edge Cases:
    inputs will be 4 digit positive integers representing year
Return:
    what century the year is in
Examples:
    1705 --> 18
    1900 --> 19
    1601 --> 17
    2000 --> 20
Psuedo Code:
    divide by 100 and if there is a remainder then round up else return the whole integer
    I am using // so that I get an integer instead of a float.
"""

# my answer
def century(year):
    #  divide by 100 and if there is a remainder then round up else return the whole integer
    # I am using // so that I get an integer instead of a float.
    if year % 100 != 0:
        return (year // 100) + 1
    else:
        return year // 100
   
print(century(1705)) # 18
print(century(1900)) # 19
print(century(1601)) # 17
print(century(2000)) # 20
   
# my answer refactored lambda one liner if else
century = lambda year: (year // 100) + 1 if year % 100 != 0 else year // 100

# best practices and most clever
# very clever the reason this works if the number is 2000 and you add 99 you still have 2099 and the integer would be 20 but if it is greater like 2001 then you have 2100 and then get 21
def century(year):
    return (year + 99) // 100

# importing math to round up with math.ceil()
import math

def century(year):
    return math.ceil(year / 100)

# YOU CAN IMPORT IN THE RETURN STATEMENT?!
def century(year):
    return __import__('math').ceil(year/100)

# funny and clever using divmod() for quotient and remainder
def century(year):
    q, r = divmod(year, 100)
    return q + bool(r)

# converting to a string and using count()
def century(year):
    s = str(year)
    if s.count('00') == 1 :
        y = year // 100
        return y
    else:
        y = year // 100 + 1
        return y