# Title Case
"""
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Arguments (Haskell)
First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
Arguments (Other languages)
First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
Example
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
"""
# Parameters or Edge Cases:
"""
inputs will be a string of words of letters that can be upper or lower case
inputs can be empty
"""
# Return:
"""
the first string with each word as lowercase except for the first letter and if the 2nd string exists in the input string and is not the first word then lowercase the word and return it
"""
# Examples:
"""
    ''  => ''
    'a clash of KINGS', 'a an the of  =>, 'A Clash of Kings'
    'THE WIND IN THE WILLOWS', 'The In'  => 'The Wind in the Willows'
    'the quick brown fox'  => 'The Quick Brown Fox'
"""
# Pseudocode:
"""
    # declare an empty array result
    # declare an array of the first string to lowercase split on white space named arr_a
    # declare an array of the second string to lowercase split on white space named arr_b
    # enumerate through arr_a to reference both index and element
    # if the current index is 0 or the current element is not in arr_b append the the element with the first letter of the word to uppercase
    # if the current index is not 0 or the current element is in arr_b append the current lower case element
    # convert the array result into a string joining on white space and return it
"""
# my answer
def title_case(a, b=''):
    # declare an empty array result 
    result = []
    # declare an array of the first string to lowercase split on white space named arr_a
    arr_a = a.lower().split()
    # declare an array of the second string to lowercase split on white space named arr_b
    arr_b = b.lower().split()
    # enumerate through arr_a to reference both index and element
    for i,e in enumerate(arr_a):
        # if the current index is 0 or the current element is not in arr_b append the the element with the first letter of the word to uppercase
        if i == 0 or e not in arr_b:
            result.append(e.capitalize())
        # if the current index is not 0 or the current element is in arr_b append the current lower case element
        else:
            result.append(e)
    # convert the array result into a string joining on white space and return it
    return ' '.join(result)

# my answer refactored declaring the result array as the one line for loop with conditionals
def title_case(a, b=''):
    arr_a = a.lower().split()
    arr_b = b.lower().split()
    result = [e.capitalize() if i == 0 or e not in arr_b else e for i,e in enumerate(arr_a)]
    return ' '.join(result)
    
# my answer refactored declaring variables in one line and returning the for loop conditionals array converted to string in one line
def title_case(a, b=''):
    arr_a, arr_b = a.lower().split(), b.lower().split()
    return ' '.join([e.capitalize() if i == 0 or e not in arr_b else e for i,e in enumerate(arr_a)])

print(title_case('')) # ''
print(title_case('First a of in','an often into')) # 'First A Of In'
print(title_case('a clash of KINGS', 'a an the of')) # 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # 'The Wind in the Willows'
print(title_case('the quick brown fox')) # 'The Quick Brown Fox'

# best practices and most clever
# same as my refactored answer but switching the conditionals
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

# using map() and lambdas for arrays
def title_case(title, minor_words=''):
    proper_title = ''

    # lowercase the entire list
    title_words = map(lambda x:x.lower(), title.split(' '))
    
    # split the minor word strings
    dont_cap = minor_words.split(' ')
    
    # always upper case the first word
    title_words = [item.capitalize() for item in title_words]
    
    # lower case the split minor words array
    dont_cap  = [item.lower() for item in dont_cap]
    
    #print title_words
    
    # loop through the 2nd word to the end word
    for i in range(1,len(title_words),1):
        # loop through the minor_words array
        for item in dont_cap:
            # if the minor word is equal to the title word, lower case it
            if item == title_words[i].lower():
                title_words[i] = title_words[i].lower()
    
    return " ".join(title_words)

# one liner for codewars only using enumerate
def title_case(title, minor_words=''):
	return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))

# one liner for codewars only using for element in object instead of enumerate
def title_case(title, minor_words = ''):
    return ' '.join(c if c in minor_words.lower().split() else c.title() for c in title.capitalize().split())