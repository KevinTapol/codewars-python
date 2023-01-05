"""
Fake Binary
Parameters or Edge Cases:
    input will be a string of digits
    input will never be an empty string
Return:
    a string of digits replacing digits less than 5 with 0 and digits equal to or greater than 5 with 1
Examples:
 tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]
Psuedo Code:
    take in the string and convert it to an array of each element as an integer
    create a shallow copy of the array where integers < 5 are set to 0 and integers >= 5 are set to 1
    convert the new array back into a string and return it
    lambda a map value and not type
"""
# my answer
def fake_bin(x):
    # take in the string and convert it to an array 
    y = list(x)
    # convert each string element into an int
    z = list(map(int,x))
    # create a shallow copy of the array where integers < 5 are set to string 0 and integers >= 5 are set to string 1
    a = list(map(lambda e: str(0) if e < 5 else str(1) ,z))
    # convert the new array back into a string and return it
    b = "".join(a)
    return b
    
print(fake_bin("45385593107843568")) # "01011110001100111"
print(fake_bin("509321967506747")) # "101000111101101"
print(fake_bin("366058562030849490134388085")) # "011011110000101010000011011"
print(fake_bin("15889923")) # "01111100"
print(fake_bin("800857237867")) # "100111001111"

# my answer refactored
fake_bin = lambda x: "".join(list(map(lambda e: str(0) if int(e) < 5 else str(1),list(x))))

# best practices
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

# best practices one liner
fake_bin = lambda x: ''.join('0' if c < '5' else '1' for c in x)

# declare empty string variable and concat to it given for loop conditionals
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result

# using translate() to convert every element to it's paired element
import string

def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))

# same as above but using str() instead
def fake_bin(x):
    map = str.maketrans('123456789', '000011111')
    return x.translate(map)

# calling the function on itself to loop
def fake_bin(x):
    if x == "":
        return x
    
    if int(x[0]) < 5:
        return '0'+fake_bin(x[1:])
    
    return '1' + fake_bin(x[1:])

# using // to divide and only take the integer which would be 0 until divided by 5
def fake_bin(x):
    return ''.join([str(int(i) // 5) for i in x])

# designating value strings in "01234" as "0"
def fake_bin(x):
    return "".join("0" if n in "01234" else "1" for n in x)

# lambda one liner with a for loop and index call based on e < '5'
fake_bin = lambda x: ''.join(['1','0'][e<'5'] for e in x)

# using .replace() in for loop
def fake_bin(x):
    str_num = x
    for i in range(5):
        str_num = str_num.replace(str(i), "0")

    for i in range(5, 10):
        str_num = str_num.replace(str(i), "1")
        
    return str_num

# using .sub(values to replace, what to replace with, and the input)
def fake_bin(x):
    x = __import__('re').sub(r"[0-4]", "0", x)
    x = __import__('re').sub(r"[5-9]", "1", x)
    return x