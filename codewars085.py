# Mumbling
# Parameters or Edge Cases:
    # input strings will only be letters a-z
    # strings can be capitalized
# Return:
    # a string repeating each letter by it's index
    # Capitalize the first letter of each repetition 
    # separate each letter with -
# Examples:
    # "abcd" -> "A-Bb-Ccc-Dddd"
    # "RqaEzty" -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    # "cwAt" -> "C-Ww-Aaa-Tttt"
# Pseudo Code:
    # declare an empty list
    # iterate through the string concatenating the product of each element and its index to the empty list and capitalize the first index 
    # convert the array back into a string joining each element by -
    # return the new string

# my answer
def accum(s):
    a = []
    for e in range(len(s)):
        a.append((s[e]*(e+1)).title())
    return "-".join(a)

# my answer refactored implicit return 
accum = lambda s:"-".join(s[e]*(e+1) for e in range(len(s))).title()

print(accum("abcd")) # "A-Bb-Ccc-Dddd"
print(accum("RqaEzty")) # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt")) # "C-Ww-Aaa-Tttt"
print(accum("ZpglnRxqenU")) # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")

# best practices and most clever
# The enumerate() function adds a counter as the key of the enumerate object. In this case the indexes of the length of s.
# enumerate(s) returns a list of elements of tuples [(index,element)] in s
# for index(element), element in enumerate(String)
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# using title() to capitalize the first word in a string of words
def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))

# similar to my answer but concatenating "-" each time then removing the final - from the answer
def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]

# same idea as above but being specific about the length - 1 
def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]

# declaring a string then concat if not at the final length of the string
def accum(s):
    str = ""
    for i in range(0, len(s)):
        str += s[i].upper()
        str += s[i].lower()*i
        if i != len(s)-1:
            str += "-"
    return str

# clean version of enumearate() then remove last character in final string
def accum(s):
    value = ""
    for i,c in enumerate(s):
        value += c.upper() + c.lower()*i + "-"
    return value[:-1]

# using .strip("-") to remove the final character 
def accum(s):
    value = ""
    for i,c in enumerate(s):
        value += c.upper() + c.lower()*i + "-"
    return value[:-1] 

# same idea but using a counter + 1 instead of enumerate()
def accum(s):
    counter = 0
    output = ""
    for letter in s:
        output += letter.upper() + letter.lower() * counter + '-'
        counter += 1
    return output[:-1]

# for index, element in enumerate(s, 1) to start at 1 instead of index 0
# def accum(s):
#     words = []
#     for i, letter in enumerate(s, 1):
#     	word = i * letter
#         words.append(word.capitalize())
#     return '-'.join(words)

# using conditionals on when to concat "-"
def accum(s):
    string = ""
    for i in range(0,len(s)):
        if i < (len(s)-1):
            string = string+s[i]*(i+1)+"-"
        else:
            string = string+s[i]*(i+1)
    return string.title()

# using .capitalize() on each concatenated element
def accum(s):
    str = s[0].capitalize()
    for i in range(1, len(s)):
        str += "-" + (s[i] * (i + 1)).capitalize()
    return str