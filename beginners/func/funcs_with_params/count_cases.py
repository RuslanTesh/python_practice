def print_case_counts(s):
    s = ' '.join(s).split()
    upper = 0
    lower = 0

    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            continue

    print(f'Букв в верхнем регистре: {upper}')
    print(f'Букв в нижнем регистре: {lower}')

print_case_counts(input())