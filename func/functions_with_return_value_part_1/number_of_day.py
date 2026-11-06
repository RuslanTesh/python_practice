def get_days(month):
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]

    if month in thirty_one:
        result = 31
    elif month in thirty:
        result = 30
    else:
        result = 28

    return result

num = int(input())

print(get_days(num))