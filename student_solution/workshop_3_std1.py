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

def readfasta(input_file): # Make sure to add the input
    sequence_dict = {}
    current_name = ""
    current_sequence = ""
    with open(input_file, "r") as fasta:
        for line in fasta:
            stripped_line = line.rstrip()
            if line.startswith(">"):
                if current_name:
                    sequence_dict[current_name] = current_sequence
                    current_sequence = ""
                current_name = stripped_line[1:]
            elif stripped_line:
                current_sequence += stripped_line
    sequence_dict[current_name] = current_sequence
    return sequence_dict # Tell python to do nothing, use when function are
        # empty, change it for a return statement

# Now, using your function, read to new fasta file

input_file = "C:\Users\Travail\Desktop\las17_aligned.fasta"

its_unknow = readfasta(input_file)
# This fasta file containt other character then
# the four nucleic acid. Build a function to remove them
# And use it on its_unknow

import re

def remove_not_nucleicacid(seq_dna):
    seq_dna = re.sub(r"[^ATGC]", "", seq_dna)
    return seq_dna


### Second Exercie:
# During the first workshop, you have caculated
# the GC content, here try to construct a function
# who calculate the GC_content of a list of sequence

its_known_clean = remove_not_nucleicacid(its_unknow.values())

def gc_content(seq):
    length=len(seq)
    g_count = seq.upper().count("G")
    c_count = seq().count("C")
    gc_count= float(g_count + c_count) / length * 100
    return gc_content

### Third exercice
# During the first workshop, you have transcribe
# some sequence, now we will try to translate them

# Complete the two functions below:
# One to transcribe DNA sequence
# One to translate the RNA

def trancription(dna_seq):
    rna_seq = dna_seq.replace("T", "U")
    

import itertools

def translation(rna_seq):
    all_codon = [''.join(x) for x in list(itertools.product(['U','C','A','G'], repeat=3))]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    genetic_code = dict(zip(all_codon, amino_acids))
    prot_seq = ""
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i: (i+3)]
        aa = genetic_code[codon]
        prot_seq = prot_seq + aa
    return prot_seq
        


    ### This code construct a dictionnary to change codon in amino acids
    all_codon = [''.join(x) for x in list(itertools.product(['U','C','A','G'], repeat=3))]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    genetic_code = dict(zip(all_codon, amino_acids))
    # genetic_code['ATG'] will output M (for the methionine amino acid)
    



# Now use your function to translate
# all sequence in its_unknow
# and print the name and the protein sequence

### Supplementaty exercice:
# 1.    Modify transcribe() to output the two possible rna_seq (from each strand)
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

