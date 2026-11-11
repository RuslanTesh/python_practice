from random import randrange

digit = randrange(1, 101)

n = int(input())

while n != digit:
    if n > digit:
        print('Слишком много, попробуйте еще раз')
    elif n < digit:
        print('Слишком мало, попробуйте еще раз')

    n = int(input())
else:
    print('Вы угадали, поздравляем!')