num = int(input())

while num != 0:
    n = num % 10
    num //= 10
    print(n)