# Bit Counting
# Parameters or Edge Cases:
    # inputs will be a positive integer and can be multi digit
# Return:   
    # the the count of 1's in the binary equivalent of the input
# Examples:
    # The binary representation of 1234 is 10011010010, so the function should return 5 in this case
    # (0) => 0)
    # (4) => 1)
    # (7) => 3)
    # (9) => 2)
    # (10) => 2)
# Pseudocode:
    # convert the input integer into binary using bin()
    # create a copy but starting at index 2 to omit 0b from the conversion
    # count the number of 1's in the binary response
    # return the count

# my answer
def count_bits(n):
    return bin(n)[2:].count("1")

# my answer refactored implicit return
count_bits = lambda n: bin(n)[2:].count("1")

print(count_bits(0)) # 0
print(count_bits(4)) # 1
print(count_bits(7)) # 3
print(count_bits(9)) # 2
print(count_bits(10)) # 2

# best practices and most clever 
# This is not omitting the 0b in front of the conversion when using bin() but you don't need to since you are counting "1". I did it out of habit.
def countBits(n):
    return bin(n).count("1")

# brute force while loop
"""Take 13 for example: In binary form 13 becomes 1101, since the rightmost bit is a 1 we know the number is odd. Therefore n % 2 is 1 and total += 1
The ">>" operation is bitwise right shift, 1101 shifted right becomes 110 which is 6. Since the rightmost bit is now 0, the number is even and n % 2 == 0
This code just loops through this process until every bit has been checked. Check the rightmost bit (n % 2) and shift everything over, repeat."""
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

# while loop same idea but not using >>
def countBits(n):
    count = 0
    while n:
        if n % 2 == 0:
            n = n / 2
        else:
            count += 1
            n = n - 1
    return count

# '{:b}' creates a string that represents the input number in binary form without 0b preceding the binary output
def countBits(n):
    """ count_bits == PEP8, forced camelCase by CodeWars """
    return '{:b}'.format(n).count('1')

# bit_count() returns the number of 1 s in the binary representation of the absolute value of the integer
def count_bits(n):
    return n.bit_count()

# create an array and sum the 1's
def count_bits(n):
    return sum(map(int, bin(n)[2:]))

# sum the converted integer elements in the string binary conversion
def countBits(n):
    return sum(int(x) for x in bin(n)[2:]) 