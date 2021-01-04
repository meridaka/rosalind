
name = "rosalind_seto"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)

d = open(f_r,'r')
s = d.readlines()
d.close()

n = int( s[0].strip() )
U = [i for i in range(1, (n+1))]
A = s[1].strip().split()
B = s[2].strip().split()

def set_setup(Z):
    Z[0] = Z[0][1:] 
    Z[-1] = int( Z[-1][:-1] )
    for k in range(0,len(Z)-1):
        if len(Z[k]) < 3:
            Z[k] = int( Z[k][0] )
        else:
            Z[k] = int( Z[k][:-1])
    
set_setup(A)
set_setup(B)

A_s = set(A)
B_s = set(B)
U_s = set(U)

uni = str( A_s.union(B_s) )
inter = str( A_s.intersection(B_s) )
diffAB = str( A_s.difference(B_s) )
diffBA = str( B_s.difference(A_s) )
diffUA = str( U_s.difference(A_s) )
diffUB = str( U_s.difference(B_s) )

ans = [uni, inter, diffAB, diffBA, diffUA, diffUB]

output = open(f_w,"w")
separator = '\n'
output.write(separator.join(ans))
output.close()
