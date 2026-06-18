n = int(input())

n1 = n // 10**2 % 10
n2 = n // 10**1 % 10
n3 = n // 10**0 % 10

total = n1 + n2 + n3
middle_n = total - max(n1, n2, n3) - min(n1, n2, n3)

if max(n1, n2, n3) - min(n1, n2, n3) == middle_n:
    print('Число интересное')
else:
    print('Число неинтересное')