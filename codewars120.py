# Your order, please
# Parameters or Edge Cases:
    # inputs will be a string sentence with each word containing a positive integer from 1-9
    # the string can be empty
    # will it always start with 1 and increase by 1? meaning will there ever be a jump in step like 1 to 3 instead of 1 to 2 to 3?
# Return:
    # an empty string if the input is empty else the sentence with each word reordered by the integer value contained in each word of the input
# Examples:
    # "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
    # "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    # ""  -->  ""
# Pseudocode:
    # declare an empty string named result to later become a list of integers from the inputs
    # declare an empty string named answer to become the final string answer
    # split the input string into an array by white space
    # iterate through the array with a for loop in range of the length of the array
    # grab the element that returns true to isnumeric() and concat it to string result
    # convert result into an array of integers
    # create an object out of the 2 list with ints being the key and strings being the value at matching indexes dict(zip(list_of_keys, list_of_values))
    # iterate through the object starting at 1 and concatenating it to an empty string and a white space
    # iterate through the object starting at 1 and concatenating it to the empty string answer with a white space
    # remove the last white space from the answer .strip() or [:-1]
    # return the string answer

# my answer
def order(sentence):
    answer = ""
    # declare an empty string named result
    result = ""
    # split the input string into an array by white space
    s = sentence.split()
    # iterate through the array with a for loop in range of the length of the array
    for i in range(len(s)):
    # grab the element that returns true to isnumeric() and concat it to string result
        for e in s[i]:
            if e.isnumeric() == True:
                result += e
    # convert result into an array of integers
    result = [int(e) for e in result]
    # create an object out of the 2 list with ints being the key and strings being the value at matching indexes dict(zip(list_of_keys, list_of_values))
    x = dict(zip(result, s))
    # iterate through the object starting at 1 and concatenating it to the empty string answer with a white space
    for i in range(len(x)):
        answer += x[i+1] + " "
    # remove the last white space from the answer
    answer = answer.strip()
    # return the new string
    return answer

# my answer refactored
def order(sentence):
    result = ""
    nums = ""
    words = sentence.split()
    for i in range(len(words)):
        for e in words[i]:
            if e.isnumeric() == True:
                nums += e
    nums = [int(e) for e in nums]
    d = dict(zip(nums, words))
    for i in range(len(d)):
        result += d[i+1] + " "
    result = result[:-1]
    return result

print(order("is2 Thi1s T4est 3a")) # "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2")) # "Fo1r the2 g3ood 4of th5e pe6ople"
print(order("")) # ""

# best practices
# sorted() on each word brings the string number first up front ie sorted(word1) returns 1word
# converting the input into an array of element words then sorting with the key of sorted words which would be the string number in each word since ascii characters come before ascii letters
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# shorter answer of best practices using key=min
# key=min --> The 'lowest value' character in each string (word) is returned. In this context, numbers (0-9) are considered as smaller than letters (a-z)
def order(sentence):
  return " ".join(sorted(sentence.split(), key=min))

# same idea of best practices but declaring another function internally
def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))

# way better answer than my brute force for loop
# nested for loop to append to an empty array the result of string(index) start 1 stop 10 step 1 (stop 10 is exclusive so it would return 9)
def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our sentence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)

# creating a class Word and importing regex but following closely to best practices of array sorted() by key=sorted(word)
import re


class Word(object):

    digit_regex = re.compile(r'[0-9]')

    def __init__(self, word):
        self._index = self.digit_regex.findall(word)[0]
        self._word = word
    
    def __repr__(self):
        return self._word
    
    @property
    def word(self):
        return self._word
    
    @property
    def index(self):
        return self._index


class Sentence(object):
  
    def __init__(self, words):
        self._words = words
    
    def __repr__(self):
        return ' '.join([str(x) for x in self.ordered()])
    
    def ordered(self):
        return sorted(self._words, key=lambda word: word.index)

def order(sentence):
  return str(Sentence(map(Word, sentence.split())))

# iterating through using isdigit() and then sorting the array by sorted key= to the digit
def order(sentence):
    def sort_key(s):
        return next(c for c in s if c.isdigit())
    return ' '.join(sorted(sentence.split(), key=sort_key))

# creating a 2d and sorting on the integer in the word of the sorted 2d array then converting it back into a string sentence
def order(sentence):
    data = sentence.split()

    result = []

    for word in data:
        for letter in word:
            if letter.isdigit():
                result.append([int(letter), word])

    return " ".join([x[1] for x in sorted(result)])

# copy() method returns a copy of the specified list
# is this better than using [:] ?
# nested for loop with a conditional for each letter in each word of the array assign the word to the array copy
def order(sentence):
    ordered = sentence.split()
    for x in ordered.copy():
        for y in x:
            if y.isdigit():
                ordered[int(y)-1] = x
    return " ".join(ordered)

# while loop using regex iterating through to find all digits and concatenating to an empty string based on for loop 1-10 10 being excluded
import re
def order(sentence):
  string_final = ''
  if sentence == '':
    return sentence
  lista = sentence.split()
  posicao=1
  while posicao <= len(lista):
    for i in range(len(lista)):
      if re.findall('\d+', lista[i]) == [str(posicao)]:
        string_final = string_final + lista[i] + ' '
        break
    posicao+=1
  return string_final[:-1]

# full codewars brain
# sorting a created array of words based on the key = integer element in the string of the first index
def order(sentence):
    return ' '.join(sorted([x for x in sentence.split()], key=lambda x: [int(n) for n in x if n.isdigit()][0]))