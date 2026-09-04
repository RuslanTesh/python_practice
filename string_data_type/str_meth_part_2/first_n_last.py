s = input()

if 'f' not in s:
    print('NO')
elif s.count('f') == 1:
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))