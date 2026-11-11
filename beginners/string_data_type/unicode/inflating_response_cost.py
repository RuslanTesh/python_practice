s = input()
en = 'eyopaxcETOPAHXCBM'
ru = 'еуорахсЕТОРАНХСВМ'
total_new = 0
total_old = 0
new_s = ''

for k in range(len(s)):
    total_old += ord(s[k])

for i in range(len(s)):
    current_char = s[i]
    if 65 <= ord(s[i]) <= 121:
        temp = en.find(current_char)
        if temp != -1:
            current_char = ru[temp]
    new_s += current_char
    total_new += ord(current_char)
    

print(f'Старая стоимость: {total_old * 3}🐝')
print(f'Новая стоимость: {(total_new) * 3}🐝')

