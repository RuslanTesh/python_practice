n = int(input())

max_number = 1
next_number = 1

for _ in range(1, n + 1):
    number = int(input())
    if number > max_number:
        next_number = max_number
        max_number = number
    elif number > next_number:
        next_number = number

print(max_number, next_number, sep='\n')