s = input().split()
arr = []

for x in s:
    arr.append(int(x))

arr.sort()
print(*arr)
arr.sort(reverse=True)
print(*arr)