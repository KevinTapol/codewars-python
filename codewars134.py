# Highest Scoring Word
"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
# Parameters or Edge Cases:
"""
    # All letters will be lowercase and all inputs will be valid.
"""
# Return:
"""
    # You need to return the highest scoring word as a string. If two words score the same, return the word that appears earliest in the original string.
"""
# Examples:
"""
    # 'man i need a taxi up to ubud' => 'taxi'
    # 'what time are we climbing up the volcano' => 'volcano'
    # 'take me to semynak' => 'semynak'
    # 'aa b' => 'aa'
    # 'b aa' => 'b'
    # 'bb d' => 'bb'
    # 'd bb' => 'd'
    # "aaa b" => "aaa"
"""
# Pseudocode:
"""
    # declare an empty array for score values named values
    # using ord('a') returns unicode 97 subtract 96 from each character when calculating score
    # take in the input string and split on white space making an array of strings of words
    # for each word convert it into an array of unicode values -96 using ord()
    # sum the word values and push it to the values array
    # create a dictionary/object of the arrays using dict(zip(words,values))
    # find the max value in the object and return the word which is in the key in the key value pair 
    
"""
# my answer
def high(input):
    # declare an empty array for score values named values
    values = []
    # using ord('a') returns unicode 97 subtract 96 from each character when calculating score
    # take in the input string and split on white space making an array of strings of words
    all_words = input.split()
    # for each word convert it into an array of unicode values -96 using ord()
    for word in all_words:
            x = [ord(e)-96 for e in word]
    # sum the word values and push it to the values array
            values.append(sum(x))
    # create a list of tuples where the value is index 0 and the word is index 1
    list_of_tuples = list(zip(values,all_words))
    # declare an empty array to push every instance of the max value at index 0 of the list list_of_tuples
    result = []
    # iterate through list_of_tuples the list of tuples and for each tuple if the first index is equal to the max value append that tuples index 1 to result
    for e in list_of_tuples:
          if e[0]== max(list_of_tuples)[0]:
                result.append(e[1])
    # return the first index of the list of letters of max values            
    return result[0]

# my answer refactored
def high(input):
    all_words = input.split()
    values = [sum([ord(e)-96 for e in word]) for word in all_words ]
    list_of_tuples = list(zip(values,all_words))
    return [e[1] for e in list_of_tuples if e[0]== max(list_of_tuples)[0]][0]    

# my answer refactored throwing the list values into zip() for the index0 tuple  for list of tuples
def high(input):
    all_words = input.split()
    list_of_tuples = list(zip([sum([ord(e)-96 for e in word]) for word in all_words ],all_words))
    return [e[1] for e in list_of_tuples if e[0]== max(list_of_tuples)[0]][0]         

print(high('man i need a taxi up to ubud')) # 'taxi'
print(high('what time are we climbing up the volcano')) # 'volcano'
print(high('take me to semynak')) # 'semynak'
print(high('aa b')) # "aa"
print(high('b aa')) # 'b'
print(high('bb d')) # 'bb'
print(high('d bb')) # 'd'
print(high("aaa b")) # "aaa"

# best practices and most clever
# here they are using the 2nd argument of max() for the key being an implicit return function of the sum of unicode values - 96 on each letter for each word in the input per element list
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# very similar to my answer in that making a list of values and a list of words
# Then calling the words index where the values list index contains the max value of the list of values
def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]

# wow... I should have though of this
# declaring a highest value and setting it to 0
# loop through and compare the value of each word and if the value of the word is greater and not equal than the value of the previous word, set it equal to highest value
def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word

# creating an array of each letter and referencing the index + 1 for value
# here they are using the same idea as declare the highest score and first occurrence of it as you loop through the list of words by value
def high(x):
    scoreboard=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    heck = x.split()
    score=0
    score_final=0
    big_word=[]
    for each in heck:
        print(each)
        for every in each:
            if every in scoreboard:
                score= score + scoreboard.index(every) + 1
                print(score)
        if score > score_final:
            score_final = score
            big_word = each
            score = 0
        else:
            score = 0
    return big_word
    # Code here 54
    
    #for every in word: if every in scoreboard, score + every.index()

# same answer as best practices and most clever but using .lower() to assure the input is only lowercase characters
def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))

# creating a dictionary of key value pairs for letters and their values
# creating a separate function to get the values and another to compare
def xx(m):
    a = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
             'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    n = 0
    for i in m:
        n += a[i]
    return n

def high(x):    
    x = x.split()
    m,n = x[0],xx(x[0])
    for i in x[1:]:
        if xx(i) > n:
            m = i
            n = xx(i)
    return m

# here they have a list of a nested for loop returning as n for each value of each word then returning the occurrence of the max values of index of the list of words
def high(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    return s[n.index(max(n))]

# same idea as best practices and most clever but using ascii_lowercase to reference the alphabet characters
import string

def high(x):
    return max(x.split(), key=lambda k: sum(string.ascii_lowercase.index(l)+1 for l in k))

# same nested for loop of comparing values but clean variable declarations
def high(x):

    arr = x.split()
    
    high_score = 0
    winner =''

    for i in arr:
        sum = 0

        for j in i:
            sum += (ord(j)- 96)
            if sum>high_score:
                high_score = sum
                winner=i


    return(winner)

# same idea as best practices of max() 2nd argument
# clever to set a random character to index 0 so you can start the alphabet at index 1
get_score = "_abcdefghijklmnopqrstuvwxyz".index


def high(stg):
    return max(stg.split(), key=lambda word: sum(get_score(c) for c in word))