n = int(input())

while n > 0:
    num = n % 10 # second mistake
    n //= 10 # first mistake

print(num) #third mistake
