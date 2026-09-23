n = int(input())
seq = []
upd_seq = []

for _ in range(n):
    seq.append(input())

request = input()

for s in seq:
    if request.lower() in s.lower():
        upd_seq.append(s)

print(*upd_seq, sep='\n')

