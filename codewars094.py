# Regex validate PIN code
# Parameters or Edge Cases:
    # inputs will be strings of letters and numbers
    # can the strings be empty or null?
    # will the numbers always be integers?
    # from test cases I found out inputs can contain symbols - and .
# Return:
    # boolean true if the input string contains either 4 or 6 integers else false
# Examples:
    # "1234"   -->  true
    # "12345"  -->  false
    # "a234"   -->  false
# Pseudo Code:
    # check if the length of the input is 4 or 6 
    # check if all elements in the input string are integers
    # if both conditions meet return true else false

# my answer brute force for elements in string and conditionals
def validate_pin(pin):
    if (len(pin) != 4) and (len(pin) != 6):
        return False
    else:
        for e in pin:
            if e not in '0123456789':
                return False
        return True

# my answer using isdigit() method returns True if all the characters are digits, otherwise False.
def validate_pin(pin):
    if (len(pin) != 4) and (len(pin) != 6):
        return False
    else:
        return pin.isdigit()
    
# my isdigit() answer refactored implicit return if length is 4 or 6 and input has contains only integers in string format
validate_pin = lambda p: ((len(p) == 4) or (len(p) == 6)) and p.isdigit()

print(validate_pin("1.234")) # False
print(validate_pin("1234")) # True
print(validate_pin("123456")) # True
print(validate_pin("a234")) # False
print(validate_pin("-1a234")) # False

# best practices and most clever
# checking if the length of the input is in the tuple or immutable array elements of 4 or 6 and using .isdigit() 
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# same idea as best practices but using a list or mutable array
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()
  
# using regex .fullmatch(regex, string, flags=0) this returns true only if the entire string matches with integers and is a length of 4 or 6
import re
def validate_pin(pin):
    #return true or false
    return bool(re.fullmatch("\d{4}|\d{6}", pin))

# same answer but with full commenting
import re
def validate_pin(pin):
    '''\d only digits
    {} = number of digits with \d
    | = or
    so, saying "accept all 4 or 6 elements if the're just digits'''
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False

# regex with .match() instead of .fullmatch()
import re
def validate_pin(pin):
    return re.match(r'(?:\d{4}|\d{6})\Z', pin) is not None

# regex with .search()
def validate_pin(pin):
    import re
    if len(pin) == 4 or len(pin) == 6: #not 4 or 6 digits
        if re.search('[^0-9]', pin) == None : #contains non-digit chars
            return True
            
    return False

# separate functions to test length and key comparisons for boolean returns
def merge(array1,array2):
    array3 = []
    i = 0
    j = 0
    while (i < len(array1) and j < len(array2)):
        if (array1[i] < array2[j]):
            array3.append(array1[i])
            i = i + 1
        else:
            array3.append(array2[j])
            j = j + 1
    return array3 + array1[i:] + array2[j:]
    
def validate_pin(pin):
    #return true or false
    
    key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # check conditions
    if len(pin) == 6 or len(pin) == 4:
        p = [i for i in pin]
        m = merge(key, p)
        
        # check lengths
        if len(set(m)) == len(key):
            return True
        return False
    else:
        return False
    
# using .isnumeric() instead of isdigit()
def validate_pin(pin):
    if pin.isnumeric() and len(pin) in [4,6]:
        return True
    return False

# try except block for errors
def validate_pin(pin):
    if(len(pin) != 4 and len(pin) != 6):
        return False
    for i in range(len(pin)):
        try:
            int(pin[i])
            if(i == len(pin) - 1):
                return True
        except ValueError:
            break
    return False

# dictionary/object with .issubset(object with string integers)
def validate_pin(pin):

    num={'0','1','2','3','4','5','6','7','8','9'}
    pin_set=set(pin)
    
    if (len(pin)==4 or len(pin)==6) and pin_set.issubset(num):
        return True
    else:
        return False
    
# using all() instead of isdigit()
digits = [str(n) for n in range(10)]

def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and all(p in digits for p in pin)