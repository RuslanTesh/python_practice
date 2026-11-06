def math_round_to_int(num):
    result = round(num)
    if num - result == 0.5:
        result += 1
    return result

num = float(input())

print(math_round_to_int(num))
