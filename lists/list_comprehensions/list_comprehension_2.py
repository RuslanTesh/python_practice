s = input().split()

cubes = [int(i) ** 3 for i in s]

print(*cubes)