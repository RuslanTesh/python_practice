a, b = int(input()), int(input())
max_a, sum_a = 0, 0

for i in range(a, b + 1):
    checker = 0

    for j in range(1, i + 1):
        if i % j == 0:
            checker += j
            
    if checker >= sum_a:
        sum_a = checker
        max_a = i
print(max_a, sum_a)