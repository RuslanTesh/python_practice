def print_symbol_counts(s):
    s = ' '.join(s).split()
    s.sort()
    new_s = []

    for c in s:
        if c not in new_s:
            new_s.extend(c)

    for el in new_s:
        print(el, sep=f': {s.count(el)}', end=f': {s.count(el)}\n')



s = input().lower()

print_symbol_counts(s)