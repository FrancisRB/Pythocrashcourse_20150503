#! -*- coding: utf-8 -*-

"""
Workshop 1

The basic objects and their build-ins methods

Author: Francis RB

"""

### First Exercice:
# Assign a variable to each of these sequences:

    # RNA 16S of E.coli:
    
GCAGAGAAAGCAAAAATAAATGCTTGACTCTGTAGCGGGAAGGCGTATTATGCACACCCCGCGCCGCTGA
GAAAAAGCGAAGCGGCACTGCTCTTTAACAATTTATCAGACAATCTGTGTGGGCACTCGAAGATACGGAT
TCTTAACGTCGCAAGACGAAAAATGAATACCAAGTCTCAAGAGTGAACACGTAATTCATTACGAAGTTTA
ATTCTTTGAGCGTCAAACTTTTAAATTGAAGAGTTTGATCATGGCTCAGATTGAACGCTGGCGGCAGGCC
TAACACATGCAAGTCGAACGGTAACAGGAAGAAGCTTGCTTCTTTGCTGACGAGTGGCGGACGGGTGAGT
AATGTCTGGGAAACTGCCTGATGGAGGGGGATAACTACTGGAAACGGTAGCTAATACCGCATAACGTCGC
AAGACCAAAGAGGGGGACCTTCGGGCCTCTTGCCATCGGATGTGCCCAGATGGGATTAGCTAGTAGGTGG
GGTAACGGCTCACCTAGGCGACGATCCCTAGCTGGTCTGAGAGGATGACCAGCCACACTGGAACTGAGAC
ACGGTCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCAGCCAT
GCCGCGTGTATGAAGAAGGCCTTCGGGTTGTAAAGTACTTTCAGCGGGGAGGAAGGGAGTAAAGTTAATA
CCTTTGCTCATTGACGTTACCCGCAGAAGAAGCACCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGG
AGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCGGTTTGTTAAGTCAGATGTGAA
ATCCCCGGGCTCAACCTGGGAACTGCATCTGATACTGGCAAGCTTGAGTCTCGTAGAGGGGGGTAGAATT
CCAGGTGTAGCGGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCCCTGGACGAAG
ACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACG
ATGTCGACTTGGAGGTTGTGCCCTTGAGGCGTGGCTTCCGGAGCTAACGCGTTAAGTCGACCGCCTGGGG
AGTACGGCCGCAAGGTTAAAACTCAAATGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTA
ATTCGATGCAACGCGAAGAACCTTACCTGGTCTTGACATCCACGGAAGTTTTCAGAGATGAGAATGTGCC
TTCGGGAACCGTGAGACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTTGTGAAATGTTGGGTTAAGTCCC
GCAACGAGCGCAACCCTTATCCTTTGTTGCCAGCGGTCCGGCCGGGAACTCAAAGGAGACTGCCAGTGAT
AAACTGGAGGAAGGTGGGGATGACGTCAAGTCATCATGGCCCTTACGACCAGGGCTACACACGTGCTACA
ATGGCGCATACAAAGAGAAGCGACCTCGCGAGAGCAAGCGGACCTCATAAAGTGCGTCGTAGTCCGGATT
GGAGTCTGCAACTCGACTCCATGAAGTCGGAATCGCTAGTAATCGTGGATCAGAATGCCACGGTGAATAC
GTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTGGGTTGCAAAAGAAGTAGGTAGCTTAAC
CTTCGGGAGGGCGCTTACCACTTTGTGATTCATGACTGGGGTGAAGTCGTAACAAGGTAACCGTAGGGGA
ACCTGCGGTTGGATCACCTCCTTACCTTAAAGAAGCGTACTTTGTAGTGCTCACACAGATTGTCTGATAG
AAAGTGAAAAGCAAGGCGTTTACGCGTTGGGAGTGAGGCTGAAGAGAATAAGGCCGTTCGCTTTCTATTA
ATGAAAGCTCACCCTACACGAAAATATCACGCAACGCGTGATAAGCAATTTTCGTGTCCCCTTCGTCTAG
AGGCCCAGGACACCGCCCTTTCACGGCGGTAACAGGGGTTCGAA

    # 18s RNA of S. cerevesiae:

