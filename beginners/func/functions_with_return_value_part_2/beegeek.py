def is_palindrome(num):
    return num == num[::-1]

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def is_even(num):
    return num % 2 == 0

def is_valid_password(password):
    password = password.split(':')
    
    if len(password) == 3:
        a = password[0]
        b = int(password[1])
        c = int(password[2])

        return is_palindrome(a) and is_prime(b) and is_even(c)

    return False
    

psw = input()

print(is_valid_password(psw))




