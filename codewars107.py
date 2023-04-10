# Sum of Digits / Digital Root - Digital root is the recursive sum of all the digits in a number.
# Parameters or Edge Cases:
    # The input will be a non-negative integer.
# Return:
    # a single digit
    # Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# Examples:
    # 16  -->  1 + 6 = 7
    # 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
    # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
# Pseudo Code:
    # convert the input integer into
    # add up the digits
    # if the sum is a single digit, return the digit
    # else repeat the loop while the length of the sum is not 1

# my answer
def digital_root(n):
    x = sum([int(e) for e in str(n)])
    if x <= 9:
        return x
    else:
        return digital_root(x)
   

# my answer refactored implicit return
digital_root = lambda n: n if n <= 9 else digital_root(sum([int(e) for e in str(n)])) 

print(digital_root(16)) # 7
print(digital_root(942)) # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2

# best practices
# here they are using map(element conversion to int, str(n)) instead of [int(e) for e in str(n)]
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# most clever
"""Repetition is the mother of didactics, so here's a simple explanation:

If n is not divisible by 9, the digital root is simply n % 9 (see Rellek's answer on this StackExchange post for a concise explanation).

If n IS divisible by 9, we have n % 9 == 0, which can't be the digital root. Then, the correct result is 9. An even simpler solution would be

def digital_root(n):
  return n % 9 or 9
But this fails if n == 0 (here, the correct result is 0, of course). Therefore, return n % 9 or (n and 9) (redundant parantheses added for clarity) is short for

if n == 0:
  return 0
elif n % 9 == 0:
  return 9
else:
  return n % 9
"""
def digital_root(n):
	return n%9 or n and 9 

# similar to the idea of best practices
def digital_root(n):
    return 1 + ((int(n) - 1) % 9) if n>0 else 0


# while loop instead of function call
def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n

# while loop using divmod()
def digital_root(n):
    while n >= 10:
        n = sum(divmod(n, 10))
    return n

# declaring an int and re-declaring it as a function call if more than 1 digit
def digital_root(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root