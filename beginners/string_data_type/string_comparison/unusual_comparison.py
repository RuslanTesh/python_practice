s1 = input().lower()
s2 = input().lower()

ns1 = ''
ns2 = ''

for c in s1:
    if c.isalpha():
        ns1 += c

for c in s2:
    if c.isalpha():
        ns2 += c

if ns1 == ns2:
    print('YES')
else:
    print('NO')




