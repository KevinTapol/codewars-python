"""
DNA to RNA Conversion
Parameters or Edge Cases:
    inpput strings will consist only of "GCAT"
Return:
    an input string converting string "T" to "U"
Examples:
    "GCAT"  =>  "GCAU"
        (dna_to_rna("TTTT"), "UUUU")
        (dna_to_rna("GCAT"), "GCAU")
        (dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")
Psuedo Code:
    take in the input string and replace all "T" with "U"
"""
# my answer best practices and most clever
def dna_to_rna(dna):
    # take in the input string and replace all "T" with "U"
    return dna.replace("T", "U")

# my answer refactored to lambda one liner
dna_to_rna = lambda dna: dna.replace("T", "U")

print(dna_to_rna("TTTT")) # "UUUU"
print(dna_to_rna("GCAT")) # "GCAU"
print(dna_to_rna("GACCGCCGCC")) # "GACCGCCGCC"

# for looping through the string and for each element c if it is "T" set it equal to "U"
def DNAtoRNA(dna):
    return "".join(["U" if c=="T" else c for c in dna])

# here they created a dictionary declared an empty array and appended the empty array with the values of the key for each element in the input
dna_dict = {
    'T': 'U',
    'A': 'A',
    'C': 'C',
    'G': 'G'
}

def DNAtoRNA(dna):
    rna = []
    for letter in dna:
        rna.append(dna_dict[letter])
    return "".join(rna)

# same idea as above dictionary calling the value of given key input for each element in input string
def DNAtoRNA(dna):
    return "".join([{"A": "A", "C": "C", "G": "G", "T": "U"}[b]for b in dna])

# one line lambda of above
dna_to_rna = lambda dna: "".join([{"A": "A", "C": "C", "G": "G", "T": "U"}[b]for b in dna])

# split the string on "T" creating an array then join on "U" converting back to a string
def DNAtoRNA(dna):
    return "U".join(dna.split("T"))

# declare an empty string and a var loop through the input string and for each element i if it is "T" then concat the empty string with "U" else concat the empty string with the element
def DNAtoRNA(dna):
    RNA= ""
    i = 0
    for i in dna:
        if i == "T":
            RNA = RNA + "U"
        else:
            RNA = RNA + i
    return RNA

# Python regex method .sub() replace "T" with "U" in input dna
import re
def DNAtoRNA(dna):
    # create a function which returns an RNA sequence from the given DNA sequence
    return re.sub('T', 'U', dna)

# translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# maketrans() method is used to create a mapping table.
def DNAtoRNA(dna):
    return dna.translate(dna.maketrans("T", "U"))

# similar to above but mapping every possible input string constraint and in a one line lambda
dna_to_rna = lambda dna:dna.translate(str.maketrans("GCAT","GCAU"))