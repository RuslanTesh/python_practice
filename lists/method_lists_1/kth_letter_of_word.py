n = int(input())
list = []
total_list = ''

for _ in range(n):
    s = input()
    list.append(s)

k = int(input()) - 1

for i in range(n):
    if len(list[i]) > k:
        total_list += list[i][k]
    else:
        continue


print(total_list)