# Parameters or Edge Cases: 
#       inputs will be integers and can be negative
# Return: 
#       opposite value int or float 
# Examples: 
#       1: -1
#       14: -14
#       -34: 34
# Psuedo Code: 
#       take input float or int multiply by -1 return product

# my answer
def opposite(number):
    return number * (-1)
print(opposite(1)) # -1
print(opposite(0)) # 0
print(opposite(14)) # -14
print(opposite(-34)) # 34

# my answer refactored lambda
opposite = lambda number: number * (-1)

# best practices and most clever (the voted most clever was a series of +1-1 which was an obvious joke)
def opposite(number):
    return -number

# accounting for good point about -0
def opposite(number):
    return -1 * number # could have used -number, but that might send -0

# if else statement
def opposite(number):
  return abs(number) if number < 0 else 0 - number

# funny using negative case of .find() to multiply by the input
def opposite(number):
  # your solution here
  return number * "Magic Forest".find("unicorn")

# using .replace() to account for double negatives
def opposite(number):
  return float(('-' + str(number)).replace('--', ''))

# testing input type
def opposite(number):
    """
    Function have one required argument.
    At start our function check your number. If it's int, float or complex - func multiplies number by -1 and return it
    If our argument is string, try to convert to complex number
    If we had Value Error in our convertation, say(use print when except):
        Input data cannot be represented as a number.
    And after return None

    Return:
        Number int or float if input number is int or float.
        Number complex if input number is complex or wrote in string
        None if we had empty line or another input types
    """
    if (type(number) is int) or (type(number) is float) or (type(number) is complex):
        number = number * -1
        return number
    else:
        try:
            number = complex(number) * -1
            return number
        except ValueError:
            print("Input data cannot be represented as a number")
            return None

# specifics about solution return times
def opposite(number):
#fastest solution returned 94ms with parens around multiplication 87ms without for results
    return number - number * 2 

#middle solution returned 109ms time period for result
#    return number * -1
#slowest solution returned 150ms time period for result
#    return -number

# importing neg
from operator import neg as opposite

# using lambda imo most clever
opposite = lambda x: -x