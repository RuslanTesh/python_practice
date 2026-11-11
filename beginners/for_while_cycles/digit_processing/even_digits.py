num = int(input())
lenght = len(str(num))
power = lenght - 1
i = 1
flag = False
temp = num

while temp != 0:
    digit = num // 10 ** power
    if digit % 2 == 0:
        print(i, '-я четная цифра равна ', digit, sep='')
        i += 1
        flag = True
    num = num - (10 ** power * digit)
    power -= 1
    temp //= 10

if flag == False:
    print('Четных цифр в числе нет')
