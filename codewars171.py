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
    # create a copy named result of first string lowercase everything then uppercase the first letter of each word with .title()
    # create a copy named check of the 2nd input string lowercase everything then uppercase the first letter of each word with .title()
    # if an element of check exists in result and is not the first index of result then lowercase the element of result
    # return result
"""
# my answer
def title_case(a,b):
    # create a copy named result of first string lowercase everything then uppercase the first letter of each word with .title()
    result = a.title()
    # create a copy named check of the 2nd input string lowercase everything then uppercase the first letter of each word with .title()
    
    # if an element of check exists in result and is not the first index of result then lowercase the element of result
    # return result
    # if len(a) == 0:
    #     return ''
    if not b:
        return result
    else:
        check = b.title()
        for e in result:
            if e in check:
                e.lower()
        return result

# print(title_case('')) # ''
print(title_case('a clash of KINGS', 'a an the of')) # 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # 'The Wind in the Willows'
print(title_case('the quick brown fox')) # 'The Quick Brown Fox'