TATCTGGTTGATCCTGCCAGTAGTCATATGCTTGTCTCAAAGATTAAGCCATGCATGTCT
AAGTATAAGCAATTTATACAGTGAAACTGCGAATGGCTCATTAAATCAGTTATCGTTTAT
TTGATAGTTCCTTTACTACATGGTATAACTGTGGTAATTCTAGAGCTAATACATGCTTAA
AATCTCGACCCTTTGGAAGAGATGTATTTATTAGATAAAAAATCAATGTCTTCGGACTCT
TTGATGATTCATAATAACTTTTCGAATCGCATGGCCTTGTGCTGGCGATGGTTCATTCAA
ATTTCTGCCCTATCAACTTTCGATGGTAGGATAGTGGCCTACCATGGTTTCAACGGGTAA
CGGGGAATAAGGGTTCGATTCCGGAGAGGGAGCCTGAGAAACGGCTACCACATCCAAGGA
AGGCAGCAGGCGCGCAAATTACCCAATCCTAATTCAGGGAGGTAGTGACAATAAATAACG
ATACAGGGCCCATTCGGGTCTTGTAATTGGAATGAGTACAATGTAAATACCTTAACGAGG
AACAATTGGAGGGCAAGTCTGGTGCCAGCAGCCGCGGTAATTCCAGCTCCAATAGCGTAT
ATTAAAGTTGTTGCAGTTAAAAAGCTCGTAGTTGAACTTTGGGCCCGGTTGGCCGGTCCG
ATTTTTTCGTGTACTGGATTTCCAACGGGGCCTTTCCTTCTGGCTAACCTTGAGTCCTTG
TGGCTCTTGGCGAACCAGGACTTTTACTTTGAAAAAATTAGAGTGTTCAAAGCAGGCGTA
TTGCTCGAATATATTAGCATGGAATAATAGAATAGGACGTTTGGTTCTATTTTGTTGGTT
TCTAGGACCATCGTAATGATTAATAGGGACGGTCGGGGGCATCAGTATTCAATTGTCAGA
GGTGAAATTCTTGGATTTATTGAAGACTAACTACTGCGAAAGCATTTGCCAAGGACGTTT
TCATTAATCAAGAACGAAAGTTAGGGGATCGAAGATGATCAGATACCGTCGTAGTCTTAA
CCATAAACTATGCCGACTAGGGATCGGGTGGTGTTTTTTTAATGACCCACTCGGCACCTT
ACGAGAAATCAAAGTCTTTGGGTTCTGGGGGGAGTATGGTCGCAAGGCTGAAACTTAAAG
GAATTGACGGAAGGGCACCACCAGGAGTGGAGCCTGCGGCTTAATTTGACTCAACACGGG
GAAACTCACCAGGTCCAGACACAATAAGGATTGACAGATTGAGAGCTCTTTCTTGATTTT
GTGGGTGGTGGTGCATGGCCGTTCTTAGTTGGTGGAGTGATTTGTCTGCTTAATTGCGAT
AACGAACGAGACCTTAACCTACTAAATAGTGGTGCTAGCATTTGCTGGTTATCCACTTCT
TAGAGGGACTATCGGTTTCAAGCCGATGGAAGTTTGAGGCAATAACAGGTCTGTGATGCC
CTTAGACGTTCTGGGCCGCACGCGCGCTACACTGACGGAGCCAGCGAGTCTAACCTTGGC
CGAGAGGTCTTGGTAATCTTGTGAAACTCCGTCGTGCTGGGGATAGAGCATTGTAATTAT
TGCTCTTCAACGAGGAATTCCTAGTAAGCGCAAGTCATCAGCTTGCGTTGATTACGTCCC
TGCCCTTTGTACACACCGCCCGTCGCTAGTACCGATTGAATGGCTTAGTGAGGCCTCAGG
ATCTGCTTAGAGAAGGGGGCAACTCCATCTCAGAGCGGAGAATTTGGACAAACTTGGTCA
TTTAGAGGAACTAAAAGTCGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTA

    # of Homo sapien:

