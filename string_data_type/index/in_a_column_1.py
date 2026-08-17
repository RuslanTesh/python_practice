s = input()
lenght = len(s)

for i in range(0, lenght):
    if i % 2 != 0:
        continue
    print(s[i])
