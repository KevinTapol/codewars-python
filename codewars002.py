# Parameters or Edge Cases: inputs will be integers
# Return: "Even" for even integers or "Odd" for odd integers
# Examples:
# Psuedo Code: take input and divide by 2
#               if there is no remainder return even
#               else return false

# my answer
def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
        
print(even_or_odd(1)) # 'Odd'
print(even_or_odd(2)) # 'Even'
print(even_or_odd(-11)) # 'Odd'
print(even_or_odd(0)) # 'Even'

# best pracices and most clever
# this remdinds me of JavaScript ternary truthy/falsy except the statment to return comes before the condition of the return
# number % 2 will return 0 for even numbers and 1 for odd ones.
# 0 evaluates to False and 1 to True, so we can do it with one line
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'

# same as above but not using the truthy/falsy 
def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'

# simple lambda
# this reminds me of a JavaScript arrow function but the return comes before the condition
even_or_odd = lambda number: "Odd" if number % 2 else "Even"

# this reminds me of JavaScript index call of an array
# because of how modulus works the answer will always be either 0 or 1 NOT quotient ex 3 % 2 === 1 but 3/2 = 1.5
# if number % 2 results into no remainder meaning 0 then the index called will be at the 0 index which is "Even" 
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

# lambda with a tuple (immutable objects like JavaScript array) 
even_or_odd=lambda n:('Even','Odd')[n%2]

# lambda with a list (mutable objects like JavaScript array)
even_or_odd = lambda n: ["Even","Odd"][n % 2]

# using lambda with start stop step call through the string
# say it is even then take the index 0 and grab index(0 + 2) and repeat till there are no more indexes 
# same with odd but start at index 1
even_or_odd=lambda n:'EOvdedn'[n%2::2]

# dictionaries or objects in JavaScript key value pairs
def even_or_odd(number):
    even_or_odd = {0: "Even", 1: "Odd"}
    return even_or_odd[number % 2]

# example of a function calling a function
    # function takes single parameter
    def check_even_or_odd(number):
        # check if the number is an integer
        if type(number) != int:
            return 'Invalid input'
        return even_or_odd(number) # return the function to check for even or odd

    # function to check odd or even
    def even_or_odd(number):
        if number % 2 == 0:
            # if value of number is integer returns even
            return 'Even'
        # else it should return odd
        return 'Odd'

# if elif else Python if else if esle JavaScript
def even_or_odd(number):
    if number % 2 == 0:
        return"Even"
    elif number % 2 == 1:
        return"Odd"
    else:
        return"you are somewhat wrong"

# a good reminder that you can use only if instead of if elif else
def even_or_odd(c):
    if c / 2 == round(c / 2):
        return 'Even'
    if c / 2 != round(c / 2):
        return 'Odd'

# a bit of overkill but a great example of simple process for a simple solution with a refresher on array manipulation but for Python list/tuples, variable declarations, nested for loops and if statements, and functions calling functions
def even_or_odd(number):
    a = []
    a.append(0)
    a.append(2)
    a.append(4)
    a.append(6)
    a.append(8)
    b = str(number)
    c = list(b)
    d = True
    e = False
    for f in range(len(c)):
        if f == len(c) - 1:
            g = int(c[f])
            for h in range(len(a)):
                if str(a[h]) == str(g):
                    return bool_to_even_odd(not_bool_return(e))
    return bool_to_even_odd(not_bool_return(d))
                    
def not_bool_return(i):
    if not i:
        return True
    else:
        return False

def bool_to_even_odd(j):
    if j:
        return '{}{}{}{}'.format('E', 'v', 'e', 'n')
    else: 
        return '{}{}{}'.format('O', 'd', 'd')

