name = input()
counter = 0

while name != 'хватит' and name != 'стоп' and name != 'достаточно':
    counter += 1
    name = input()

print(counter)