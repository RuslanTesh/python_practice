n = int(input())

f = n % 10
s = n // 10 % 10
t = n // 100 % 10

print(t, s, f, sep='')
print(t, f, s, sep='')
print(s, t, f, sep='')
print(s, f, t, sep='')
print(f, t, s, sep='')
print(f, s, t, sep='')