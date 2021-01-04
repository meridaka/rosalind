import Bio
from Bio import SeqIO

input_file = open("rosalind_gc.txt", "r")
sequences = SeqIO.parse(input_file, "fasta")
dna_seqs = [sequence for sequence in sequences]

highest_gc = ["",0]

for sequence in dna_seqs:
    g_content = sequence.seq.count("G")
    c_content = sequence.seq.count("C")
    gc_content = float(g_content + c_content)/len(sequence.seq)*100
    if gc_content > highest_gc[1]:
        highest_gc = [sequence.id, gc_content]

answer = (str(highest_gc[0]) + "\n" + str(highest_gc[1]))
output_file = open("gc_content.txt", "w")
output_file.write(answer)
output_file.close()
