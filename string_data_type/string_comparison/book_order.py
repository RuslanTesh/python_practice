n = int(input())
temp_author = ''
temp_name = ''

for i in range(n):
    s = input()
    author = s[0:s.index(' ')]
    name = s[s.index('«') + 1:s.index('»')]
    if temp_author < author:
        temp_author = author
        flag = True
    elif temp_author == author:
        if temp_name < name:
            temp_name = name
            flag = True
        else:
            flag = False
            break
    else:
        flag = False
        break

    temp_name = name
    temp_author = author

if flag:
    print('YES')    
else:
    print('NO')