n = int(input())
largest = 0

for i in range(n):
    x = int(input())
    if x > largest:
        largest = x
    s_largest = x
    if x < s_largest < largest:
        s_largest = x

print(largest) 
print(s_largest) 
