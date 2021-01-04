input_file = open("rosalind_iev.txt", "r")
contents = input_file.read().strip().split()

AAxAA = [float(contents[0]), 1]
AAxAa = [float(contents[1]), 1]
AAxaa = [float(contents[2]), 1]
AaxAa = [float(contents[3]), 3.0/4]
Aaxaa = [float(contents[4]), 1.0/2]
aaxaa = [float(contents[5]), 0]

couples =  [AAxAA, AAxAa, AAxaa, AaxAa, Aaxaa, aaxaa]

expected_value = 0.0
for couple in couples:
    expected_value += couple[0]*couple[1]


answer = str(2*expected_value)
output_file = open("expected_offspring.txt","w")
output_file.write(answer)
output_file.close()
