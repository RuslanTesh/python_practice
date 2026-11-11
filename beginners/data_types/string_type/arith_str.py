a = input()
b = input()
c = input()

la = len(a)
lb = len(b)
lc = len(c)

max_n = max(la, lb, lc)
min_n = min(la, lb, lc)
mid_n = (la + lb + lc) - max_n - min_n

if max_n - mid_n == mid_n - min_n:
    print('YES')
else:
    print('NO')