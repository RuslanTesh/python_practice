n = int(input())

for i in range(0, 24):
    for j in range(0, 60):
        if i ** n == j:
            if i < 10 and j < 10:
                print(0, i, ':', 0, j, sep='')
            elif j < 10:
                print(i, ':', 0, j, sep='')
            elif i < 10:
                print(0, i, ':', j,sep='')
            else:
                print(i, ':', j, sep='')