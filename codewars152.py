# Simple Encryption #1 - Alternating Split
"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""
# Parameters or Edge Cases:
"""
    these are separate katas but with the same parameters
    inputs will be a string and an integer for both functions
    the string can be empty or none and contain letters, integers and special characters
    the integer can be negative or positive

    if the input integer can be less than 1 then return the input string as is
"""
# Return:
"""
    1st kata function 
        return a string of the input where the odd indexed characters come first concatenated by the even indexed characters
        reassign the output as the input and repeat the function if the 2nd input integer is greater than 1 times

    2nd kata function
        reverse the above process

"""
# Examples:
"""
    kata 1
        "This is a test!", 0 => "This is a test!"
        "This is a test!", 1 => "hsi  etTi sats!"
        "This is a test!", 2 => "s eT ashi tist!"
        "This is a test!", 3 => " Tah itse sits!"
        "This is a test!", 4 => "This is a test!"
        "This is a test!", -1 => "This is a test!"
        "This kata is very interesting!", 1 => "hskt svr neetn!Ti aai eyitrsig"

    kata 2
        "This is a test!", 0 => "This is a test!"
        "hsi  etTi sats!", 1 => "This is a test!"
        "s eT ashi tist!", 2 => "This is a test!"
        " Tah itse sits!", 3 => "This is a test!"
        "This is a test!", 4 => "This is a test!"
        "This is a test!", -1 => "This is a test!"
        "hskt svr neetn!Ti aai eyitrsig", 1 => "This kata is very interesting!"

"""
# Pseudocode:
"""
    # kata 1 encrypt

    # kata 2 decrypt
"""
# my answer for kata 1 encrypt
def encrypt(input, n):
    # if the input is empty or null return the input
    if input in ("", None):
        return input
    # declare an empty string named result
    result = ""
    # iterate through the input string
    for i,e in enumerate(input):
        # if the current index is not
        if i % 2 != 0:
            result += e
    for i,e in enumerate(input):
        if i % 2 == 0:
            result += e
    if n < 1: 
        return input
    if n == 1:
        return result
    if n > 1:
        return encrypt(result, n -1)
    return result

# my answer refactored
def encrypt(input, n):
    if input in ("", None):
        return input
    result = ""
    for i,e in enumerate(input):
        if i % 2 != 0:
            result += e
    for i,e in enumerate(input):
        if i % 2 == 0:
            result += e
    if n < 1: 
        return input
    if n == 1:
        return result
    if n > 1:
        return encrypt(result, n -1)
    return result

print(encrypt("012345", -1)) # "012345"
print(encrypt("012345", 0)) # "012345"
print(encrypt("012345", 1)) # "135024"
print(encrypt("012345", 2)) # "304152"
print(encrypt("This is a test!", 0)) # "This is a test!"
print(encrypt("This is a test!", 1)) # "hsi  etTi sats!"
print(encrypt("This is a test!", 2)) # "s eT ashi tist!"
print(encrypt("This is a test!", 3)) # " Tah itse sits!"
print(encrypt("This is a test!", 4)) # "This is a test!"
print(encrypt("This is a test!", -1)) # "This is a test!"
print(encrypt("This kata is very interesting!", 1)) # "hskt svr neetn!Ti aai eyitrsig"

# my answer for kata 2 decrypt
def decrypt(input, n):
    if input in ("", None):
        return input
    
    half = len(input) // 2

    for i in range(n):
        a = input[:half]
        b = input[half:]
        input = ""
        for i in range(half + 1):
            input += b[i:i+1] + a[i:i+1]
    return input

print(decrypt("This is a test!", 0)) # "This is a test!"
print(decrypt("hsi  etTi sats!", 1)) # "This is a test!"
print(decrypt("s eT ashi tist!", 2)) # "This is a test!"
print(decrypt(" Tah itse sits!", 3)) # "This is a test!"
print(decrypt("This is a test!", 4)) # "This is a test!"
print(decrypt("This is a test!", -1)) # "This is a test!"
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1)) # "This kata is very interesting!"

def decrypt(input, n):
    if input in ("", None):
        return input
    
    ndx = len(input) // 2

    for i in range(n):
        a = input[:ndx]
        b = input[ndx:]
        input = ""
        for i in range(ndx + 1):
            input += b[i:i+1] + a[i:i+1]
    return input

