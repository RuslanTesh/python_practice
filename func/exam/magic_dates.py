def is_magic(date):
    date = date.split('.')
    new_date = [int(char) for char in date]

    if new_date[0] * new_date[1] == new_date[2] % 100:
        return True

    return False


date = input()

print(is_magic(date))




