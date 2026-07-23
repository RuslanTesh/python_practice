n = int(input())
max_digit = 0 # five mistake
flag = False

while n != 0: # first mistake
    digit = n % 10
    if digit % 3 == 0 and digit >= max_digit:
        max_digit = digit # third mistake
        flag = True
    n //= 10 # second mistake 

if flag == False: # fouth mistake
    print('NO')
else:
    print(max_digit)