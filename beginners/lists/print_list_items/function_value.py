n = int(input())
seq = []
f_seq = []

for _ in range(n):
    num = int(input())
    seq.append(num)

for el in seq:
    el = el**2 + 2 * el + 1
    f_seq.append(el)

print(*seq, sep ='\n')
print()
print(*f_seq, sep='\n')