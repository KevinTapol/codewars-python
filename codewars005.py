# Parameters or Edge Cases: 
#       no restrictions on inputs but test cases are only testing for boolean
# Return: 
#       'Yes' for boolean true else 'No'
# Examples: 
#       'Yes' for true 'No' for false
# Psuedo Code: 
#       If the input is boolean true return string Yes else string No

# my answer
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'
print(bool_to_word(True)) # Yes
print(bool_to_word(False)) # No

# my answer refactored lambda and one line if else
bool_to_word = lambda boolean: "Yes" if boolean else "No"

# best practices
# putting if else on one line
def bool_to_word(bool):
    return "Yes" if bool else "No"

# most clever
# True equates to 1 so index of 1 of the list returns "Yes"
def bool_to_word(bool):
    return ['No', 'Yes'][bool]

# using {}.get
bool_to_word = {True: 'Yes', False: 'No'}.get

# using list [] 
bool_to_word = ['No','Yes'].__getitem__

# lambda with and or statements
bool_to_word = lambda b: b and "Yes" or "No"

# using parameters with .get()
bool_to_word= lambda _:{1:'Yes'}.get(_,'No')

# using a string slice start stop step
bool_to_word=lambda b:"YNeos"[1-b::2]

# using .join()
def bool_to_word(boolean):
    return ''.join(['Yes' if bool(boolean) else 'No'])

# using key value pair 
def bool_to_word(boolean):
    return {True:"Yes",False:"No"}.get(boolean)