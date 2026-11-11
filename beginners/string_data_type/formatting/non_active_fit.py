g = 0.2
day, weight = int(input()), float(input())

if day * g > 100 - weight:
    print('Что-то пошло не так')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - day * g} кг')
elif day * g <= 100 - weight:
    print('Все идет по плану')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - day * g} кг')
    