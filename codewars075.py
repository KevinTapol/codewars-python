# Digit*Digit
# Parameters or Edge Cases:
    # inputs will be integers >= 0
# Return:
    #  the square every digit of a number and concatenate them.
# Examples:
    # 9119 => 9^2 is 81 and 1^2 is 1 => 81-1-1-81 =>  811181
    # 765 => 7^2 is 49, 6^2 is 36, and 5^2 is 25 => 49-36-25 =>  493625
# Pseudo Code:
    # declare an empty string
    # iterate through each index of the input and multiply it by itself
    # concat the product each time to the new string
    # convert the string back into an integer and return it

# my answer
def square_digits(num):
    a = ""
    b = str(num)
    for e in b:
        a += str(int(e)*int(e))
    return int(a)       

# my answer implicit return
square_digits = lambda n: int("".join(str(int(e)*int(e)) for e in (str(n))[:]))

print(square_digits(9119)) # 811181
print(square_digits(0)) # 0

# best practices similar to my unrefactored answer
# **2 is the same as ^2
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

# most clever
# similar to my refactored but not an implicit return and using **2 instead of element*element
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# using a while loop
def square_digits(num):
    # s converts num to a str so we can index through it
    # when then loop through the len of the str 
    # while we're looping the string we convert it back to a int and square it
    # after we add it to a str to keep it from adding and then convert it to a int
    s = str(num)
    t = len(s)
    y=0
    g= 0
    b=""
    while y < t:
        g = int(s[y])**2 
        b= b+ str(g) 
        final = int(b)
        y=y+1
    return(final)   
    pass

# using pow(e, 2) instead of e**2 or e*e
def square_digits(n):
  return int("".join(str(pow(int(i), 2)) for i in str(n)))

# using map() to create a list
def square_digits(num):
    return int(''.join([str(n * n) for n in map(int, str(num))]))

# using list() instead of map()
def square_digits(num):
  return int(''.join([str(int(x)**2) for x in list(str(num))]))

# nested lambda inside map()
def square_digits(num):
    return int(''.join(map(lambda x: str(int(x)**2), str(num))))

# while loop but using input //= 10 to divide the input by 10 and only take the integer for each iteration
def square_digits(num):
    result = 0
    multiplier = 1
    while num:
        digit = num % 10
        result += digit ** 2 * multiplier
        multiplier *= (10, 100)[digit > 3]
        num //= 10
                                        
    return result