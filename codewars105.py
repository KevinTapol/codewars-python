# Create Phone Number
# Parameters or Edge Cases:
    # will be an array of 10 elements of integers
# Return:
    # the input as a string representation of a phone number "(xxx) xxx-xxxx"
# Examples:
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] => "(123) 456-7890"
# Pseudocode:
    # create a string named phone with the declared format "(xxx) xxx-xxxx"
    # convert the input of each element into a string and the array itself into a string and declare it as nums
    # iterate through the phone and replace each x with each element of nums using a for loop incrementing by 1
    # return the new string

# my answer
def create_phone_number(n):
    nums = "".join(str(e) for e in n)
    phone = "(xxx) xxx-xxxx"
    for i in range(len(nums)):
        phone = phone.replace("x", nums[i], 1)
    return phone

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"

# best practices and most clever using *args to iterate through the input and .format() for string interpolation
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# similar to my idea by converting the input array elements into a string and the array itself into a string. 
# Then declare a string with the format of a phone number and replace them with the strings.
# Here they are replacing by array lists starting at 0 ending at 2, start at 3 and end at 5 and start at 6 and end at the length
def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

# same as above but using .format() instead of %s
def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

# Same idea just using "".join(str(element) for element in array) instead of a for loop but finishing with string interpolation.
def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])

  return '({}) {}-{}'.format(str1, str2, str3)

# brute force concatenation
def create_phone_number(n):
    n = "".join([str(x) for x in n] )
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))

# wow using a tuple for efficiency of memory
# Same idea of string interpolation but replacing the input array elements by tuple()
# tuple is forcing the replace each element with string conversion.
def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)

# lol one liner implicit return but using 0-9 
create_phone_number = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

# using a for loop but with conditionals of where you are in the for loop
def create_phone_number(n):
  d='('
  #for loop to go through the array
  for i in range(len(n)):
  #get the first part of the final string
      if i<3:
          d=d+str(n[i])
          if i==2:
              d=d+') '
  #get the middle part of the final string
      elif i>=3 and i<6:
         
          d=d+str(n[i])
          if i==5:
              d=d+'-'
  #get the last 4 string members of the final string
      elif i>=6 and i<10:
   
          d=d+str(n[i])
  # return the entire string        
  return d

# using .format() with "".join()
def create_phone_number(n):
    n = list(map(str, n))
    return "({}) {}-{}".format("".join(n[:3]), "".join(n[3:6]), "".join(n[6:10]))  

# using reduce() and .replace()
from functools import reduce

def create_phone_number(n):
    return reduce( lambda a,c: a.replace('x',c, 1), list(map(str,n)), '(xxx) xxx-xxxx')