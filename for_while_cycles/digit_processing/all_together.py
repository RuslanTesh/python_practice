num = int(input())
sum = 0
count = 0
product = 1
avg = 0
first_n = 0
first_last_sum = 0
last_n = num % 10

while num != 0:
    n = num % 10
    sum += n
    count += 1
    product *= n
    avg = sum / count
    first_n = n
    if num < 10:
        first_last_sum = num + last_n
    num //= 10

print(sum)
print(count)
print(product)
print(avg)
print(first_n)
print(first_last_sum)