# Parameters or Edge Cases: no restrictions on inputs but test cases are only testing for boolean
# Return: 'Yes' for boolean true else 'No'
# Examples: 'Yes' for true 'No' for false
# Psuedo Code: If the input is boolean true return string Yes else string No

# my answer
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'
print(bool_to_word(True)) # Yes
print(bool_to_word(False)) # No

# best practices
def bool_to_word(bool):
    return "Yes" if bool else "No"

# most clever
def bool_to_word(bool):
    return ['No', 'Yes'][bool]