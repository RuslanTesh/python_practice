n = int(input())
list = []

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        list.append(num)

print(list)