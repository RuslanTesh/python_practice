s = input().split('.')
flag = 'ДА'

for num in s:
    if not 0 <= int(num) <= 255:
        flag = 'НЕТ'

print(flag)

