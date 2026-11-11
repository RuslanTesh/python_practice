s = input()
plus, star = '+', '*'

for i in range(len(s)):
    if s[i] in plus:
        plus += '+'
    if s[i] in star:
        star += '*'

print('Символ + встречается', len(plus) - 1, 'раз')
print('Символ * встречается', len(star) - 1, 'раз')
