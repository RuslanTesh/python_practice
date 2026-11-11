f = int(input())
s = int(input())
v = input()

if v != '*' and v != '/' and v != '+' and v != '-':
    print('Неверная операция')

if v == '*':
    print(f * s)
elif v == '/' and s == 0:
    print('На ноль делить нельзя!')
elif v == '/':
    print(f / s)
elif v == '+':
    print(f + s)
elif v == '-':
    print(f - s)