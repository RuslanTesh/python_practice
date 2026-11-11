num = int(input())
maximum = 0
minimum = num % 10

while num != 0:
    n = num % 10
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n
    num //= 10

print("Максимальная цифра равна", maximum)
print("Минимальная цифра равна", minimum)