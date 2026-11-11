arr = []

for x in range(int(input())):
    arr.append(input())

arr.sort()
print(*arr, sep='\n')