TACCTGGTTGATCCTGCCAGTAGCATATGCTTGTCTCAAAGATTAAGCCATGCATGTCTGAGTACGCACG
GCCGGTACAGTGAAACTGCGAATGGCTCATTAAATCAGTTATGGTTCCTTTGGTCGCTCGCTCCTCTCCT
ACTTGGATAACTGTGGTAATTCTAGAGCTAATACATGCCGACGGGCGCTGACCCCCTTCGCGGGGGGGAT
GCGTGCATTTATCAGATCAAAACCAACCCGGTCAGCCCCTCTCCGGCCCCGGCCGGGGGGCGGGCGCCGG
CGGCTTTGGTGACTCTAGATAACCTCGGGCCGATCGCACGCCCCCCGTGGCGGCGACGACCCATTCGAAC
GTCTGCCCTATCAACTTTCGATGGTAGTCGCCGTGCCTACCATGGTGACCACGGGTGACGGGGAATCAGG
GTTCGATTCCGGAGAGGGAGCCTGAGAAACGGCTACCACATCCAAGGAAGGCAGCAGGCGCGCAAATTAC
CCACTCCCGACCCGGGGAGGTAGTGACGAAAAATAACAATACAGGACTCTTTCGAGGCCCTGTAATTGGA
ATGAGTCCACTTTAAATCCTTTAACGAGGATCCATTGGAGGGCAAGTCTGGTGCCAGCAGCCGCGGTAAT
TCCAGCTCCAATAGCGTATATTAAAGTTGCTGCAGTTAAAAAGCTCGTAGTTGGATCTTGGGAGCGGGCG
GGCGGTCCGCCGCGAGGCGAGCCACCGCCCGTCCCCGCCCCTTGCCTCTCGGCGCCCCCTCGATGCTCTT
AGCTGAGTGTCCCGCGGGGCCCGAAGCGTTTACTTTGAAAAAATTAGAGTGTTCAAAGCAGGCCCGAGCC
GCCTGGATACCGCAGCTAGGAATAATGGAATAGGACCGCGGTTCTATTTTGTTGGTTTTCGGAACTGAGG
CCATGATTAAGAGGGACGGCCGGGGGCATTCGTATTGCGCCGCTAGAGGTGAAATTCTTGGACCGGCGCA
AGACGGACCAGAGCGAAAGCATTTGCCAAGAATGTTTTCATTAATCAAGAACGAAAGTCGGAGGTTCGAA
GACGATCAGATACCGTCGTAGTTCCGACCATAAACGATGCCGACCGGCGATGCGGCGGCGTTATTCCCAT
GACCCGCCGGGCAGCTTCCGGGAAACCAAAGTCTTTGGGTTCCGGGGGGAGTATGGTTGCAAAGCTGAAA
CTTAAAGGAATTGACGGAAGGGCACCACCAGGAGTGGAGCCTGCGGCTTAATTTGACTCAACACGGGAAA
CCTCACCCGGCCCGGACACGGACAGGATTGACAGATTGATAGCTCTTTCTCGATTCCGTGGGTGGTGGTG
CATGGCCGTTCTTAGTTGGTGGAGCGATTTGTCTGGTTAATTCCGATAACGAACGAGACTCTGGCATGCT
AACTAGTTACGCGACCCCCGAGCGGTCGGCGTCCCCCAACTTCTTAGAGGGACAAGTGGCGTTCAGCCAC
CCGAGATTGAGCAATAACAGGTCTGTGATGCCCTTAGATGTCCGGGGCTGCACGCGCGCTACACTGACTG
GCTCAGCGTGTGCCTACCCTACGCCGGCAGGCGCGGGTAACCCGTTGAACCCCATTCGTGATGGGGATCG
GGGATTGCAATTATTCCCCATGAACGAGGAATTCCCAGTAAGTGCGGGTCATAAGCTTGCGTTGATTAAG
TCCCTGCCCTTTGTACACACCGCCCGTCGCTACTACCGATTGGATGGTTTAGTGAGGCCCTCGGATCGGC
CCCGCCGGGGTCGGCCCACGGCCCTGGCGGAGCGCTGAGAAGACGGTCGAACTTGACTATCTAGAGGAAG
TAAAAGTCGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTA

    # of Arabidopsie thaliana:

