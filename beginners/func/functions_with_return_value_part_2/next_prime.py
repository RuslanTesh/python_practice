def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def get_next_prime(num):
    while not is_prime(num):
        num += 1

    return num
    
n = int(input()) + 1

print(get_next_prime(n))




