#reading the fasta sequences
from Bio import SeqIO

name = "rosalind_tran"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)


records = list(SeqIO.parse(f_r,"fasta"))

s1 = records[0].seq
s2 = records[1].seq

transitions = 0
transversions = 0

puri = ["A","G"]
pyri = ["C","T"]

for k in range(0,len(s1)):
    bp1 = s1[k]
    bp2 = s2[k]
    if bp1 == bp2:
        continue
    elif bp1 in puri and bp2 in puri:
        transitions += 1
    elif bp1 in pyri and bp2 in pyri:
        transitions += 1
    else:
        transversions += 1

ratio = transitions/transversions

output = open(f_w,"w")
output.write(str( ratio ))
output.close()
