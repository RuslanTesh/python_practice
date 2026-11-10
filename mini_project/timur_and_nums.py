n = int(input())
attempts = 0

while n > 0:
    n //= 2
    attempts += 1

print(attempts)

