# Parameters or Edge Cases: inputs will be integers and can be negative
# Return: a number as a string
# Examples: 123  --> "123"
#           999  --> "999"
#           -100 --> "-100"
# Psuedo Code: return number as a string

# my answer and best practices
def number_to_string(num):
    return str(num)
print(number_to_string(123)) # "123"
print(number_to_string(999)) # "999"
print(number_to_string(-100)) # "-100"

# most clever
number_to_string = str