# Parameters or Edge Cases:
#       input will be a string with atleast 2 characters
# Return:
#       the input string without it's first and last character
# Examples:
        # (remove_char('eloquent'), 'loquen')
        # (remove_char('country'), 'ountr')
        # (remove_char('person'), 'erso')
        # (remove_char('place'), 'lac')
        # (remove_char('ok'), '')
        # (remove_char('ooopsss'), 'oopss')
# Psuedo Code:
#       return the input string sliced at index 1 and index length -1

# my answer
def remove_char(s):
    # return the input string sliced at index 1 and index length -1
    return s[1:len(s)- 1]

# my answer refactored using lambda similar to JavaScript arrow function
remove_char = lambda s: s[1:len(s) -1]  

print(remove_char('eloquent')) # 'loquen'
print(remove_char('ok')) # ''

# best practices and most clever
# same as my answer but using -1 as the final slice instead of len(string) -1
def remove_char(s):
    return s[1 : -1]

# here they are using an if else statement for empty string return
def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]

# converting to a list, using list methods to mutate, converting back into a string and returning it
def remove_char(s):\
    # converting the input into a list
    s = list(s)
    # remove the last character .pop()
    s.pop()
    # remove the first character .pop(0)
    s.pop(0)
    # returning it to a string with .join()
    return ''.join(s)

# converting to a list, deleting the values at the index, using a for loop to concatenate to an empty string and return it
def remove_char(s):
    a = list(s)
    del a[0]
    del a[-1]
    l = ''
    for i in a:
        l += i
    return l

# converting to a list, pop last value, reverse the list, pop last value (which was first value before reverse), reverse the list again and convert back to a string
def remove_char(s):
    a = list(s)
    a.pop()
    a.reverse()
    a.pop()
    a.reverse()
    return ''.join(a)

# using regex
import re
def remove_char(s): return re.sub('^.(.*).$', '\g<1>', s)

# using enumerate
def remove_char(s):
    return ''.join(item for index, item in enumerate(s) if index != 0 and index != len(s) - 1)

# for loop
def remove_char(s):
    result_s = ''
    for i in range(0, len(s)):
        if i != 0 and i != len(s) - 1:
            result_s = result_s + s[i]
    return result_s

# using .split() on indexes
def remove_char(s):
    return s.split()[0][1:len(s)-1]

# using .append() with a for loop and a declared list
def remove_char(s):
    res = []
    for i in s:
        res.append(i)
    
    return ''.join(res[1:len(res)-1])    