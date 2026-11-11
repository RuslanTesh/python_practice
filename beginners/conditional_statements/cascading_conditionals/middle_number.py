x = int(input())
y = int(input())
z = int(input())

if x >= y >= z or z >= y >= x:
    print(y)
elif x >= z >= y or y >= z >= x:
    print(z)
elif y >= x >= z or z >= x >= y:
    print(x)
