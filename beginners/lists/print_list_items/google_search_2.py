strings, find_strings, total_strings = [], [], []
n = int(input())

for _ in range(n):
    strings.append(input())

k = int(input())

for _ in range(k):
    find_strings.append(input())

for s in strings:
    flag = True
    for f in find_strings: 
        if f.lower() not in s.lower():
            flag = False
            break

    if flag:
        total_strings.append(s)


print(*total_strings, sep='\n')
