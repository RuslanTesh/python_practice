num = int(input())
fives_total = 0

while 6 > num > 0:
    if num == 5:
        fives_total += 1

    num = int(input())

print(fives_total) 