# Roman Numerals Encoder
"""
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""
# Parameters or Edge Cases:
"""
    inputs will be integers from 1-3999 inclusively
    will there be empty or null inputs?
"""
# Return:
"""
    the Roman Numeral string equivalent of the integer input
"""
# Examples:
"""
    
    1990 => 1000=M, 900=CM meaning 1000 - 100, 90=XC meaning 100-10 =>'MCMXC'
    2008 => 'MMVIII'
    1666 => 'MDCLXVI'
    1000 => 'M'

"""
# Pseudocode:
"""
    # declare an array for 1 4 5 and 9 values for each tenths place and name it years
    # declare an array of matching roman numeral letters for each 1 4 5 and 9 tenths place value and name it letters
    # declare an empty string result
    # iterate through the length of years which is the same as letters starting at index 0
    # declare a local variable taking only the integer from the quotient of the input divided by the current index of year
    # if the quotient is not 0
    # repeat the corresponding index in letter quotient number of times and concat it to result
    # reassign the input to the current input minus the result of the current index value of years multiplied by quotient
    # NOTE this is removing the total value of the current tenths place from the input meaning ex input = 1900 then set input = 1900 - 1000
    # return result

"""

# my answer
def solution(input):
    # declare an array for 1 4 5 and 9 values for each tenths place and name it years
    years = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # declare an array of matching roman numeral letters for each 1 4 5 and 9 tenths place value and name it letters
    letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # declare an empty string named result
    result = ""

    # iterate through the length of years which is the same as letters starting at index 0
    for i in range(len(years)):
        # declare a local variable taking only the integer from the quotient of the input divided by the current index of year
        quotient = input // years[i]
        # if the quotient is not 0
        if quotient != 0:
            # repeat the corresponding index in letter quotient number of times and concat it to result
            result += letters[i]*quotient
            # reassign the input to the current input minus the result of the current index value of years multiplied by quotient
            # NOTE this is removing the total value of the current tenths place from the input meaning ex input = 1900 then set input = 1900 - 1000
            input -= years[i] * quotient
    # return result
    return result

print(solution(1990)) # 'MCMXC'
print(solution(2008)) # 'MMVIII'
print(solution(1666)) # 'MDCLXVI'
print(solution(1000)) # 'M'


# I found a similar solution using divmod and refactored it to match my previous solution
def solution(input):
    # declare an array for 1 4 5 and 9 values for each tenths place and name it years
    years = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # declare an array of matching roman numeral letters for each 1 4 5 and 9 tenths place value and name it letters
    letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # declare an empty string named result
    result = ""

    # create a 2D list array with the corresponding year and letter tuple array pairs by index from the years and letters array
    for year,letter in list(zip(years, letters)):
        quotient,input = divmod(input,year)
        #divide the input by the current iterating year and grab the resulting quotient and reassign the remainder as the next input

        quotient,input = divmod(input,year)
        # repeat the corresponding letter of the letter year pair currently being divided the number of times equivalent to the quotient and append the product to result
        result += letter*quotient
    # return result
    return result

# best practices and most clever
# declare an empty string 
# created an object where the integer year is the key and the value is the roman numeral as a string
# sort the keys in reversed order meaning starting at 1
# while the input is greater than the current integer, concat the value of the current key to the empty string and subtract the key from n repeating the loop until n is less than key

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

# declaring arrays of every outcome  per index per tenths place
# concat together each respective whole integer return divided by each tenths place array
units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]

# this is the original divmod() example that was very similar to my answer so I made a break down of it how I would use divmod for my 2nd answer
anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def solution(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)

# similar to the divmod but creating the list of tuples right away instead of using zip()
def solution(x):
    table = [
        (1000,"M"),
        (900,"CM"),
        (500,"D"),
        (400,"CD"),
        (100,"C"),
        (90,"XC"),
        (50,"L"),
        (40,"XL"),
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I")
    ]
    for num, rep in table:
        if x >= num:
            return rep + solution(x-num)
    return str()

# very similar to best practices
def solution(n):
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    roman = ''
    for a in reversed(sorted(dic.keys())):
        while (a <= n):
            n = n - a;
            roman = roman + dic[a];
    return roman

# lol I thought about doing if statements for each tenths place outcome like this
def solution(n):
    if n == 0: return ""
    if n >= 1000: return "M" + solution(n-1000)
    if n >= 900: return "CM" + solution(n-900)
    if n >= 500: return "D" + solution(n-500)
    if n >= 400: return "CD" + solution(n-400)
    if n >= 100: return "C" + solution(n-100)
    if n >= 90: return "XC" + solution(n-90)
    if n >= 50: return "L" + solution(n-50)
    if n >= 40: return "XL" + solution(n-40)
    if n >= 10: return "X" + solution(n-10)
    if n >= 9: return "IX" + solution(n-9)
    if n >= 5: return "V" + solution(n-5)
    if n >= 4: return "IV" + solution(n-4)
    else: return "I" + solution(n-1)