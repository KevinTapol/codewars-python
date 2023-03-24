# Credit Card Mask
# Parameters or Edge Cases
    # inputs will be a string of integers
    # the strings can be empty
# Return:
    # the entire string replacing all the numbers with "#" except the last 4
# Examples:
    # "4556364607935616" --> "############5616"
    #  "64607935616" -->      "#######5616"
    #    "1" -->                "1"
    # "" -->                 ""
# Pseudo Code:
    # reverse the string and grab the first 4 integers
    # concat the remaning length of the string -4 with "#"
    # reverse the answer again and return it

# my answer
def maskify(cc):
    x = list(reversed(cc))
    y = "".join(x[0:4]) + "".join((len(cc)-4)*"#")
    return y[::-1]

# my answer refactored implicit return
maskify = lambda i: ("".join(i[::-1][0:4]) + "".join((len(i)-4)*"#"))[::-1]

print(maskify("4556364607935616")) # "############5616"
print(maskify("64607935616")) # "############5616"
print(maskify("1")) # "1"
print(maskify("")) # ""

# best practices and most clever
# of course... start at 04 and end at length of input
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

# using string interpolation
def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))

# for loop through
def maskify(cc):
  
  word = list(cc)
  #loop through the list except the last 4 index's this will also prevent
  #the loop from running for anything less than 5 index's long
  for i in range(len(word) - 4):
    word[i] = '#'
  # join and return the list
  return ''.join(word)
  
# using .rjust() will right align the string, using a specified character (space is default) as the fill character
def maskify(cc):
    return cc[-4:].rjust(len(cc), "#")

# string interpolation with f string
# return masked string
def maskify(cc):
    return f"{'#'*len(cc[:-4])}{cc[-4:]}"

# using for element in list
def maskify(cc):
    return "".join(["#" if i < len(cc) - 4 else cc[i] for i in range(len(cc))])

# using regex
import re
def maskify(cc):
    return re.sub('.', '#', cc[:-4]) + cc[-4:]

# for loop with list methods
def maskify(cc):
    # empty list to be filled
    z= []
    # get the length so you can subtract 1 every loop until it reaches to "four"
    y = len(cc)
    
    for x in cc:
        # check if the length of credit card is less than or equal 3 if yes then append it to list
        if y <= 3:
            z.append(x)
        else:
             # when the length reaches to "four" it will append the real value not "#"
            if y == 4:
                z.append(x)
            else:
                z.append('#')
                y -= 1
                
    return ''.join(z)