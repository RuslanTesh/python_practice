h_s = int(input())
v_s = int(input())

h_m = int(input())
v_m = int(input())

if (h_s != h_m and v_s == v_m) or (h_s == h_m and v_s != v_m):
    print('YES')
else: 
    print('NO')