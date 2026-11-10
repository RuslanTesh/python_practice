def draw_triangle():
    space = 7
    for weight in range(1, 16, 2):
        print(' ' * space + '*' * weight)
        space -= 1

draw_triangle()




