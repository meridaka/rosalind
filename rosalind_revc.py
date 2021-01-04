import Bio
from Bio.Seq import Seq

dna_file = open("rosalind_revc.txt")
dna_sequence = Seq(dna_file.read())

reverse_complement = dna_sequence.reverse_complement()

output_file = open("rosalind_reverse_complement.txt", "w")
output_file.write(str(reverse_complement))
output_file.close()
