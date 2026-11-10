import random

def is_valid(n):
    return (n.isdigit() and 0 < int(n) <= right)

print('Задайте конечное число диапазона: ', end='')
right = int(input())
num = random.randint(1, right)
tries = 0

while True:
    n = input()
    if not is_valid(n):
        print(f'А может быть все-таки введем целое число от 1 до {right}?')
        continue

    tries += 1
    
    if int(n) < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif int(n) > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали, поздравляем! Число попыток: {tries}')
        print('Сыграем ещё раз? (д = да, н = нет)')
        answer = input().lower()
        if answer == 'д':
            print('Задайте конечное число диапазона: ', end='')
            right = int(input())
            num = random.randint(1, right)
            tries = 0
            continue
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
            

