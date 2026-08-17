s = input()
digits = '0123456789'
flag = False

for i in range(len(s)):
    if s[i] in digits:
        flag = True
        break

if flag:
    print('Цифра')
else:
    print('Цифр нет')
