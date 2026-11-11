l = input().split()
m = input().split()

arr = [int(l[i]) + int(m[i]) for i in range(len(l))]

print(*arr, sep=' ')