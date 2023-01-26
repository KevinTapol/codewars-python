# Rock Paper Scissors
# Parameters or Edge Cases:
    # given 2 inputs player1 and player2
    # inputs will be string "scissors", "paper", or "rock"
    # input strings will be lowercase
# Return:
    # "Player 1 won", Player 2 won" or "Draw"
# Examples:
    # "scissors", "paper" --> "Player 1 won!"
    # "scissors", "rock" --> "Player 2 won!"
    # "paper", "paper" --> "Draw!"
# Psuedo Code:
    # if p1 and p2 are equal return "Draw"
    # if p1 is "rock" and p2 is "scissors" return "Player 1 won!"
    # if p1 is "scissors" and p2 is "paper" return "Player 1 won!"
    # if p1 is "paper" and p2 is "rock" return "Player 1 won!"
    # else return "Player 2 won"

# my answer
def rps(p1, p2):
    # if p1 and p2 are equal return "Draw"
    if p1 == p2:
        return "Draw!"
    # if p1 is "rock" and p2 is "scissors" return "Player 1 won!"
    if p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    # if p1 is "scissors" and p2 is "paper" return "Player 1 won!"
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    # if p1 is "paper" and p2 is "rock" return "Player 1 won!"
    if p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    # else return "Player 2 won"
    else:
        return "Player 2 won!"
    
# my answer refactored one liner implicit return conditionals
rps = lambda p1, p2: "Draw!" if p1 == p2 else "Player 1 won!" if p1 == "rock" and p2 == "scissors" else "Player 1 won!" if p1 == "scissors" and p2 == "paper" else "Player 1 won!" if p1 == "paper" and p2 == "rock" else "Player 2 won!"

# my answer refactored one liner implicit with and or 
rps = lambda p1, p2: "Draw!" if p1 == p2 else "Player 1 won!" if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") else "Player 2 won!"

print(rps('rock', 'scissors')) # "Player 1 won!"
print(rps('scissors', 'rock')) # "Player 2 won!"
print(rps('rock', 'rock')) # "Draw"

# best practices
# using dictionary/object with key winning over value statements and call the key for the player win else draw
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

# most clever
# using dictionary/object with tuple/array index call for win
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

# using 3 conditions similar to my refactored
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
    
# tuple with nested list and .format()
def rps(p1, p2):
    d1 = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]
    return 'Draw!' if p1 == p2 else "Player {} won!".format(1 if (p1, p2) in d1 else 2)

# all of the logic in the dictionary/object and call the key which contains p1 and p2
RPS = {('rock', 'rock'): 'Draw!',
       ('rock', 'paper'): 'Player 2 won!',
       ('rock', 'scissors'): 'Player 1 won!',
       ('paper', 'rock'): 'Player 1 won!',
       ('paper', 'paper'): 'Draw!',
       ('paper', 'scissors'): 'Player 2 won!',
       ('scissors', 'rock'): 'Player 2 won!',
       ('scissors', 'paper'): 'Player 1 won!',
       ('scissors', 'scissors'): 'Draw!'}


def rps(p1, p2):
    return RPS[(p1, p2)]

# one liner implicit return lambda tuple for win and tuple with nested lists for logic
rps = lambda a, b: ['Draw!', 'Player 1 won!', 'Player 2 won!'][('srp'.index(a[0]) - 'srp'.index(b[0])) % 3]

# declaring the tuples as variables
def rps(p1, p2):
    options = ["rock", "paper", "scissors"]
    outcomes = ["Draw!", "Player 1 won!", "Player 2 won!"]
    return outcomes[options.index(p1) - options.index(p2)]

# interesting concatenating the inputs for condition checks
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 + p2 in ('rockscissors', 'paperrock', 'scissorspaper'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
    
# using f string
def rps(p1, p2):
    order = "rock scissors paper rock"
    return ( "Player 1 won!" if f"{p1} {p2}" in order
        else "Player 2 won!" if f"{p2} {p1}" in order
        else "Draw!" )

# wow lambda with f string p1 win then not win for r s p r for input in string representation
rps=lambda x,y:['Draw!',f'Player {(y[0]+x[0]in"rspr")+1} won!'][x!=y]

# interesting nested lambdas in a return statement 
def rps(p1, p2, w = {'scissors':'paper', 'paper':'rock', 'rock':'scissors'}):
    return {False:lambda:f"Player {(w[p1]!=p2)+1} won!", True: lambda:'Draw!'}[p1==p2]()