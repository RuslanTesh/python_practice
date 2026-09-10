res_max = ''
res_min = 'я'

while True:
    s = input()
    if s == 'КОНЕЦ':
        break
    if res_max <= s:
        res_max = s
    if res_min >= s:
        res_min = s

print(f'Минимальная строка ⬇️: {res_min}')
print(f'Максимальная строка ⬆️: {res_max}')