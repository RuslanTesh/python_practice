strings = input().split()
s = []

for x in strings:
    s.append(int(x))

maximum = s.index(max(s))
minimum = s.index(min(s))

s[maximum], s[minimum] = s[minimum], s[maximum]

print(*s)