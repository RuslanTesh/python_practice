a, b = int(input()), int(input())

for i in range(a, b + 1):
    counter = 0
    if i == 1:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    
    if counter > 2:
        continue
    else:
        print(i)