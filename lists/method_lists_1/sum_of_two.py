n = int(input())
full_list = []
update_list = []

for _ in range(n):
    num = int(input())
    full_list.append(num)

for i in range(n - 1):
    update_list.append(full_list[i] + full_list[i + 1])

print(update_list)