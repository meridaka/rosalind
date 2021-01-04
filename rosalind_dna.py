dna_file = open("rosalind_dna.txt")
dna_sequence = dna_file.read()

As = dna_sequence.count("A")
Ts = dna_sequence.count("T")
Gs = dna_sequence.count("G")
Cs = dna_sequence.count("C")

number_of_nucleotides = open("rosalind_dna_output.txt", "w")
output = str(As) + " " + str(Cs) + " " + str(Gs) + " " + str(Ts)
number_of_nucleotides.write(output)
number_of_nucleotides.close()
