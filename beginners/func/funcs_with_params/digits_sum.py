def print_digit_sum(num):
    num = ' '.join(num).split()
    integer_nums = [int(x) for x in num]
    print(sum(integer_nums))

n = input()

print_digit_sum(n)