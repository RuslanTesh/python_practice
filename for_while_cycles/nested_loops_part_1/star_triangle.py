n = int(input())
top = n // 2 + 1

for i in range(1, n + 1):
    if top < i:
        break
    for j in range(i):
        print('*', end='')
    print()

for k in range(top - 1, 0, -1):
    for l in range(k):
        print('*', end='')
    print()