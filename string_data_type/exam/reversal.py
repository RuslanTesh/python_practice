s = input()
fh = s.find('h')
lh = s.rfind('h')
rev = s[lh - 1:fh:-1]

print(s[0:fh + 1], rev, s[lh:], sep='')