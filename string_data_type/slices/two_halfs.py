s = input()
d = len(s) // 2

if len(s) % 2 == 0:
    print(s[d:] + s[:d])
else:
    d += 1
    print(s[d:] + s[:d])