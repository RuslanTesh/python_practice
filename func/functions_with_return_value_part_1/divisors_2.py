def number_of_factors(num):
    divisors_list = [int(i) for i in range(1, num + 1) if num % i == 0]
    return len(divisors_list)

n = int(input())

print(number_of_factors(n))




