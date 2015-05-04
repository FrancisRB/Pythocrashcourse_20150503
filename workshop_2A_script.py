#!/usr/bin/python


# Solution to workshop 2A
# Written by Lou
# 2015-04-30



### First step : reading the fasta file

# Name of the input fasta file
input_file = "workshop_2A_DNA.fa"

# Dictionary of sequences, to fill while reading the file.
sequence_dict = {}

# Variable to hold each sequence name consecutively
current_name = ""

# With the fasta file opened in reading mode:
with open(input_file, "r") as fasta:
	
	# For each line of input:
	for line in fasta:
		
		# Strip the trailing newline character
		stripped_line = line.rstrip()
		
		# If the line is a sequence name:
		if line.startswith(">"):
			
			# Change the current name to the new sequence name
			current_name = stripped_line[1:]
		
		# If the line is a sequence, create a dictionary item from the
		# current name and sequence
		elif stripped_line:
			sequence_dict[current_name] = stripped_line



### Second step : writing the table

# Name of the table file
output_file = "workshop_2A_table.tsv"

# With the output file opened in writing mode:
with open(output_file, "w") as table:
	
	# List of column names for the table
	column_names = ["Name", "Length", "GC_content", "Contains_ATG"]
	
	# Turn the list into a header line
	header_line = "\t".join(column_names) + "\n"
	
	# Write the header in the output file
	table.write(header_line)
	
	# For each sequence name in alphabetical order:
	for seq_name in sorted(sequence_dict.keys()):
		
		# The associated sequence
		seq = sequence_dict[seq_name]
		
		# Length, GC content and presence of "ATG" in the sequence
		seq_length = len(seq)
		seq_gc = 100 * float(seq.count("G") + seq.count("C")) / len(seq)
		seq_contains_atg = "ATG" in seq
		
		# List of infos to write as a line of the table
		row_info = [seq_name, seq_length, seq_gc, seq_contains_atg]
		
		# Turn the list in a line of tab-separated values
		table_line = "\t".join(str(info) for info in row_info) + "\n"
		
		# Write the line in the output file
		table.write(table_line)





# BONUS CODE
#
# Reading fasta files with sequences on multiple lines

if False:
	
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
