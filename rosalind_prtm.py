#creating the monoisotopic mass dictionary

f = open("data\monoisotopic_mass.txt",'r')

monoisotopic_mass = {}

for line in f.readlines():
    l = line.strip().split()
    monoisotopic_mass[l[0]] = l[1]

f.close()

#calculating protein mass

name = "rosalind_prtm"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)


d = open(f_r,'r')
protein = d.readline().strip()
d.close()

p_mass = 0

for aminoacid in protein:
    p_mass += float( monoisotopic_mass[aminoacid] )


output = open(f_w,"w")
output.write(str( p_mass ))
output.close()
