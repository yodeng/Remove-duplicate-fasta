import sys

input_file=sys.argv[1]
output_file=sys.argv[2]

fasta_file=open(input_file, 'r')  #opens inputfile for reading
fasta_lines=fasta_file.read().split('>')[0:]  #splits each sequence by header
unique_sequences=open(output_file,'w')  #opens outputfile for writing

def remove_complete_duplicates(fasta_lines): #start of definition of a new function with purpose: remove_duplicates from sequence list
    outputlist=[] #creates an empty list to contain output/ uniquesequences
    setofuniqsequence=set() #assigns a set for sequences -set can only contain uniquesequences 
    for sequence in fasta_lines: #for loop - for sequence list in sequence list:
	 if sequence not in setofuniqsequence: # If sequence has not been encountered yet i.e unique:
           outputlist.append(sequence) # ... add it to list.
           setofuniqsequence.add(sequence) #... add it to set.
    return outputlist

result=remove_complete_duplicates(fasta_lines) # Remove duplicates from the list and defines as 'result'
unique_sequences.write('>'.join(result)) #'>' replaces lost > symbols
unique_sequences.close() #closes output file

#Usage: python script_name  fasta_file   output_fasta_file
