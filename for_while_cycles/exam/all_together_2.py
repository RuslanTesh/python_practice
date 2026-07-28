n = int(input())

three_cnt = 0
last_num_cnt = 0
last_digit = n % 10
odd_cnt = 0
more_than_five_sum = 0
product = 1
zero_five_cnt = 0

while n != 0:
    digit = n % 10
    if digit == 3:
        three_cnt += 1

    if digit == last_digit:
        last_num_cnt += 1

    if digit % 2 == 0:
        odd_cnt += 1

    if digit > 5:
        more_than_five_sum += digit

    if digit > 7:
        product *= digit

    if digit == 5 or digit == 0:
        zero_five_cnt += 1

    n //= 10

print(three_cnt)
print(last_num_cnt)
print(odd_cnt)
print(more_than_five_sum)
print(product)
print(zero_five_cnt)
