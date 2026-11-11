def get_unique(numbers):
    unique_numbers = []
    for c in numbers:
        if c not in unique_numbers:
            unique_numbers.append(c)
    return unique_numbers

numbers = eval(input())

print(get_unique(numbers))




