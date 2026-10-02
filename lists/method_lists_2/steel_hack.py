n = int(input()[1:])
arr = []

for i in range(n):
    s = input()
    if '#' not in s:
        s = s.rstrip()
        arr.append(s)
    else:
        position = s.index('#')
        s = s[:position].rstrip()
        arr.append(s)

print(*arr, sep='\n')
