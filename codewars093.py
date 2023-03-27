# Binary Addition
# Parameters or Edge Cases:
    # inputs will be integer
    # after looking at the test cases, I also noticed that the inputs will be non negative meaning equal to or greater than 0
# Return:
    # the sum of the inputs in binary
# Examples:
    # 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
    # 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
    # (1,1) => "10"
    # (0,1) => "1"
    # (1,0) => "1"
    # (2,2) => "100"
    # (51,12) => "111111"
# Pseudo Code:
    # get the sum of the inputs
    # use the function bin() to convert the sum into binary
    # make a shallow copy with [2:] to start after the prefix of binary
    # return the new binary copy without the prefix

# my answer, best practices and most clever
def add_binary(a,b):
    return bin(a+b)[2:]

# my answer refactored implicit return
add_binary = lambda a,b: bin(a+b)[2:]

print(add_binary(1,1)) # "10"
print(add_binary(5, 9)) # "1110"
print(add_binary(0,1)) # "1"
print(add_binary(1,0)) # "1"
print(add_binary(2,2)) # "100"
print(add_binary(51,12)) # "111111"

# {:b} isn't a decimal-to-binary converter, because nothing is in decimal in the first place. Rather, Python has a number (namely, a+b), and it will convert it into a string in some manner. The default manner is to display it in decimal, but we've overridden the default string display for numbers with our {::b}, which means it will display in binary.
# clever using "{0:b}" .format(integer) string interpolation to convert an input into a string to binary string similar to JavaScript .toString(2)
def add_binary(a,b):
    return '{0:b}'.format(a + b)

# Apparently the format() function reads 'b' as format to binary, not 'b' as in the string 'b' or the variable 'b' as a string. Another way to write it is as a formatted or f string, such as f"{number:b}" which would produce the same results, because the b is read as "Translate this to binary." I think it's especially confusing in this example because there was a variable named b. Try it in your terminal to make sure you understand. For example, f"{12:b}" and f"{a+b:b}" both return '1100' if a+b = 12.
# using the 2nd parameter of format(integer, 'b') to convert the integer to binary
def add_binary(a, b):
    return format(a + b, 'b')

# string interpolation again but with f string
def add_binary(a,b):
    return f"{a + b:b}"

# this coder created their own function to loop through and create the string binary representation
# a comment was left that 1 << n is faster than 2**n
def find_highest_power_2(num):
    n=0
    while 2**n <= num:
        n += 1
    return n-1    

def add_binary(a,b):
    sum = a + b
    number = 0
    while sum != 0:
        place_holder = find_highest_power_2(sum)
        number += 10**place_holder
        sum = sum - 2**place_holder
    return str(number)  

# using bin() but .replace() to remove the prefix of 0b
def add_binary(a,b):
    c = a + b 
    return bin(c).replace('0b','')

# using array methods with a while loop
def add_binary(a,b):
    n = a + b
    binList = []
    while (n > 0):
        binList.append(n % 2)
        n = n // 2
    return ''.join(map(str, reversed(binList)))

# using conditionals per case
def add_binary(a,b):
    return convert_to_binary(a + b)[::-1]

def convert_to_binary(num):
    if num == 0:
        return '1'
    elif num == 1:
        return '1'
    elif num % 2 == 0:
        return '0' + convert_to_binary(num / 2)
    else:
        return '1' + convert_to_binary(num - 1)[1:]
    
# splitting the output on b of 0b and return the index after the split
def add_binary(a,b):
    return str(bin(a+b)).split('b')[1]

# while loop for string
def add_binary(a,b):
    
    s = ""
    num = a + b
    
    while num > 0:
        s = str(num%2) + s
        num = num/2
        
    return s