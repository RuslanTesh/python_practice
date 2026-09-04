s = input()
fh = s.find('h')
lh = s.rfind('h')
res = ''

for i in range(len(s)):
    if fh <= i <= lh:
        continue
    else:
        res += s[i]

print(res)