s = input()
total = 0

for i in range(len(s)):
    total += ord(s[i])

print('Текст сообщения: ', "'", s, "'", sep='')
print(f'Стоимость сообщения: {total * 3}🐝')