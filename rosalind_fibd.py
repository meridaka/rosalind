
input_file = open("rosalind_fibd.txt", "r")
contents = input_file.read().strip().split()
months = int(contents[0])
mortality = int(contents[1])

def totes_buns(d):
    total_bunnies = 0
    for key in d:
        total_bunnies += d.get(key)
    return total_bunnies

def mortal_rabbits(n, m):
    if n == 1:
        return {1:1}
    else:
        buns = mortal_rabbits(n-1, m)
        baby_buns = totes_buns(buns) - buns[1]
        older_buns = age_up_bunnies(buns, m)
        older_buns[1] = baby_buns
        return older_buns

def age_up_bunnies(l, m):
    new_l = {}
    for key in l:
        if key+1 <= m:
            new_l[key+1] = l[key]
    if m+1 in new_l:
        new_l[m+1] = 0
    return new_l


a = mortal_rabbits(months, mortality)


    
answer = str(totes_buns(a))
output_file = open("mortal_rabbits.txt","w")
output_file.write(answer)
output_file.close()
