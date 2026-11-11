s = input()
counter = 0
result = ''

for i in range(len(s)):
    if s.count(s[i]) >= counter:
        counter = s.count(s[i])
        result = s[i]

print(result)
