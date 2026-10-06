s = input().split()

slangs = [el[1:] + el[0] + 'ки' for el in s]

print(*slangs, sep=' ')