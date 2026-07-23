num = int(input())
last = num % 10
flag = 'YES'

while num != 0:
    n = num % 10
    if n != last:
        flag = 'NO'
    num //= 10

print(flag)
