temp = 0
total = 0

for i in range(4):
    s = input()
    for j in range(len(s)):
        total+=ord(s[j])
    if total > temp:
        temp = total
        word = s
    total = 0

print(word)


