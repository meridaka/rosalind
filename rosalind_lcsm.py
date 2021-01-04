import Bio
import itertools
from Bio import SeqIO

input_file = open("rosalind_lcsm.txt", "r")
contents = SeqIO.parse(input_file, "fasta")
sequences = [str(sequence.seq) for sequence in contents]

nucleotides = ['A', 'C', 'G', 'T']

#growing functions
def grow_left(motif, total_motifs):
    grown_l_motifs = []
    for nucleotide in nucleotides:
        possible_motif = nucleotide + motif
        if possible_motif not in total_motifs:
            grown_l_motifs.append(possible_motif)
    return grown_l_motifs

def grow_right(motif, total_motifs):
    grown_r_motifs = []
    for nucleotide in nucleotides:
        possible_motif = motif + nucleotide
        if possible_motif not in total_motifs:
            grown_r_motifs.append(possible_motif)
    return grown_r_motifs
    
def grow_both(motif, total_motifs):
    grown_b_motifs = []
    for startn in nucleotides:
        for endn in nucleotides:
            possible_motif = startn + motif + endn
            if possible_motif not in total_motifs:
                grown_b_motifs.append(possible_motif)
    return grown_b_motifs

#function that checks and removes any motifs that don't appear in all sequences
def motif_validator(sequence_list, motif_list):
    validated_motifs = []
    for motif in motif_list:
        counter = 0
        for sequence in sequence_list:
            if motif in sequence:
                counter += 1
            else:
                break
        if counter == len(sequence_list):
            validated_motifs.append(motif)
    return validated_motifs

def longest_motif_finder(sequence_list, motif_list, total_motifs):
    motifs_to_grow = motif_validator(sequence_list, motif_list)
    if motifs_to_grow != []:
        new_motif_list = []
        for motif in motifs_to_grow:
            l_grow_motifs = grow_left(motif, total_motifs)
            total_motifs += l_grow_motifs
            r_grow_motifs = grow_right(motif, total_motifs)
            total_motifs += r_grow_motifs
            b_grow_motifs = grow_both(motif, total_motifs)
            total_motifs += b_grow_motifs
            new_motif_list += l_grow_motifs + r_grow_motifs + b_grow_motifs
        longest_motif_finder(sequence_list, new_motif_list, total_motifs)
    longest_motif = get_longest(motif_list)
    return longest_motif

def get_longest(motif_list):
    longest_motif = ''
    for motif in motif_list:
        if len(motif) > len(longest_motif):
            longest_motif = motif
    return longest_motif
        
answer = longest_motif_finder([sequences[0], sequences[1]], nucleotides, nucleotides)
output_file = open("shared_motif.txt","w")
output_file.write(answer)
output_file.close()
