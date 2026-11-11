max_x = - 10 ** 6
sum = 0
flag = False

for i in range(10):
    num = int(input())
    if num < 0:
        sum += num
        flag = True
    if num < 0:
        if max_x < num:
            max_x = num 

if flag:
    print(sum)
    print(max_x)
else:
    print('NO')