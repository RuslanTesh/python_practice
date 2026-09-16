alphabet = 'abcdefghijklmnopqrstuvwxyz'
list = []

for i in range(len(alphabet)):
    list.append(alphabet[i] * (i + 1))

print(list)