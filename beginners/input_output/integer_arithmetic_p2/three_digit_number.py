n = int(input())

f = n % 10
s = n // 10 % 10
t = n // 100 % 10

print("Сумма цифр =", f + s + t)
print("Произведение цифр =", f * s * t)