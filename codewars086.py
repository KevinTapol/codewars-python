# Complementary DNA
# Parameters or Edge Cases:
    # inputs will be a random string of multiple capital letters 'ATGC'
    # inputs will not be empty or null
# Return:
    # the input string replacing every 'A' with 'T', every 'T' with 'A', every 'G' with 'C' and every 'C' with 'G'
# Examples:
    # "ATTGC" --> "TAACG"
    # "GTAT" --> "CATA"
# Pseudo Code:
    # declare an empty array
    # iterate through the input string and append each element 'A' with 'T', 'T' with 'A', 'C' with 'G' and 'G' with 'C'
    # convert the array into a string and return it

# my answer brute force 
def DNA_strand(dna):
    s = []
    for index in range(len(dna)):
        if dna[index] == 'A':
            s.append('T')
        elif dna[index] == 'T':
            s.append('A')
        elif dna[index] == 'C':
            s.append('G')
        elif dna[index] == 'G':
            s.append('C')
            
    return "".join(s)

# my answer refactored using dict
def DNA_strand(dna):
    t = ""
    s = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for e in s[dna]:
        t += e
    return t

# my dictionary answer refactored implicit return
DNA_strand = lambda dna: "".join({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[e] for e in dna)

print(DNA_strand("ATTGC")) # "TAACG"
print(DNA_strand("GTAT")) # "CATA"

# best practices and most clever DEPRECATED!!!!!!!
# importing string to use .maketrans(what to replace, what replacing with)
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC")

# working version of best practices and most clever
def DNA_strand(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))

# also using a dictionary
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

# math with index for each element in dna call on 'ACGT'
DNA_strand = lambda dna: ''.join(['ACGT'[-1 * ('ACGT'.index(l) + 1)] for l in dna])

# while loop
def DNA_strand(dna):
    i = 0
    dna2 = ""
    while len(dna) > i: #loop till hit the end of last index exclusively
        if dna[i] == "A":
            dna2 = dna2 + "T"
        elif dna[i] == "T":
           dna2 = dna2 + "A"
        elif dna[i] == "G":
            dna2 = dna2 + "C"
        else:
            dna2 = dna2 + "G"
        i += 1
    return dna2

# very clever to take advantage of all inputs being uppercase
# this way you can re iterate through the string multiple times and not replace what you just replaced
def DNA_strand(dna):
    return dna.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
