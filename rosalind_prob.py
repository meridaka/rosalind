#calculating the common logarithm of the probability that a random
#string constructed with specific GC content will match a string exactly
import math

name = "rosalind_prob"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)


d = open(f_r,'r')
s = d.readline().strip()
gc_content = d.readline().strip().split()
d.close()

print(gc_content)

common_log_prob = []

for content in gc_content:
    prob = 0
    for bp in s:
        if (bp == "A") or (bp == "T"):
            prob += math.log10( (1 - float( content ))/2 )
        else:
            prob += math.log10( float( content )/2 )
    common_log_prob.append(str( round(prob,3) ))


print(common_log_prob)

output = open(f_w,"w")
separator = ' '
output.write(separator.join(common_log_prob))
output.close()
