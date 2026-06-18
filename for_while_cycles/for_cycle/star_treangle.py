n = int(input())

stars = n + 1

for i in range(n):
    stars = stars - 1
    print(stars * '*')