import Bio
from Bio import SeqIO


input_file = open("rosalind_cons.txt", "r")
sequence_iterator = SeqIO.parse(input_file, "fasta")
sequences = [sequence.seq for sequence in sequence_iterator]
profiles= []

for base in range(0, len(sequences[0])):
    As = 0
    Cs = 0
    Gs = 0
    Ts = 0
    for sequence in sequences:
        if sequence[base] == "A":
            As += 1
        elif sequence[base] == "C":
            Cs += 1
        elif sequence[base] == "G":
            Gs += 1
        else:
            Ts += 1
    profiles.append([As, Cs, Gs, Ts])
    
consensus = ""
for base in range(0, len(profiles)):
    consensus_base = max(profiles[base])
    if consensus_base == profiles[base][0]:
        consensus += "A"
    elif consensus_base == profiles[base][1]:
        consensus += "C"
    elif consensus_base == profiles[base][2]:
        consensus += "G"
    else:
        consensus += "T"   

profile = ["A: ","C: ","G: " ,"T: "]

for line in profiles:
    profile[0] += str(line[0])+" "
    profile[1] += str(line[1])+" "
    profile[2] += str(line[2])+" "
    profile[3] += str(line[3])+" "
    
final_profile = ""

for p in profile:
    final_profile += p.strip() + "\n"

answer = consensus + "\n" + final_profile
    
output_file = open("consensus_profile.txt","w")
output_file.write(answer)
output_file.close()
