# Decode the Morse code
"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
C#: MorseCode.Get(".--") (returns string)
F#: MorseCode.get ".--" (returns string)
Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no longer used and kept only for old solutions.
Elm: MorseCodes.get : Dict String String
Haskell: morseCodes ! ".--" (Codes are in a Map String String)
Java: MorseCode.get(".--")
Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
Racket: morse-code (a hash table)
Rust: MORSE_CODE
Scala: morseCodes(".--")
Swift: MorseCode[".--"] ?? "" or MorseCode[".--", default: ""]
C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
NASM: a table of pointers to the morsecodes, and a corresponding list of ascii symbols
All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.
"""
# Parameters or Edge Cases:
"""
    inputs will be a string representing Morse code of only '.' and/or '-' characters
    inputs will not be empty
    inputs will vary on white space and must be maintained in the output
"""
# Return:
"""
    a string of equivalent ascii characters of the input string
"""
# Examples:
"""
    '.... . -.--   .--- ..- -.. .' => "HEY JUDE"
        '.-' => 'A'
    '--...' => '7'
    '...-..-' => '$'
    '.' => 'E'
    '..' => 'I'
    '. .' => 'EE'
    '.   .' => 'E E'
    '...-..- ...-..- ...-..-' => '$$$'
    '----- .---- ..--- ---.. ----.' => '01289'
    '.-... ---...   -..-. --...' => '&: /7'
    '...---...' => 'SOS'
    '... --- ...' => 'SOS'
    '...   ---   ...' => 'S O S'
"""
# Pseudocode:
"""
    # declare an empty array
    # iterate through the input split at 3 white spaces creating a 1d array of each morse word sequence
    # grab each individual letter of each word in the current index and pass it through the given MORSE_CODE dictionary then append each value to  
        a local variable called word
    # if word is not empty then append it to the declared array
    # convert the array back into a string with each element divided by a white space
    
"""
# I can't print test cases because the dictionary is local to the kata
# my answer
def decodeMorse(input):
    # declare an empty array 
    result = []
    # iterate through the input split at 3 white spaces creating a 1d array of each morse word sequence
    for morse_word in input.split('   '):
        # grab each individual letter of each word in the current index and pass it through the given MORSE_CODE dictionary then append each value to a local variable called word
        word = ''.join(MORSE_CODE.get(e, '') for e in morse_word.split(' '))
        # if word is not empty then append it to the declared array
        if word:
            result.append(word)
    # convert the array back into a string with each element divided by a white space
    return ' '.join(result)

# best practices and most clever
# I strongly disagree for best practices. 
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))


# similar to my answer but easier to read given variable declarations
def decodeMorse(morse_sequence):
    words = []
    for morse_word in morse_sequence.split('   '):
        word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
        if word:
            words.append(word)
    return ' '.join(words)

# this is an easier to follow example imo given the nested for loops
# a great brute force for loop answer breaking the nested for loop out of one liner from above code
def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    output = ""
    words = morse_code.strip().split("   ")
    for w in words:
        letters = w.split(" ")
        for char in letters:
            output = output + MORSE_CODE[char]
        output += " "
    return output.strip()

# similar to above but when converting to each morse word for the first time they are not adding a white space to split on again
def decodeMorse(morse_code):
    decoded = ''
    words = morse_code.split('   ')
    for word in words:
        letters = word.split()
        for letter in letters:
            decoded += MORSE_CODE[letter]
        decoded += ' '
    return decoded.strip()

# clever to use * in place of 3 white spaces to split on each morse word
def decodeMorse(morseCode):

    morseCode = morseCode.strip().replace("   ", " * ")

    msg = ""
    
    for x in morseCode.split():
        if x != "*":
            msg += MORSE_CODE[x]
        else:
            msg += " "
    
    return msg

# I love this answer because they are splitting each step into it's own function
WORD_DELIMETER = '   '

def decode_morse_character(morse_character):
	return MORSE_CODE.get(morse_character, '')
    
def decode_morse_word(morse_word):
 	return ''.join([
        decode_morse_character(char)
        for char in morse_word.split(' ')
    ])
    
def decodeMorse(morseCode):
    morse_code = morseCode.rstrip().lstrip()
    
    return ' '.join([
        decode_morse_word(word)
        for word in morse_code.split(WORD_DELIMETER)
    ])


# using array methods in nested for loops
def decodeMorse(morseCode):
    CHARS = " "
    WORDS = "   "
    lst = []
    for word in morseCode.strip().split(WORDS):
        wordLst = []
        for character in word.split(CHARS):
            wordLst.append("".join(MORSE_CODE[character]))
        lst.append("".join(wordLst))
    return " ".join(lst)

# this coder found a morse code key value pair to make test cases and call as key value instead of relying on internal MORSE_CODE
MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

def decodeMorse(morseCode):
    return ' '.join([''.join(map(lambda i:MORSE_CODE[i],x.split())) for x in [w for w in morseCode.strip().split('  ')]])