ATCATAGTCAAAAGAAGAGTTTGATCCTGGCTCAGAAGGAACGCTAGCTATATGCTTAACACATGCAAGT
CGAACGTTGTTCTCGGGGAGCTAGGCAGAAGGAAAAGAGGCTCCTAGCTCAAGGTAGCTTGTCTCGCCCA
GGAGGCGGGAAGAGTTGAGAACAAAGTGGCGAACGGGTGCGTAAGGCGTGGGAATCTGCCGAACAGTTCG
GGCCAAATCCTGAAGAAAGCTAAAAAGCGCTGTTTGATGAGCCTGCGTAGTATTAGGTAGTTGGTTAGGT
AAAGGCTGACCAAGCCAATGATGCTTAGCTGGTCTTTTCGGATGATCAGCCACACTGGGACTGAGACACG
GCCCGGACTCCCACGGGGGGCAGCAGTGGGGAATCTTGGACAATGGGCGAAAGCCGATCCAGCAATATCG
CGTGAGTGAAGAAAGGCAATGCCGCTTGTAAAGCTCTTTCGTCGAGTGCGCGATCATGACAGGACTCGAG
GAAGAAGCCCCGGCTAACTCCGTGCCAGCAGCCGCGGTAAAACGGGGGGGGCAAGTGTTCTTCGGAATGA
CTGGGCGTAAAGGGCACGTAGGCGGTGAATCGGGTTGAAAGTGAAAGTCGCCAAAAAGTGGCGGAATGCT
TTCGAAACCAATTCACTTGAGTGAGACAGAGGAGAGTGGAATTTCGTGTGGAGGGGTGAAATCTACAGAT
CTACGAAGGAACGCCAAAAGCGAAGGCAGCTCTCTGGGTCCCTACCGACGCTGGGGGTGCGAAAGCATGG
GGGAGCGAACGGGATTAGATACCCTGGTAGTCCATGCCGTAAACGATGAGTGTTCGCCCTTGGTCTACGC
AGATCAGGGGCTCAGCTAACGCGTGAACACTCCGCCTGGGGAGTACGGTCGCAAGACCAAAACTCAAAGG
AATTGACGGGGGCCTGCACAAGCGGTGGAGCATGTGGTTTAATTCGATACAACGCGCAAAACCTTACCAG
CCCTTGACATATGAACAACAAAACCTATCCTTAACGGGATGGTACTCACTTTCATACAGGTGCTGCATGG
CTGTCGTCAGCTCGTGTCGTGAGATGTTTGGTCAAGTCCTATAACGAGCGAAACCCTCGTCTTGTGTTGC
TCAGACATGCGCCTAAGGAGAAAGGCTTGAAAACCGAAGTGAGCCAAGGAGCCGAGTGACGTGCCAGACC
TAGTAATTGAGTGACAGCAACTAGCTCTGCTCTCAGTAAGAAGGGAGACGGCGCCTTTCCAAGCCCTTTC
TAGTCTGCGCTTGAGTTTGATTGCAGCTAGCGCCGCGCTTTACTAAGAAGTGCGAAAGGGCTTTTCTCGC
TTGTTTAGTAAAGTCAAGTTTTTGACCCAGGTGACGACGACGTCGAGTTGGCGGCGGAGAAAGACTCGGC
ATTCAGGCGAGCCGCCCGGTGGTGTGGGACGAAGTAAGTGGGTTTAGTACGCCCTGCCAAAACGGCTCCG
AAACAAACAAAAAGGTGCGTGCCGCACTCACGAGGGACTGCCAGTGATATACTGGAGGAAGGTGGGGATG
ACGTCAAGTCCGCATGGCCCTTATGGGCTGGGCCACACACGTGCTACAATGGCAATTACAATGGGAAGCA
AGGCTGTAAGGCGGAGCGAATCCGGAAAGATTGCCTCAGTTCGGATTGTTCTCTGCAACTCGGGAACATG
AAGTTGGAATCGCTAGTAATCGCGGATCAGCATGCCGCGGTGAATATGTACCCGGGCCCTGTACACACCG
CCCGTCACACCCTGGGAATTGGTTTCGCCCGAAGCATCGGACCAATGATCACCCATGACTTCTGTGTACC
ACTAGTGCCACAAAGGCTTTTGGTGGTCTTATTGGCGCATACCACGGTGGGGTCTTCGACTGGGGTGAAG
TCGTAACAAGGTAGCCGTAGGGGAACCTGTGGCTGGATTGAATCC

# Remove the newline character ('\n') using the method .replace()
# You can look at help(str.replace) for more information:


### Second Exercice:
# Find the lenght of each of the sequence:


print "E. coli length: " 
print "S. cerevisiae length: "
print "A. thaliana length: "
print "H. sapiens length: " 

### Third Exercice:
# Find the occurence of each nucleic acid in each of the sequence
# Output a dictionnary for each sequence:
# (Try 2 differents methods to do it)
# (For ADVANCED users, try to find a third method to do it)

ecoli_nucleidacid_occurance =
scere_nucleidacid_occurance =
hsapien_nucleidacid_occurance =
athaliana_nucleidacid_occurance = 

# Find the more occurent nucleic acid for each sequence
# And the number of occurence

print 'The most present nucleic acid of 16S RNA of E. coli is {ec_type} and it appear {ec_num} times'.format(ec_type=, ec_num),
        ', of 18S RNA of S. cerevisiae is {sc_type} and it appear {sc_num} times'.format(sc_type=, sc_num=),
        ', of H, sapien is {hs_type} and it appear {hs_num} times'.format(hs_type=, hs_num=),
        ' and od A. thaliana is {at_type} and it appear {at_num} times'.format(at_type=, at_num=)


### Fourth Exercice:
# Find the %GC of each sequence
# As output, print the %GC of each sequence with the name of the species:



# Find the %GC of the first and last 50 nucleic acids
# As output, show which one (between the first and the last)
# is higher for each sequence and which one is the higher amount all

boolean_symbols = {'True': '>', 'False': '<'}


### Fifth Exercice:
# Find the possition of the first ATG in each sequence


### Supplementarry exercice:
# Transcribe the sequence
# print the first 50 nucleid acids in 5'- 3' orientation
# Tips1: You can use many time the same method

