# Switch it Up!
"""

When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
"""
# Parameters or Edge Cases:
"""
    inputs will be integers 0-9
"""
# Return:
"""
    return the input integer as it's pronounced spelling in string format using a switch case
"""
# Examples:
"""
    # 0 => "Zero"
    # 9 => "Nine"
"""
# Pseudocode:
"""
    create a switch case of 10 cases for each integer 0-9 and return the string spelling
    or create an array of string words matching their index and call the index based on the input
"""

# my answer
# def switch_it_up(number):
#     arr = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
#     return arr[number]

# my answer using a switch case because the kata requested it
def switch_it_up(number):
    match number:
        case 0:
            return 'Zero'
        case 1:
            return 'One'
        case 2:
            return 'Two'
        case 3:
            return 'Three'
        case 4:
            return 'Four'
        case 5:
            return 'Five'
        case 6:
            return 'Six'
        case 7:
            return 'Seven'
        case 8:
            return 'Eight'
        case 9:
            return 'Nine'
print(switch_it_up(0)) # 'Zero'
print(switch_it_up(9)) # 'Nine'

# best practices 
# using the same as my answer of array by index call but not declaring the array as a variable
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]

# using dictionary/object key value pair call
def switch_it_up(number):
    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return number_converter[number]

# using a dictionary/object but with the .get() method instead of key call 
def switch_it_up(number):
    dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"}
    
    return dict.get(number)

# the requested solution from the kata using switch case
def switch_it_up(n):
    match n:
        case 0:return'Zero'
        case 1:return'One'
        case 2:return'Two'
        case 3:return'Three'
        case 4:return'Four'
        case 5:return'Five'
        case 6:return'Six'
        case 7:return'Seven'
        case 8:return'Eight'
        case 9:return'Nine'

# using if conditionals instead of switch case
def switch_it_up(number):
    if number == 1:
        return"One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    elif number == 0:
        return "Zero"
    else:
        return "i have depression please help"
    
# creating a string of words then splitting on white space to create an array and call by index from input
def switch_it_up(number):
    return 'Zero One Two Three Four Five Six Seven Eight Nine'.split()[number]