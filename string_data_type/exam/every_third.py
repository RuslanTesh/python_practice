s = input()
new_s = ''

for c in range(len(s)):
    if c % 3 != 0:
        new_s += s[c]
    else:
        continue

print(new_s)
        