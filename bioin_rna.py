dna_file = open("rosalind_rna.txt")
dna_sequence = dna_file.read()

transcribed_RNA = dna_sequence.replace("T","U")

transcribed_sequence = open("rosalind_rna_output.txt", "w")
transcribed_sequence.write(transcribed_RNA)
transcribed_sequence.close()
