"""
Workshop3:

Work on fonction

How to create fonction

Author: Francis RB

"""

import itertools

# Previously you have write code to read fasta
# You would probably have to reuse this code often
# So it's a good idea to be able to acces it easily
# A good way to do it, it to create a function

### First Exercice:
# Transform your script to read a fasta in a function

def readfasta(): # Make sure to add the input
    pass # Tell python to do nothing, use when function are
        # empty, change it for a return statement

# Now, using your function, read to new fasta file

input_file = ""

its_unknow = readfasta(input_file)

# This fasta file containt other character then
# the four nucleic acid. Build a function to remove them
# And use it on its_unknow

def remove_not_na():
    pass

### Second Exercie:
# During the first workshop, you have caculated
# the GC content, here try to construct a function
# who calculate the GC_content of a list of sequence

def gc_content(seq_list):
    pass

### Third exercice
# During the first workshop, you have transcribe
# some sequence, now we will try to translate them

# Complete the two functions below:
# One to transcribe DNA sequence
# One to translate the RNA

def trancription(dna_seq):
    pass

def translation(rna_seq):

    ### This code construct a dictionnary to change codon in amino acids
    all_codon = [''.join(x) for x in list(itertools.product(['U','C','A','G'], repeat=3))]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    genetic_code = dict(zip(all_codon, amino_acids))
    # genetic_code['ATG'] will output M (for the methionine amino acid)
    
    pass

# Now use your function to translate
# all sequence in its_unknow
# and print the name and the protein sequence

### Supplementaty exercice:
# 1.    Modify transcribe() to output the two possible rna_seq (from each strain)
#       and modify transcribe() to take both rna sequence
# 2.    Modify translation() to only start at ATG and end on stop codon
#       And to ouput all possible protein if there is no stop codon,
#       the function as to discard the protein sequence
# 3.    Contruct a dictionnary containing all possible protein
#       for every DNA sequence in its_unknow

def adv_transcribe():
    pass

def adv_translate():
    pass

