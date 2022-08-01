# Parameters or Edge Cases: inputs will be integers
# Return: "Even" for even integers or "Odd" for odd integers
# Examples:
# Psuedo Code: take input and divide by 2
#               if there is no remainder return even
#               else return false

# my answer 3rd in best practices
def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# best pracices and most clever
# number % 2 will return 0 for even numbers and 1 for odd ones.
# 0 evaluates to False and 1 to True, so we can do it with one line
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'

# 2nd best practice
def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'

# clost to most clever
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]