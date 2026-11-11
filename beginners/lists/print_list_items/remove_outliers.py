n = int(input())
seq = []
tot_seq = []

for _ in range(n):
    seq.append(int(input()))

maximum = max(seq)
minimum = min(seq)

for el in seq:
    if el != maximum and el != minimum:
        tot_seq.append(el) 

print(*tot_seq, sep='\n')