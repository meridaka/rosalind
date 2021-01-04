input_file = open("rosalind_subs(1).txt", "r")
contents = input_file.readlines()

s = contents[0].strip()
t = contents[1].strip()

positions = []

while s.find(t) != -1:
    position = s.find(t)
    positions.append(str(position+1))
    s = s[:position] + "*" + s[position+1:]

answer = " ".join(positions)
print(answer)
    
output_file = open("motifs.txt","w")
output_file.write(answer)
output_file.close()
