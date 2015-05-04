#!/usr/bin/python

def read_FASTA(input_file):
	
	# Dictionary of sequences. Will be built and then returned.
	sequence_dict = {}
	
	# Variables for holding transitory sequence names and sequences
	current_name = ""
	current_sequence = ""
	
	# With the FASTA file opened:
	with open(input_file, "r") as fasta:
		
		# Read and process each line of input
		for line in fasta:
			
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
				current_name = line.rstrip()[1:]
			
			# If the line is a sequence chunk, add to current sequence
			else:
				current_sequence += line.rstrip()
	
	# Once all lines have been read, set the last dictionary item
	sequence_dict[current_name] = current_sequence
	
	return sequence_dict
