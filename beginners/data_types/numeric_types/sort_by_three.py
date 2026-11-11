a = int(input())
b = int(input())
c = int(input())

total = a + b + c
max_n = max(a, b, c)
min_n = min(a, b, c)
middle_n = total - max(a, b, c) - min(a, b, c)

print(max_n)
print(middle_n)
print(min_n)
