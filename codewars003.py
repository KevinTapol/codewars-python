# Parameters or Edge Cases:
# Return: opposite value int or float 
# Examples: 1: -1
#           14: -14
#           -34: 34
# Psuedo Code: take input float or int multiply by -1 return product

# my answer
def opposite(number):
    return number * (-1)
print(opposite(1)) # -1
print(opposite(0)) # 0
print(opposite(14)) # -14
print(opposite(-34)) # 34

# best practices
def opposite(number):
    return -number