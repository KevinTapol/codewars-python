# Write Number in Expanded Form
"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""
# Parameters or Edge Cases:
"""
    inputs will be integers greater than 0
    inputs will not be empty or null
"""
# Return:
"""
    a string representation of the input with each digit at its tenths place
"""
# Examples:
"""
    # 12 => '10 + 2'
    # 42 => '40 + 2'
    # 70304 => '70000 + 300 + 4'
"""
# Pseudocode:
"""
    # declare an empty string named result
    # declare an empty array named array_of_nums
    # take in the integer, convert it into a string then into an array of strings named x
    # iterate through the array x and for each index and element using enumerate()
        # append that element to array_of_nums with the product of  '0' multiplied by the length of the array subtracted by the current index plus 1
    # iterate through array_of_nums and if the element converted to an integer is not equal to 0 then append it to resultt
    # convert result into a string joined on whitespace + whitespace and return result
"""

# my answer
def expanded_form(num):
    # declare an empty array named result
    result = []
    # declare an empty array named array_of_nums
    array_of_nums = []
    # take in the integer, convert it into a string then into an array of strings named x
    x = [e for e in str(num)]
    # iterate through the array x and for each index and element using enumerate()
    for i,e in enumerate(x):
        # append that element to array_of_nums with the product of  '0' multiplied by the length of the array subtracted by the current index plus 1
        array_of_nums.append(e + '0'*(len(x) - (i + 1)))
    # iterate through array_of_nums and if the element converted to an integer is not equal to 0 then append it to result
    for e in array_of_nums:
        if int(e) != 0:
            result.append(e)
    # convert result into a string joined on whitespace + whitespace and return result
    return " + ".join(result)

# my answer without comments
def expanded_form(num):
    result = []
    array_of_nums = []
    x = [e for e in str(num)]
    for i,e in enumerate(x):
        array_of_nums.append(e + '0'*(len(x)- (i +1)))
    for e in array_of_nums:
        if int(e) != 0:
            result.append(e)
    return " + ".join(result)

# my answer refactored
def expanded_form(num):
    x = [e for e in str(num)]
    array_of_nums = [e + '0'*(len(x) - (i + 1)) for i,e in enumerate(x)]
    return " + ".join([e for e in array_of_nums if int(e) != 0])

print(expanded_form(12)) # '10 + 2'
print(expanded_form(42)) # '40 + 2'
print(expanded_form(70304)) # '70000 + 300 + 4'

# best practices
# very similar to my answer
# wow list(str(multi_digit_number)) will return the multi digit number as an array with each digit as a string element which is the same as my code [e for e in str(num)]
# here they are using y instead of i for index with enumerate() and if the current element does not equal '0' then concat the appropriate '0' per index reference maths. Finally convert the array back into a string joined on the proper separator " + "
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

# one liner of best practices and most clever
def expanded_form(num):
    return " + ".join([str(int(v)*int("1"+"0"*(len(str(num))-(i+1)))) for i,v in enumerate(str(num)) if v != "0"])

# here they are using 10 to the power of index of the input string in reverse order and finishing with reversing the final array converted to a string with the proper separator
def expanded_form(num):
    return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])

# same idea as above but concatenating to the element each iteration instead of converting then concatenating for each iteration
def expanded_form(num):
    return ' + '.join([x+'0'*i for i,x in enumerate(str(num)[::-1]) if x != '0'][::-1])

# same idea as reversed input 
# using range(start, stop, step) to go in reverse order stop at the last value which is the first value in this case and step backwards
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)

# I didn't know you could strip more than just whitespace with .strip() method here they strip the string ' +'
# here they are concatenating using .format() with the current element for tenths place math based on index
def expanded_form(num):
    num = str(num)
    st = ''
    for j, i in enumerate(num):
        if i != '0':
            st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
    return st.strip(' +')

# using variable declarations to reference as range(start, stop, step) instead of using enumerate()
def expanded_form(num):
    s = str(num)
    n = len(s)
    return ' + '.join( [s[-i]+"0"*(i-1) for i in range(n,0,-1) if s[-i] != "0"])