import Bio
from Bio.Seq import Seq

input_file = open("rosalind_prot.txt", "r")
sequence = Seq(input_file.read().strip())

answer = str(sequence.translate())[:-1]
output_file = open("rna_to_protein.txt","w")
output_file.write(answer)
output_file.close()
