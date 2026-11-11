n = int(input())

first = n % 10
second = n // 10 % 10
third = n // 100 % 10
fourth = n // 1000 % 10

print("Цифра в позиции тысяч равна", fourth)
print("Цифра в позиции сотен равна", third)
print("Цифра в позиции десятков равна", second)
print("Цифра в позиции единиц равна", first)