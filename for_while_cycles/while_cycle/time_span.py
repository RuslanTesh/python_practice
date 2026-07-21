h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

minutes1 = 60 * h1 + m1
minutes2 = 60 * h2 + m2

while minutes1 <= minutes2:
    if m1 < 10 and h1 < 10:
        print(0, h1, ":", 0, m1, sep='')
    elif m1 < 10:
        print(h1, ":", 0, m1, sep='')
    elif h1 < 10:
        print(0, h1, ":", m1, sep='')
    else:    
        print(h1, ":", m1, sep='')
    minutes1 += 1
    if m1 != 59:
        m1 += 1
    else:
        h1 += 1
        m1 = 0

