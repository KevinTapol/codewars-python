# Encrypt this!
"""
Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""
# Parameters or Edge Cases:
"""
    inputs will be a string sentence of only letter characters
    inputs can be empty
"""
# Return:
"""
    the input string with each word's first character ascii code and the 2nd character swapped with the last character
"""
# Examples:
"""
    "" => "" 
    "A wise old owl lived in an oak" => "65 119esi 111dl 111lw 108dvei 105n 97n 111ka" 
    "The more he saw the less he spoke" => "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp" 
    "The less he spoke the more he heard" => "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare" 
    "Why can we not all be like that wise old bird" => "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri" 
    "Thank you Piotr for all your help" => "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple" 
"""
# Pseudocode:
"""
    # declare an empty array named result
    # iterate through the input as an array of elements split on white space
    # convert word into an array
    # replace first letter with ascii code
    # if word has more than 2 characters
    # declare e as a variable for index 1 of word
    # declare v as a variable for the index of the last character of word -1
    # reassign the last character of word to the variable representing the character at index 1
    # reassign the character at index 1 to the variable representing the last character of word -1
    # convert the current word into a string and append it to result
    # convert result into a string and return it
    # convert result into a string
    # return result

"""

# # my answer
def encrypt_this(text):
    # declare an empty array named result
    result = []
    # iterate through the input as an array of elements split on white space
    for word in text.split():
        # convert word into an array
        word = list(word) 
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        # if word has more than 2 characters
        if len(word) > 2:
            # declare e as a variable for index 1 of word -1
            e = word[1]
            # declare v as a variable for the index of the last character of word
            v = word[-1]
            # reassign the last character of word to the variable representing the character at index 1
            word[-1] = e
            # reassign the character at index 1 to the variable representing the last character of word -1
            word[1] = v
        # convert the current word into a string and append it to result
        result.append(''.join(word))
    # convert result into a string
    result = ' '.join(result) 
    return result

# my answer refactored 
# one lining the variable declarations for e and v
# one lining the variable reassignments for second and last indexes
# returning result as a string instead of reassigning result as such then returning
def encrypt_this(text):
    result = []
    for word in text.split():
        word = list(word) 
        word[0] = str(ord(word[0]))
        if len(word) > 2:
            e, v = word[1], word[-1]
            word[-1], word[1] = e, v
        result.append(''.join(word))
    return ' '.join(result)


print(encrypt_this("A wise old owl lived in an oak")) # "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
print(encrypt_this("The more he saw the less he spoke")) # "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
print(encrypt_this("The less he spoke the more he heard")) # "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
print(encrypt_this("Why can we not all be like that wise old bird")) # "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
print(encrypt_this("Thank you Piotr for all your help")) # "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"

# best practices
# YOU CAN DO THIS??!! very similar to mine but switching index 1 and last index in one line
# Swapping values of an index in one line instead of overwriting each other with variable assignments.
def encrypt_this(text):
    result = []
    
    for word in text.split():
        # turn word into a list
        word = list(word)
        
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        
        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        
        # add to results
        result.append(''.join(word))
    
    return ' '.join(result)

# most clever
def swapper(w):
    return w if len(w)<2 else w[-1] + w[1:-1] + w[0]

def encrypt_this(s):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())

# regex
import re
def encrypt_this(text):
    return re.sub(r'\b(\w)(\w?)(\w*?)(\w?)\b', lambda m: '{}'.format(str(ord(m.group(1))) + m.group(4) + m.group(3) + m.group(2)), text).replace('   ', ' ').replace('  ', ' ')

# codewars only one liner
encrypt_this=lambda s:' '.join(str(ord(w[0]))+w[-1:]*(w[1:]>'')+w[2:-1]+w[1:2]*(w[2:]>'')for w in s.split())

# more readable breakdown of most clever
def encrypt_word(word):
    result = list(word)
    result[0] = str(ord(result[0]))
    if len(word) > 1:
        result[1], result[-1] = result[-1], result[1]
    return "".join(result)
    
def encrypt_this(text):
    return " ".join(encrypt_word(word) for word in text.split())

# regex and map()
import re
def encrypt_this(text):
    return ' '.join(
        map(lambda w: re.sub('(^.)(.?)(.*?)(.?)$', 
            lambda m: str(ord(m.group(1)))+m.group(4)+m.group(3)+m.group(2), w), 
        text.split())
    )