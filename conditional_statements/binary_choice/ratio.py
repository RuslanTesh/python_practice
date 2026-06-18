x = int(input())

x_1 = x % 10
x_2 = x // 10 % 10
x_3 = x // 100 % 10
x_4 = x // 1000

if x_1 + x_4 == x_3 - x_2:
    output = 'ДА'

else:
    output = 'НЕТ'

print(output)