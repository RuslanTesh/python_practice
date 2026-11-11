x = int(input())

x_1 = (x // 10**3) % 10
x_2 = (x // 10**2) % 10
x_3 = (x // 10**1) % 10
x_4 = (x // 10**0) % 10

if x_1 != 0 and x // 10**3 <= 9 and (x % 7 == 0 or x % 17 == 0): 
    print('YES')
else:
    print('NO')