n = int(input())
binary = ''

while n != 0:
    s = n % 2
    binary = str(s) + binary
    n //= 2

print(binary)
