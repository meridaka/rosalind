input_file = open("rosalind_fib.txt", "r")
contents = input_file.read()
arguments = contents.strip().split()

months = int(arguments[0])
litter_size = int(arguments[1])
def wascally_wabbits(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return wascally_wabbits(n-2,k)*k + wascally_wabbits(n-1, k)

output_file = open("rabbits_and_recurrence_r.txt", "w")
output_file.write(str(wascally_wabbits(months, litter_size)))
output_file.close()
