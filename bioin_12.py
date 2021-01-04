import Bio
from Bio import SeqIO

import itertools

input_file = open("rosalind_grph.txt", "r")
contents = SeqIO.parse(input_file, "fasta")

sequences = [sequence for sequence in contents]

adjacency_list = []

sequences_se = []

for sequence in sequences:
    start = sequence.seq[:3]
    end = sequence.seq[-3:]
    sequences_se.append([sequence.id, start, end])

product_list = list(itertools.product(sequences_se, repeat=2))

for product in product_list:
    if product[0] != product[1]:
        if product[0][2] == product[1][1]:
            directed_pair = [product[0][0], product[1][0]]
            if not directed_pair in adjacency_list:
                adjacency_list.append(directed_pair)
        elif product[1][2] == product[0][1]:
            directed_pair = [product[1][0], product[0][0]]
            if not directed_pair in adjacency_list:
                adjacency_list.append(directed_pair)

answer = ""

for directed_pair in adjacency_list:
    answer += str(directed_pair[0]) + " " + str(directed_pair[1]) + "\n"
    
output_file = open("overlap.txt","w")
output_file.write(answer)
output_file.close()
