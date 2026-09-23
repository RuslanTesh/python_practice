n = int(input())
tot_list = []

for i in range(n):
    s = input()
    if s not in tot_list:
        tot_list.append(s)

print(*tot_list, sep='\n')