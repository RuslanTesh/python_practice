def get_factors(num):
    divisors_list = [int(i) for i in range(1, num + 1) if num % i == 0]
    return divisors_list
    

n = int(input())

print(get_factors(n))




