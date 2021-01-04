name = "rosalind_fibo"
f_r = "data\{}.txt".format(name)
f_w = "data\{}_output.txt".format(name)

d = open(f_r,'r')
n= int( d.readline().strip() )
d.close()

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

ans = fibo(n)

output = open(f_w,"w")
output.write(str( ans ))
output.close()
