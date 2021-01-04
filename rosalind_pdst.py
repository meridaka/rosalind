from Bio import SeqIO

name = "rosalind_pdst"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)

records = list(SeqIO.parse(f_r,"fasta"))
sequences = []

for sequence in records:
    sequences.append(sequence.seq)

distance_matrix = []

def p_distance(s1, s2):
    diff = 0
    for k in range(0, len(s1)):
        if s1[k] != s2[k]:
            diff += 1
    return float(diff / len(s1))

for s1 in sequences:
    row_entry = []
    for s2 in sequences:
        row_entry.append(str( p_distance(s1, s2) ))
    distance_matrix.append(' '.join(row_entry))



output = open(f_w,"w")
separator = '\n'
output.write(separator.join(distance_matrix))
output.close()
