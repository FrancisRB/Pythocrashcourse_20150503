#!/usr/bin/python


# Code to read the FASTA from workshop 2B
# Written by Lou
# 2015-05-03



# Name of the input fasta file
input_file = "workshop_2B_DNA.fa"

# Dictionary of sequences, to fill while reading the file.
sequence_dict = {}

# Variables to hold transitory sequence names and sequences
current_name = ""
current_sequence = ""

# With the FASTA file opened:
with open(r"C:\Users\Travail\Desktop\workshop_2B_DNA.fa") as fasta:
    
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

import re

with open(r"C:\Users\Travail\Desktop\workshop_2B_table.tsv", "w") as table:
    column_names = [
                    "Name",
                    "PCRstart",
                    "PCRstop",
                    "NumOfFrag",
                    "FragSizes"
                   ]

    header_line = "\t".join(column_names) + "\n"
    table.write(header_line)
    
    for seq_name in sorted(sequence_dict.keys()):
        pcr = sequence_dict[seq_name]
        name = re.search(r"seq[A-Z]", seq_name)
        position_pcr = re.search(r"\d+-\d+", seq_name)
        position_pcr = position_pcr.group().split("-")
        
        frag=pcr[(position_pcr[0]-1):(position_pcr[1]-1)]
        
        # Pour couper les fragments amplifiés
        frag=re.search(r"GT[A|C][G|T]AC", frag)
         

#### COrrigé à Lou
# .gruop(1) signifie qu'il sélection que le premier élément défini.
# Codon stop: diminue de 1 à cause du cadre du logiciel et augmenter de 1
# à cause de nombre, pour tout sélectionner.
# [AT] signifie soit A ou T équivalent à (A\T)     
       
       
       seq_len = len(seq)

        # g content and c content
        g = seq.count("G")
        c = seq.count("C")
        seq_gc = 100 * float(g + c) / seq_len

        seq_contains_atg = "ATG" in seq

        row_info = [seq_name,
                    str(seq_len),
                    str(seq_gc),
                    str(seq_contains_atg)
                   ]

        table_line = "\t".join(row_info) + "\n"
        table.write(table_line)

