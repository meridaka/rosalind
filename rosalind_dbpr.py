from Bio import ExPASy
from Bio import SwissProt

name = "rosalind_dbpr"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)

d = open(f_r,'r')
protein_id = d.readline().strip()
d.close()

handle = ExPASy.get_sprot_raw(protein_id)
record = SwissProt.read(handle) #if you want to do multiple proteins use
                                #SwissProt.parse(handle)
handle.close()


cr = []
for entry in record.cross_references:
    if entry[0] == 'GO':
        if(entry[2][0] == 'P'):
            cr.append(entry[2][2:])

print(cr)

output = open(f_w,"w")
separator = '\n'
output.write(separator.join(cr))
output.close()

#check the attributes of the record
#print(dir(record))

#to see the list of references to other databases
#print(record.cross_references[0])