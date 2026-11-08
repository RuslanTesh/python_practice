def is_prime(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

n = int(input())

print(is_prime(n))




