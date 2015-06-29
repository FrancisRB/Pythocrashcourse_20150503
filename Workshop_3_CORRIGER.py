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

    # Dictionary of sequences, to fill while reading the file.
    sequence_dict = {}

    # Variables to hold transitory sequence names and sequences
    current_name = ""
    current_sequence = ""

    # With the FASTA file opened:
    with open(input_file, "r") as fasta:

        # Read and process each line of input
        for line in fasta:

            # Strip the trailing newline character
            stripped_line = line.rstrip()

            # If the line is the first of a new entry:
            if line.startswith(">"):

                # If this entry is not the first of the file:
                if current_name:

                    # Then the previous entry has been read entirely.
                    # Make a dict. item from current name and sequence.
                    sequence_dict[current_name] = current_sequence

                    # Reset current sequence
                    current_sequence = ""

                # Change current name to the new sequence name
                current_name = stripped_line[1:]

            # If the line is a sequence chunk, add to current sequence
            elif stripped_line:
                current_sequence += stripped_line

        # Once all lines have been read, set the last dictionary item
        sequence_dict[current_name] = current_sequence
            
        return sequence_dict

# Now, using your function, read to new fasta file

input_file = "C:\Users\USER\Desktop\ITS.fas"

its_unknow = readfasta(input_file)

# This fasta file containt other character then
# the four nucleic acid. Build a function to remove them
# And use it on its_unknow

def remove_not_na(dict_sequence):

    for key, val in dict_sequence.items():
        dict_sequence[key] = ''.join([x for x in dict_sequence[key]
                                      if x in ['A','C','T','G']])

    return dist_sequence

def remove_not_nucleicacid(dict_sequence):

    return {key: ''.join([x for x in dict_sequence[key]
                                      if x in ['A','C','T','G']])
            for key, val in dict_sequence.items()}


### Second Exercice:
# During the first workshop, you have calculated
# the GC content, here try to construct a function
# who calculate the GC_content of a list of sequence

def gc_content(seq_list):

    gc_content_list = []

    for seq in seq_list:
        gc_quantity = seq.count('G') + seq.count('C')
        lenght_seq = len(seq)
        gc_ratio = gc_quantity/float(lenght_seq)
        gc_content_list.append(gc_ratio)

    return gc_content_list

    # or

def gc_content(seq_list):

    return [(seq.count('G')+ seq.count('C'))/float(len(seq)) for seq in seq_list]

# Calculate the GC content of each sequence of its_unknow

its_gc_content = gc_content(its_unknow.values())

print its_gc_content

### Third exercice
# During the first workshop, you have transcribe
# some sequence, now we will try to translate them

# Complete the two functions below:
# One to transcribe DNA sequence
# One to translate the RNA

def trancription(dna_seq):
    return dna_seq.replace('A', 'U').replace('T','A').replace('G','g').replace('C','G').replace('g','C').replace('N', '').replace('-', '')[::-1]

    # or

def transcription(dna_seq):

    correspondance = ["Au", "Ta", "Cg", "Gc"]
    dna_seq = dna_seq.replace('N', '').replace('-', '')
    seq = dna_seq[:] # A form of copy in Python

    for c in correspondance:
        seq = seq.replace(c[0], c[1])

    seq = seq[::-1].upper()

    return seq

    # or

def transcription(dna_seq):

    rna_seq = []

    for an in dna_seq[::-1]:
        if an == 'A':
            rna_seq.append('U')
        elif an == 'T':
            rna_seq.append('A')
        elif an == 'C':
            rna_seq.append('G')
        elif an == 'G':
            rna_seq.append('C')

    ans =  ''.join(rna_seq)

    return ans


def translation(rna_seq):

    ### This code construct a dictionnary to change codon in amino acids
    all_codon = [''.join(x) for x in list(itertools.product(['U','C','A','G'], repeat=3))]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    genetic_code = dict(zip(all_codon, amino_acids))
    # genetic_code['ATG'] will output M (for the methionine amino acid)

    protein = ''
    for i in range(len(rna_seq)/3):
        codon = rna_seq[i*3:(i+1)*3]
        aa = genetic_code[codon]
        protein += aa    

    return protein
  

# Now use your function to translate
# all sequence in its_unknow
# and print the name and the protein sequence

for name, seq in its_unknow.items():
    print name
    print translation(transcription(seq))

### Supplementaty exercice:
# 1.    Modify transcribe to output the two possible rna_seq (from each strain)
#       and modify transcribe to take both rna sequence
# 2.    Modify translation to only start at ATG and end on stop codon
#       And to ouput all possible protein if there is no stop codon,
#       the function as to discard the protein sequence
# 3.    Contruct a dictionnary containing all possible protein
#       for every DNA sequence in its_unknow

def adv_transcribe(dna_seq):

    correspondance = ["Au", "Ta", "Cg", "Gc"]
    dna_seq = dna_seq.replace('N', '').replace('-', '')
    forward_seq = dna_seq[:] # A form of copy in Python
    lagging_strain = dna_seq[:]

    for c in correspondance:
        forward_seq = forward_seq.replace(c[0], c[1])

    forward_seq = forward_seq[::-1].upper()

    lagging_strain = lagging_strain.replace('T','U')

    return forward_seq, lagging_strain

def adv_translate(rna_seq_list):

    ### This code construct a dictionnary to change codon in amino acids
    all_codon = [''.join(x) for x in list(itertools.product(['U','C','A','G'], repeat=3))]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    genetic_code = dict(zip(all_codon, amino_acids))
    # genetic_code['ATG'] will output M (for the methionine amino acid)

    print rna_seq_list

    def find_start_codon(rna_seq, pattern='AUG'):
    
        codon_occurence = [i for i, a in enumerate(rna_seq)
                           if rna_seq[i:i+3] == pattern]

    def single_translate(rna_seq, start):

        ORF  = [rna_seq[i:i+3] for i in range(start, len(rna_seq), 3)]
        good_orf = [codon for codon in ORF if len(codon) == 3]
        peptide = ''.join([genetic_code[codon] for codon in good_orf])
        if '*' in peptide:
            return peptide.partition('*')[0]
        else:
            return None
    
    return [single_translate(rna, start_codon)
            for rna in rna_seq_list
            for start_codon in find_start_codon(rna)]

all_protein_its = {key:adv_translate(adv_transcribe(val))
                   for key, val in its_unknow.items()}
