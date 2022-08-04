# Parameters or Edge Cases:
# Return: 'Yes' for true 'No' for false
# Examples:
# Psuedo Code:

# my answer
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

# best practices
def bool_to_word(bool):
    return "Yes" if bool else "No"

# most clever
def bool_to_word(bool):
    return ['No', 'Yes'][bool]