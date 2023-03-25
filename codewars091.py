# Friend or Foe?
# Parameters or Edge Cases:
    # inputs will be a list of strings
    # can they empty or null?
    # will there be special characters?
    # do i need to worry about case sensitivity?
# Return:
    # a new list of the input list elements that have only 4 characters in index order 
# Examples:
    # ["Ryan", "Kieran", "Jason", "Yous"] => ["Ryan", "Yous"]
    # ["Ryan", "Kieran", "Mark",] => ["Ryan", "Mark"]
    # ["Ryan", "Jimmy", "123", "4", "Cool Man"] => ["Ryan"]
    # ["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"] => ["Jimm", "Cari", "aret"]
# Pseudo Code:
    # create an empty list
    # iterate through the input list and append each element that has a length of 4 to the empty list
    # return the empty list

# my answer
def friend(x):
    y = []
    for e in x:
        if len(e) == 4:
            y.append(e)
    return y

# my answer refactored implicit return
friend = lambda x: list(e for e in x if len(e) == 4)

print(friend(["Ryan", "Kieran", "Jason", "Yous"])) # ["Ryan", "Yous"]
print(friend(["Ryan", "Kieran", "Mark",])) # ["Ryan", "Mark"]
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"])) # ["Ryan"]
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"])) # ["Jimm", "Cari", "aret"]

# best practices and most clever
# same as my implicit return
def friend(x):
    return [f for f in x if len(f) == 4]

# same as my unrefactored but with great commenting
def friend(x):
    myFriends = []                   # Initialize list variable
    for person in x:                 # Loop through list of names 
        if len(person) == 4:         # Check to see if the name is of length 4
            myFriends.append(person) # If the name is 4 characters long, append it to variable myFriends
    return myFriends                 # Return myFriends list

# create a new list filtering only elements of length of 4
def friend(x):
    return list(filter(lambda name: len(name) == 4, x))

# same as above but without an implicit return lambda
def len_4(x):
    return len(x)==4
def friend(x):
    #Code
    return filter(len_4,x)

# enumerate() returns a list of tuples [(index, element), (index, element)]def friend(x):
    res = []
    
    for i, j in enumerate(x):
        if len(j) == 4:
            res.append(j)
            
    return res
