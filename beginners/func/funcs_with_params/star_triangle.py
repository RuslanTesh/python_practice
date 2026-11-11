def draw_triangle(fill, base):
    high = base // 2 + 1
    for j in range(1, high + 1):
        print(fill * j)
    for k in range(high - 1, 0, -1):
        print(fill * k)


fill = input()
base = int(input())

draw_triangle(fill, base)