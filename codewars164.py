# IP Validation
"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
"""
# Parameters or Edge Cases:
"""
    inputs will be a string of letters, numbers and special characters
    inputs can be empty or null
"""
# Return:
"""
    boolean True if the string contains four integers between 0 to 255 inclusively separated by three periods else false
    # for this specific kata any values that start with '0' but are less than 255 are still considered False ex '024' is between '0' and '255' but not for the case of this kata
"""
# Examples:
"""
    '12.255.56.1' =>     True
    '' =>                False
    'abc.def.ghi.jkl' => False
    '123.456.789.0' =>   False
    '12.34.56' =>        False
    '12.34.56 .1' =>     False
    '12.34.56.-1' =>     False
    '123.045.067.089' => False
    '127.1.1.0' =>       True
    '0.0.0.0' =>         True
    '0.34.82.53' =>      True
    '192.168.1.300' =>   False
"""
# Pseudocode:
"""
    # take in the input and convert it into an array x splitting each element on '.'
    # if the length of x is not equal to 4 return false
    # iterate through each element in x and if any of the elements is not a digit return false isdigit()
    # if the element is a digit and a length of 3 and starts with '0' return false
    # convert x where each element is an integer
    # iterate through each element and if they are less than 0 or greater than 255 return false
    # outside of the for loop return true

"""

# my answer
def is_valid_IP(input):
    # take in the input and convert it into an array x splitting each element on '.'
    x = input.split('.')
    # if the length of x is not equal to 4 return false
    if len(x) != 4:
        return False
    # iterate through each element in x and if any of the elements is not a digit return false isdigit()
    for e in x:
        if e.isdigit() == False:
            return False
        # if the element is a digit and a length of 3 and starts with '0' return false
        if e.startswith('0') and len(e) != 1:
            return False
    # convert x where each element is an integer
    x = [int(e) for e in x]
    # iterate through each element and if they are less than 0 or greater than 255 return false
    for e in x:
        if e < 0 or e > 255:
            return False
    # outside of the for loop return true
    return True

# my answer refactored to a single for loop
def is_valid_IP(input):
    x = input.split('.')
    if len(x) != 4:
        return False
    for e in x:
        if e.isdigit() == False:
            return False
        if e.startswith('0') and len(e) != 1:
            return False
        if int(e) < 0 or int(e) > 255:
            return False
    return True

print(is_valid_IP('12.255.56.1')) # True
print(is_valid_IP('')) # False
print(is_valid_IP('abc.def.ghi.jkl')) # False
print(is_valid_IP('123.045.067.089')) # False

# best practices and most clever
# importing socket
import socket

def is_valid_IP(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False
    

# similar to my answer but one line conditional in for loop
def is_valid_IP(strng):
    if len(strng.split(".")) != 4:
        return False
    
    for group in strng.split("."):
        if not group.isdigit() or group != str(int(group)) or not 0 <= int(group) <= 255:
            return False
    
    return True

# one line version of similar to my answer but using all()
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

# lol there is an import to check ip address
import ipaddress

def is_valid_IP(strng):
    try:
        ipaddress.ip_address(strng)
        return True
    except:
        return False
    
# using regex
def is_valid_IP(address):
    return bool(__import__('re').match('(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}\Z',address))

# implicit return lambda for Codewars only
is_valid_IP = lambda str: all(False if not(i.isdigit()) else False if "{}".format(int(i))!=i else int(i)>-1 and int(i)<256 for i in str.split('.')) and len(str.split('.'))==4