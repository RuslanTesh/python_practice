def is_password_good(password):
    upper_chars = lower_chars = digits = 0

    if len(password) < 8:
        return False

    for el in password:
        if el.isupper():
            upper_chars = 1
        elif el.islower():
            lower_chars = 1
        elif el.isdigit():
            digits = 1

    if upper_chars == lower_chars == digits == 1:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))




