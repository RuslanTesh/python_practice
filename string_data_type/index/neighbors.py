s = input()
total = 0
temp = 0

for i in range(len(s)):
    if temp == s[i]:
        total += 1
    temp = s[i]

print(total)