num = int(input())
flag = 'YES'
last = num % 10

while num != 0:
    n = num % 10
    if n < last:
        flag = 'NO'
    last = n
    num //= 10

print(flag)