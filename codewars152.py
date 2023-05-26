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
    # if the input is empty or null return the input
    # declare an empty string named result
    # iterate through the input string
    # grab all the odd index elements and append them to result
    # iterate through the input string again
    # grab all the even index elements and append them to result
    # if the input integer n is less than 1, return the input
    # if the input integer n is equal to 1 return result
    # if the input integer n is more than 1 recall the function but with result as the input string and n -1 as the integer

    # kata 2 decrypt
    # if the input is empty or null return the input
    # declare a variable as integer and not remainder return of half the input length
    # create a for loop starting at 0 and ending at the input integer
    # declare an array copy of the input starting at index 0 and stopping at half
    # declare an empty string
    # create a nested for loop starting at 0 and stopping at half + 1 to include half in the iteration
    # grab the current index copy of b and append it to input then do the same with a alternating concatenation to input of even and odd
    # outside of the parent for loop return the input
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
        # grab all the odd index elements and append them to result 
        if i % 2 != 0:
            result += e
    # iterate through the input string again
    for i,e in enumerate(input):
        # grab all the even index elements and append them to result
        if i % 2 == 0:
            result += e
    # if the input integer n is less than 1, return the input
    if n < 1: 
        return input
    # if the input integer n is equal to 1 return result
    if n == 1:
        return result
    # if the input integer n is more than 1 recall the function but with result as the input string and n -1 as the integer
    if n > 1:
        return encrypt(result, n -1)

# my answer for kata 1 encrypt refactored
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
    # if the input is empty or null return the input
    if input in ("", None):
        return input
    # declare a variable as integer and not remainder return of half the input length
    half = len(input) // 2

    # create a for loop starting at 0 and ending at the input integer
    for i in range(n):
        # declare an array copy of the input starting at index 0 and stopping at half
        a = input[:half]
        # declare an array copy of the input starting at half and stopping at the last index of input
        b = input[half:]
        # declare an empty string
        input = ""
        # create a nested for loop starting at 0 and stopping at half + 1 to include half in the iteration
        for i in range(half + 1):
            # grab the current index copy of b and append it to input then do the same with a alternating concatenation to input of even and odd
            input += b[i:i+1] + a[i:i+1]
    # outside of the parent for loop return the input
    return input

# my answer for kata 2 decrypt refactored
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

# best practices and most clever
# similar to my code but way cleaner in string copy concatenation
def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

# similar to best practices and most clever but using if not input for null and empty inputs to return the input
# also, inside the for loop they are multiline declaring string copies 
def decrypt(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s

# using text == None for null and empty
# using the encrypt function inside of decrypt
def decrypt(text, n):
    if text == None: return text
    
    decodeList = encrypt(list(range(len(text))),n)
    return ''.join( text[decodeList.index(i)] for i in range(len(text)) )


def encrypt(text, n):

    if text == None: return text
    return encrypt(text[1::2] + text[0::2],n-1) if n>0 else text

# Codewars only one liners for each function
def encrypt(text, n):
    return "".join([(text)[((i+1)*2**n-1)%(len(text) + (len(text)+1)%2)] for i in range(len(text))]) if text and not n<=0 else text

def decrypt(text, n):
    return "".join({num: text[j] for j, num in enumerate([((i+1)*2**n-1)%(len(text) + (len(text)+1)%2) for i in range(len(text))])}.values()) if text and not n<=0 else text
