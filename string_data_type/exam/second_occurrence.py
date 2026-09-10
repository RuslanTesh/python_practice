s = input()
res = -2

if s.find('f', s.find('f') + 1) > -1:
    res = s.find('f', s.find('f') + 1)
elif s.find('f') > -1:
    res = -1
print(res)