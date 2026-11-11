n, m = int(input()), int(input())
flag = False

for b in range(1, n):
    for s in range(1, n):
        for g in range(1, n):
            if b + 3 * s + 2 * g == m:
                print(b, ' + ', 3, '×', s, ' + ', 2, '×', g, ' = ', m, sep ='')
                flag = True
if flag == False:
    print('При заданных n и m решений не существует.')