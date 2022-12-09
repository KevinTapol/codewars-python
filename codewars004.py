# Parameters or Edge Cases: 
#       inputs will be integers and can be negative
# Return: 
#       a number as a string
# Examples: 
#       123  --> "123"
#       999  --> "999"
#       -100 --> "-100"
# Psuedo Code: 
#       return number as a string

# my answer and best practices
def number_to_string(num):
    return str(num)
print(number_to_string(123)) # "123"
print(number_to_string(999)) # "999"
print(number_to_string(-100)) # "-100"

# my answer refactored lambda
number_to_string = lambda num: str(num)

# most clever
number_to_string = str

# try except block
def number_to_string(num):
    try:
        return str(num)
    except:
        return None

# using {} and .format()
def number_to_string(num):
    return "{}".format(num)

# using while loop
def number_to_string(num):
  if num < 0: return "-" + number_to_string(-num)
  if num == 0: return "0"
  
  s = ''
  
  while num > 0:
      a = num % 10
      s = chr(ord('0') + a) + s
      num = num // 10
      
  return s

# descriptive comments of format()
def number_to_string(num):
    # Return a string of the number here!
    # return "%s" % num          # %-formatting
    # return str(num)            # int to string
    # return "{n}".format(n=num) # str.format()
    return f"{num}"              # f-strings

# using modulus
def number_to_string(num):
    return "%s" % num

# using ascii
def number_to_string(num):
    # Return a string of the number here!
    return ascii(num)

# using type()
def number_to_string(num):
    if type (num) == int: return str(num)
    return None