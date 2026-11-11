n = int(input())
letters = 'АБВГДЕЖЗИЙКЛМНОП'
digits = '0123456789'

for i in range(n):
    s = input()
    if len(s) != 2 or s[1] not in letters or s[0] not in digits:
        print('NO')
    else:
        print('YES')