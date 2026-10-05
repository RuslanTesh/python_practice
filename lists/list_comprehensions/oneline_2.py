s = input()

digits = [i for i in s if i.isdigit()]

print(*digits, sep='')