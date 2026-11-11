n = int(input())
s = 0

while n != 0:
    last_digit = n % 10 
    if n % 2 == 0:
        s += last_digit
    n //= 10
print(s)