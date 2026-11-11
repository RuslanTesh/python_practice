m = int(input())

if (m % 2 != 0 and 1 <= m <= 7) or (8 <= m <= 12 and m % 2 == 0):
    print(31)
elif (m == 2):
    print(28)
else:
    print(30)