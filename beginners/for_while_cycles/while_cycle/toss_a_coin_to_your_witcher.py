sum = int(input())
count = 0

while sum // 25 > 0:
    count += sum // 25
    sum -= 25 * (sum // 25)

while sum // 10 > 0:
    count += sum // 10
    sum -= 10 * (sum // 10)

while sum // 5 > 0:
    count += sum // 5
    sum -= 5 * (sum // 5)

while sum // 1 > 0:
    count += sum // 1
    sum -= 1 * (sum // 1)

print(count)