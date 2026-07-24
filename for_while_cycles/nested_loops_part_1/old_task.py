for b in range(1, 11):
    for c in range(1, 21):
        for l in range(1, 201):
            total = 10 * b + 5 * c + 0.5 * l
            if total == 100 and (l + c + b) == 100:
                print(b, c, l)
