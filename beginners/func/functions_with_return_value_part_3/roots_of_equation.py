from math import sqrt

def solve(a, b, c):

    D = b**2 - 4 * a * c
    
    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        if x1 <= x2:
            return x1, x2
        else:
            return x2, x1
    
    elif D == 0:
        return -b / (2 * a), -b / (2 * a)

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)




