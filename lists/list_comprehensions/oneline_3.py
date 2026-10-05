squares = [
    int(i) ** 2
    for i in input().split()
    if "4" not in str(int(i) ** 2) and int(i) % 2 == 0
]

print(*squares, sep=" ")
