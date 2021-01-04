input_file = open("rosalind_iprb.txt", "r")
contents = input_file.read().strip().split()

K = float(contents[0])
M = float(contents[1])
N = float(contents[2])

k = K - 1
m = M - 1

T = K + M + N
t = T - 1

HHxHH_prob = (K*k)/(T*t)
HHxHh_prob = 2*((K*M)/(T*t))
HHxhh_prob = 2*((K*N)/(T*t))
Hhxhh_prob = 2*((M*N)/(T*t))*(1.0/2)
HhxHh_prob = ((M*m)/(T*t))*(3.0/4)


answer = str(HHxHH_prob + HHxHh_prob + HHxhh_prob + Hhxhh_prob + HhxHh_prob)
output_file = open("mendel.txt","w")
output_file.write(answer)
output_file.close()
