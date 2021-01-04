input_file = open("rosalind_hamm.txt", "r")
sequences = input_file.readlines()
dna_sequences = [sequence.strip() for sequence in sequences]

hamming_distance = 0

for x in range(0, len(dna_sequences[0])):
    if dna_sequences[0][x] != dna_sequences[1][x]:
        hamming_distance += 1

answer = (str(hamming_distance))
output_file = open("point_mutations.txt", "w")
output_file.write(answer)
output_file.close()
