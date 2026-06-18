h_s = int(input())
v_s = int(input())

h_m = int(input())
v_m = int(input())

if (h_m - 1 == h_s or h_s == h_m + 1 or h_s == h_m) and (v_m == v_s or v_m - 1 == v_s or v_s == v_m + 1):
    print('YES')
else:
    print('NO')