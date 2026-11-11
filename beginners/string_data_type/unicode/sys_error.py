s = input()
res = ''
c = 0

while c < len(s):
    if s[c] == '[':
        code = chr(int(s[c + 3:c + 7]))
        res += code
        c += 8
    else:
        res += s[c]
        c += 1

print(res)

        

